import numpy as np

from utils.marco import train_80, train_40, test_80, test_40

class CLASSIFIER:
    def __init__(self):
        self.Ypred = []
        self.performance = {}

    def read(self, matrix120):
        matrix120 = np.array(matrix120)
        # read true and false samples
        self.Xtrain = matrix120[train_80 + train_40]
        self.Ytrain = np.array([1] * len(train_80) + [0] * len(train_40))
        # shuffle
        index_shuffle = np.arange(self.Ytrain.shape[0])
        np.random.shuffle(index_shuffle)
        self.Xtrain = self.Xtrain[index_shuffle]
        self.Ytrain = self.Ytrain[index_shuffle]

        # test set
        self.Xtest = matrix120[test_80 + test_40]
        self.Ytest = np.array([1] * len(test_80) + [0] * len(test_40))

    def train(self):
        pass

    def predict(self, extern=None):
        pass

    def evaluate(self):
        match = (self.Ypred == self.Ytest).sum()
        self.performance['accuracy'] = match / (self.Ytest.shape[0] * 1.0)

        return self.performance

    def report(self):
        self.evaluate()
        print('Report:')
        for i in self.performance:
            print('\t%s: %.2f%%'%(i, self.performance[i] * 100.0))