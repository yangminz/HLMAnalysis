import os

import nltk
import numpy as np

from utils.io_file import read_vcb
from utils.marco import funcDict_frame, cand_num, ftr_lst
from preprocess.vocabulary import vcb_dict

def get_candidate_word(vcb_key):
    wlst = []
    for i in ftr_lst:
        wlst += read_vcb('%s-%03d'%(vcb_key, i))
    common_lst = nltk.FreqDist(wlst).most_common()
    return [wrd for (wrd, cnt) in common_lst if cnt >= cand_num]

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

def word_freq(argv_lst):
    # untuple arguments
    [vcb_key] = argv_lst
    cwrd = get_candidate_word(vcb_key)

    return given_word_frequency([cwrd, vcb_key])

ftr_dict = {
    'word freq': word_freq,
    'given word freq': given_word_frequency,
}

def extract_feature_from_text(ftr_key, vcb_key):
    # check if vcb_key legal
    # if illegal, system exit
    vcb_func = lambda x: x
    funcDict_frame(vcb_dict, vcb_key, [], vcb_func)

    # call feature extraction
    argv_lst = [vcb_key]
    return funcDict_frame(ftr_dict, ftr_key, argv_lst)