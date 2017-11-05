import os

import nltk
import numpy as np

from utils.io_file import read_vcb
from utils.marco import funcDict_frame, cand_num
from preprocess.vocabulary import vcb_dict

def get_candidate_word(clst, vcb_key):
    wlst = []
    for i in clst:
        wlst += read_vcb(vcb_key + '-%03d'%i)
    common_lst = nltk.FreqDist(wlst).most_common()
    return [wrd for (wrd, cnt) in common_lst if cnt >= cand_num]

def word_freq(argv_lst):
    # untuple arguments
    [clst, vcb_key] = argv_lst
    cwrd = get_candidate_word(clst, vcb_key)

    ftr_matrix = []
    for i in range(120):
        ftr_vector = [0] * len(cwrd)
        wlst = read_vcb(vcb_key + '-%03d'%i)
        for ii in range(len(cwrd)):
            ftr_vector[ii] = wlst.count(cwrd[ii])
        ftr_matrix += [ftr_vector]

    return ftr_matrix

ftr_dict = {
    'word freq': word_freq,
}

def extract_feature_from_text(ftr_key, vcb_key, clst):
    # check if vcb_key legal
    # if illegal, system exit
    vcb_func = lambda x: x
    funcDict_frame(vcb_dict, vcb_key, [], vcb_func)

    # call feature extraction
    ftr_lst = [clst, vcb_key]
    return funcDict_frame(ftr_dict, ftr_key, ftr_lst)