import os, sys

# sentence split mark
snt_mark = '#'
# vocabulary split mark
vcb_mark = '/'
# number of word candidate for featured vector
cand_num = 150
# chapters for building features, 40 vs 40
ftr_lst = [55, 12, 40, 27, 38, 13, 46, 32, 18, 16, 53, 59, 51,  4, 21, 64, 14, 10, 57, 26,
           61,  6, 78, 35, 66, 65,  7, 67, 36, 54, 31, 15, 29, 50, 68, 52, 44, 71, 76, 58,
           80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
           100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]
# training set, 20 vs 20
train_80 = [36, 66, 28, 39, 2, 50, 53, 6, 76, 71, 75, 73, 56, 67, 31, 34, 3, 22, 25, 48]
train_40 = [96, 92, 105, 119, 80, 112, 88, 107, 86, 94, 97, 99, 117, 84, 111, 81, 87, 95, 103, 83]
# test set 60 vs 20
test_80 = [57, 19, 15, 70, 79, 27, 41, 20, 45, 7, 68, 44, 65, 54, 8, 35, 24, 5, 9, 11, 14, 60, 74, 47, 32, 0, 37, 40, 10, 49, 77, 61, 52, 30, 13, 29, 4, 63, 38, 12, 78, 43, 58, 46, 16, 23, 33, 17, 55, 59, 42, 51, 26, 62, 21, 18, 1, 72, 69, 64]
test_40 = [114, 89, 85, 90, 108, 82, 102, 98, 116, 91, 100, 109, 110, 93, 118, 106, 104, 115, 101, 113]

def regularize_root_dir():
    default_dir = os.path.dirname(os.path.realpath(__file__))
    for i in range(2):
        default_dir = os.path.dirname(default_dir)

    if len(sys.argv) == 1:
        return default_dir
    elif len(sys.argv) == 2:
        target_dir = str(sys.argv[1])
        # if target directory does not exist
        if os.path.exists(target_dir) == False:
            print('Target directory not found!')
            sys.exit()
        # else, if target directory exists
        else:
            return os.path.realpath(target_dir)
    else:
        print('Error in argument input!')
        sys.exit()

root_dir = regularize_root_dir()

file_dict = {}
for i in range(120):
    file_dict['sent-%03d' % i] = os.path.join(root_dir, 'data/sent', '%03d.txt' % i)
    file_dict['epub-%03d' % i] = os.path.join(root_dir, 'data/epub', 'chap%03d.html' % i)
    file_dict['jieba-%03d' % i] = os.path.join(root_dir, 'data/jieba', '%03d.txt' % i)

file_dict['manual-dict'] = os.path.join(root_dir, 'data/manual-dict.txt')


def funcDict_frame(argv_dct, argv_key, argv_lst, arg_fun=None):
    # wrong key
    if argv_key not in argv_dct.keys():
        print('Wrong option! Enter:')
        end = min([5, len(argv_dct)])
        for i in list(argv_dct.keys())[: end]:
            print('\t', i)
        print('\t...')
        sys.exit()
    # else correct
    else:
        if arg_fun == None:
            return argv_dct[argv_key](argv_lst)
        else:
            return arg_fun(argv_lst)