from sklearn.naive_bayes import GaussianNB

from ..classifier import CLASSIFIER

class GNB_classifier(CLASSIFIER):
    def train(self):
        print('Gaussian Naive Bayes training ...')
        self.model = GaussianNB()
        self.model.fit(self.Xtrain, self.Ytrain)

    def predict(self, extern=None):
        # evaluate within Hong Lou Meng
        if extern == None:
            self.Ypred = self.model.predict(self.Xtest)
            return self.Ypred
        # evaluate by other external text
        else:
            # untuple extern argv
            [exX, exY] = extern
            self.model.predict(exX)