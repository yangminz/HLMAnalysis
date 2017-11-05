from utils.io_file import clear_cache
from utils.marco import ftr_lst
from preprocess.sentence import save_splited_sentence
from preprocess.vocabulary import save_parsed_words
from model.feature import extract_feature_from_text
from model.subclass.svm import SVM_classifier

save_splited_sentence()
save_parsed_words('jieba')

# random 40 for first 80 and all last 40
matrix120 = extract_feature_from_text('word freq', 'jieba', ftr_lst)

c = SVM_classifier()
c.read(matrix120)
c.train()
c.predict()
c.report()

print('See You.\a')