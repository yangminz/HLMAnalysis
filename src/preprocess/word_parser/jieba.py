import os

import jieba

from utils.io_file import save_txt, read_file
from utils.marco import snt_mark, vcb_mark, file_dict

def jieba_parser(argv_lst):
    # un-tuple arguments
    [chap_lst] = argv_lst

    # hlm_words
    hlm_words = read_file('manual-dict').split('\n')
    for i in hlm_words:
        jieba.add_word(i)

    all_saved = True
    for i in range(len(chap_lst)):
        # existence check
        fpath = file_dict['jieba-%03d'%i]
        if os.path.isfile(fpath) == False:
            all_saved = False
            # sentence split list for one chapter
            sent_text = chap_lst[i].split(snt_mark)
            word_lst = []
            # word parse for each sentence:
            for ii in sent_text:
                tmp = vcb_mark.join(jieba.cut(ii))
                word_lst += tmp.split(vcb_mark)
            # regularize
            content = vcb_mark.join(word_lst)
            content = content.lstrip(vcb_mark)
            content = content.strip(vcb_mark)
            # saving
            save_txt(fpath, content)
        else:
            all_saved = all_saved and True
    if all_saved:
        print('Vocabulary files already saved.')