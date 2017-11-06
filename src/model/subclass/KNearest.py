from sklearn.neighbors import KNeighborsClassifier

from ..classifier import CLASSIFIER

class KN_classifier(CLASSIFIER):
    def train(self):
        # untuple argv
        [argv_n] = self.argv_lst

        print('K-Nearest training ...')
        self.model = KNeighborsClassifier(n_neighbors=argv_n)
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