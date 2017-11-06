from sklearn.tree import DecisionTreeClassifier

from ..classifier import CLASSIFIER

class DTree_classifier(CLASSIFIER):
    def train(self):
        print('Decision Tree training ...')
        self.model = DecisionTreeClassifier()
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