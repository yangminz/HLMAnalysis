from utils.io_file import clear_cache

from preprocess.sentence import save_splited_sentence
from preprocess.vocabulary import save_parsed_words

from model.feature import extract_feature_from_text
from model.subclass.SupportVM import SVM_classifier
from model.subclass.GaussianNB import GNB_classifier
from model.subclass.MLPerceptron import MLP_classifier
from model.subclass.StochasticGD import SGD_classifier
from model.subclass.LinearDA import LDA_classifier
from model.subclass.DecisionTree import DTree_classifier
from model.subclass.KNearest import KN_classifier

save_splited_sentence()
save_parsed_words('jieba')

# random 40 for first 80 and all last 40
matrix120 = extract_feature_from_text('word freq', 'jieba')

classifier_lst = [
    SVM_classifier(),
    GNB_classifier(),
    MLP_classifier(['lbfgs', 1e-5, (256, 64, 8, 2), 1]),
    SGD_classifier(["hinge", "l2"]),
    LDA_classifier(),
    DTree_classifier(),
    KN_classifier([20])
]

for c in classifier_lst:
    c.read(matrix120)
    c.train()
    c.predict()
    c.report()

print('See You.\a')