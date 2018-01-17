import numpy as np

from utils.marco import train_80, train_40, test_80, test_40

class CLASSIFIER:
    def __init__(self, argv_lst=None):
        if argv_lst != None:
            self.argv_lst = argv_lst
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
        match = (self.Ypred == self.Ytest)

        for k in ('TP', 'TN', 'FP', 'FN'):
            self.performance[k] = []

        for i in range(len(test_80)):
            if match[i] == True:
                self.performance['TP'] += [test_80[i]]
            else:
                self.performance['FN'] += [test_80[i]]
        
        for i in range(len(test_40)):
            ii = i + len(test_80)
            if match[ii] == True:
                self.performance['TN'] += [test_40[i]]
            else:
                self.performance['FP'] += [test_40[i]]

        self.performance['accuracy'] = match.sum() * 100.0 / len(match)
        self.performance['precision'] = len(self.performance['TP']) * 100.0 / (len(self.performance['TP']) + len(self.performance['FP']))
        self.performance['recall'] = len(self.performance['TP']) * 100.0 / (len(self.performance['TP']) + len(self.performance['FN']))

        return self.performance

    def report(self):
        self.evaluate()
        print('Report:')
        for i in self.performance:
            print('\t%s:'%(i), self.performance[i])