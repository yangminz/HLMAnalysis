from utils.io_file import clear_cache

from preprocess.sentence import save_splited_sentence
from preprocess.vocabulary import save_parsed_words

from model.feature import extract_feature_from_text

save_splited_sentence()
save_parsed_words('jieba')

# random 40 for first 80 and all last 40
matrix120 = [
    extract_feature_from_text('bag of words', ['jieba']),
    extract_feature_from_text('sentence length', []),
]

from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

X = matrix120[0]
y = [1]*80 + [0]*40

pca = PCA(n_components=2)
X = pca.fit(X).transform(X)

for i in range(120):
    if i <= 79:
        print(X[i][0], '\t', X[i][1])
    else:
        print(X[i][0], '\t\t', X[i][1])