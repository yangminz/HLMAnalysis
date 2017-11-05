import os, re

from utils.marco import root_dir, snt_mark
from utils.io_file import read_file, save_txt

replace_lst = [
    '。', '，', '、', '＇', '：', '∶', '；', '?', '‘', '’', '“', '”', '〝', '〞', 'ˆ', 'ˇ', '﹕', '︰', '﹔', '﹖', '﹑', '·', '¨', '…', '.', '¸', ';', '！', '´', '？', '！', '～', '—', 'ˉ', '｜', '‖', '＂', '〃', '｀', '@', '﹫', '¡', '¿', '﹏', '﹋', '﹌', '︴', '々', '﹟', '#', '﹩', '$', '﹠', '&', '﹪', '%', '*', '﹡', '﹢', '﹦', '﹤', '‐', '￣', '¯', '―', '﹨', 'ˆ', '˜', '﹍', '﹎', '+', '=', '<', '＿', '_', '-', '\\', 'ˇ', '~', '﹉', '﹊', '（', '）', '〈', '〉', '‹', '›', '﹛', '﹜', '『', '』', '〖', '〗', '［', '］', '《', '》', '〔', '〕', '{', '}', '「', '」', '【', '】', '︵', '︷', '︿', '︹', '︽', '_', '﹁', '﹃', '︻', '︶', '︸', '﹀', '︺', '︾', 'ˉ', '﹂', '﹄', '︼',
    '\"', '\'', '.', ',', '．', '\n', '\t'
]

strip_lst = [
    ' +', '　+', snt_mark + '+'
]

def regularize_epub(chap_id):
    print('Reading epub data', chap_id, '...')
    # read raw text
    raw_text = read_file('epub-%03d'%chap_id)
    ib = raw_text.find('<body>')
    ie = raw_text.find('</body>')
    raw_text = raw_text[ib: ie]
    # strip html tag
    raw_text = re.sub('<[a-z/0-9]*>', '', raw_text)
    # replace puncuation
    for i in replace_lst:
        raw_text = raw_text.replace(i, snt_mark)
    # strip with `snt_mark`
    for i in strip_lst:
        raw_text = re.sub(i, snt_mark, raw_text)

    return raw_text

def save_splited_sentence():
    # make dir
    sent_dir = os.path.join(root_dir, 'data/sent')
    os.makedirs(sent_dir, exist_ok=True)
    # check if already saved
    all_saved = True
    for i in range(120):
        filename = os.path.join(sent_dir, '%03d.txt'%i)
        # existence check
        if os.path.isfile(filename) == False:
            all_saved = False
            # reading
            chap_text = regularize_epub(i)
            # saving
            save_txt(filename, chap_text)
        else:
            all_saved = all_saved and True
    if all_saved:
        print('Sentence split files already saved.')