from utils.marco import snt_mark, funcDict_frame
from utils.io_file import read_file
from .word_parser.suffix_tree import suffix_tree_parser
from .word_parser.jieba import jieba_parser

def sentence_length_count(text):
    sents = text.split(snt_mark)
    sent_len = [len(i) for i in sents]
    len_max = max(sent_len)

    # cnt_len_lst[10] = 34
    # 34 sentences in text have length of 10
    cnt_len_lst = [0] * (len_max + 1)
    for i in sent_len:
        cnt_len_lst[i] += 1

    # word count
    cnt_sum_lst = []
    for i_len in range(len(cnt_len_lst)):
        cnt_sum = 0
        for ii_len, ii_cnt in enumerate(cnt_len_lst):
            if ii_len >= i_len:
                cnt_sum += ii_cnt * (ii_len - i_len + 1)
        cnt_sum_lst += [cnt_sum]
        
    return cnt_len_lst, cnt_sum_lst

vcb_dict = {
    'suffix-tree': suffix_tree_parser,
    'jieba': jieba_parser,
}

def save_parsed_words(vcb_key):
    chap_lst = []
    for i in range(120):
        chap_lst += [read_file('sent-%03d' % i)]

    # vocabulary function dictionary
    vcb_lst = [chap_lst]
    funcDict_frame(vcb_dict, vcb_key, vcb_lst)