import os, sys, shutil

from .marco import root_dir, funcDict_frame, vcb_mark

def read_file(text_key):
    # make dictionary
    text_dict = {}
    for i in range(120):
        text_dict['sent-%03d'%i] = os.path.join(root_dir, 'data/sent', '%03d.txt'%i)
        text_dict['epub-%03d'%i] = os.path.join(root_dir, 'data/epub', 'chap%03d.html'%i)
        text_dict['jieba-%03d'%i] = os.path.join(root_dir, 'data/jieba', '%03d.txt'%i)

    def foo(foo_lst):
        # untuple arguments
        [foo_dict, foo_key] = foo_lst
        # existence check
        fpath = foo_dict[foo_key]
        if os.path.isfile(fpath):
            content = open(fpath, 'r').read()
            return content
        else:
            print('File %s not exists'%fpath)
            sys.exit()

    foo_lst = [text_dict, text_key]
    return funcDict_frame(text_dict, text_key, foo_lst, foo)

def read_vcb(text_key):
    content = read_file(text_key)
    return content.split(vcb_mark)

def save_txt(filename, content):
    print('Saving to txt file', filename, '...')
    # directory existence check
    fdir = os.path.dirname(filename)
    if os.path.isdir(fdir) == False:
        os.makedirs(fdir, exist_ok=True)
    # write file
    wf = open(filename, 'w')
    wf.write(content)
    wf.close()

def save_list(filename, ctnt_lst):
    print('Saving list to file', filename, '...')
    # directory existence check
    fdir = os.path.dirname(filename)
    if os.path.isdir(fdir) == False:
        os.makedirs(fdir, exist_ok=True)
    # write file
    wf = open(filename, 'w')
    content = '\n'.join(ctnt_lst)
    wf.write(content)
    wf.close()

def clear_cache():
    dir_lst = [
        os.path.join(root_dir, 'data/sent'),
        os.path.join(root_dir, 'data/jieba'),
    ]

    for i in dir_lst:
        shutil.rmtree(i)