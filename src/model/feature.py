import os

import nltk
import numpy as np

from utils.io_file import read_vcb, read_snt
from utils.marco import funcDict_frame, cand_num, ftr_lst, common_num, candidate_words
from preprocess.vocabulary import vcb_dict

def get_candidate_word(vcb_key):
    # check if marco setting is legal
    assert common_num >= cand_num

    word_each_chapter = []
    all_word = []
    for i in ftr_lst:
        word_each_chapter += [read_vcb('%s-%03d'%(vcb_key, i))]
        all_word += read_vcb('%s-%03d'%(vcb_key, i))
     
    common_tuple = nltk.FreqDist(all_word).most_common()
    common_words = [wrd for (wrd, cnt) in common_tuple]

    std_tuple = []
    for w in common_words[: common_num]:
        appear_lst = [i.count(w) for i in word_each_chapter]
        std_tuple += [[np.std(appear_lst), w]]
    std_tuple.sort()

    return [w for [std,w] in std_tuple[: cand_num]]

def given_word_frequency(argv_lst):
    # untuple arguments
    [cwrd, vcb_key] = argv_lst

    ftr_matrix = []
    for i in range(120):
        ftr_vector = [0] * len(cwrd)
        wlst = read_vcb('%s-%03d'%(vcb_key, i))
        for ii in range(len(cwrd)):
            ftr_vector[ii] = wlst.count(cwrd[ii])
        ftr_matrix += [ftr_vector]

    return ftr_matrix

def bag_of_words_with_calculation(argv_lst):
    # untuple arguments
    [vcb_key] = argv_lst
    cwrd = get_candidate_word(vcb_key)
    return given_word_frequency([cwrd, vcb_key])

def bag_of_words(argv_lst):
    # directly import candidate words from marco
    # untuple arguments
    [vcb_key] = argv_lst
    return given_word_frequency([candidate_words, vcb_key])

def sentence_length(argv_lst):
    ftr_matrix = []
    for i in range(120):
        # sentence length vector for one chapter
        ftr_vector = [0] * 30
        for ii in range(30):
            slen = ii + 1
            snt_lst = read_snt('sent-%03d' % i)
            slen_lst = [len(s) for s in snt_lst]
            ftr_vector[ii] = slen_lst.count(slen)  / (len(snt_lst) * 1.0)
        ftr_matrix += [ftr_vector]

    return ftr_matrix

ftr_dict = {
    'sentence length': sentence_length,
    'bag of words': bag_of_words,
}

def extract_feature_from_text(ftr_key, argv_lst):
    # check if vcb_key legal
    # if illegal, system exit
    if len(argv_lst) > 0:
        vcb_func = lambda x: x
        funcDict_frame(vcb_dict, argv_lst[0], [], vcb_func)

    # call feature extraction
    return funcDict_frame(ftr_dict, ftr_key, argv_lst)