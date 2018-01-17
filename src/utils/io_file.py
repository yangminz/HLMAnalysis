import os, sys, shutil

from .marco import root_dir, funcDict_frame, vcb_mark, snt_mark, file_dict

def read_file(text_key):
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

    foo_lst = [file_dict, text_key]
    return funcDict_frame(file_dict, text_key, foo_lst, foo)

def read_vcb(text_key):
    content = read_file(text_key)
    return content.split(vcb_mark)

def read_snt(text_key):
    content = read_file(text_key)
    return content.split(snt_mark)

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