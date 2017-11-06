from sklearn.neural_network import MLPClassifier

from ..classifier import CLASSIFIER

class MLP_classifier(CLASSIFIER):
    def train(self):
        # untuple argv
        [argv_solver, argv_alpha, argv_hidden, argv_rnd_state] = self.argv_lst

        print('Multi-layer Perceptron training ...')
        self.model = MLPClassifier(solver=argv_solver, alpha=argv_alpha,
                                   hidden_layer_sizes=argv_hidden, random_state=argv_rnd_state)
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