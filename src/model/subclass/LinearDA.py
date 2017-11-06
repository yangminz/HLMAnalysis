from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from ..classifier import CLASSIFIER

class LDA_classifier(CLASSIFIER):
    def train(self):
        print('Linear Discrininant Analysis training ...')
        self.model = LinearDiscriminantAnalysis()
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