from sklearn.linear_model import SGDClassifier

from ..classifier import CLASSIFIER

class SGD_classifier(CLASSIFIER):
    def train(self):
        # untuple argv
        [argv_loss, argv_penalty] = self.argv_lst

        print('Stochastic Gradient Descent training ...')
        self.model = SGDClassifier(loss=argv_loss, penalty=argv_penalty)
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