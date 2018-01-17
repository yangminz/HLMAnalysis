import numpy as np

x1 = list(np.arange(80))

x2 = list(80 + np.arange(40))

def count_sent_len(idlst):
    len_lst = []
    for i in idlst:
        strfile = open('../../data/sent/%03d.txt'%i).read()
        sentlst = strfile.split('#')
        len_lst += [len(sent) for sent in sentlst]
    for slen in range(50):
        print(slen, '\t', len_lst.count(slen) / (len(len_lst) * 1.0))

count_sent_len(x1)
print('==')
count_sent_len(x2)