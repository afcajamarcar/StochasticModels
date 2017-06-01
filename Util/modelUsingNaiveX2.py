# Sthochastic Models
########################################
# Authors
# Jeisson Andres Prieto Velandia
# Andres Felipe Cajamarca Rojas
# Juan Felipe Arango Manrique
########################################
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
import csv
import random

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.base import BaseEstimator, ClassifierMixin


import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels
from sklearn.metrics import euclidean_distances
class TemplateClassifier(BaseEstimator, ClassifierMixin):

    def __init__(self, demo_param='demo'):
        self.demo_param = demo_param

    def fit(self, X, y):

        # Check that X and y have correct shape
        X, y = check_X_y(X, y)
        # Store the classes seen during fit
        self.classes_ = unique_labels(y)

        self.X_ = X
        self.y_ = y
        # Return the classifier
        return self

    def predict(self, X):

        def hibridModel(x):
            naiveClassifier = GaussianNB().fit(self.X_, self.y_)
            y_predict_Naive = naiveClassifier.predict(x)[0]


            matrixDataTmp = []
            vectorTargetTmp = []
            with open('../LearningInformation/learningBayesianBinomial'+str(y_predict_Naive) + '.csv') as f:
                readerGenuine = csv.reader(f)

                readerGenuine.next()
                for i in readerGenuine:
                    matrixDataTmp.append(map(float, i[:len(i) - 1]))
                    # matrixData.append(map(float, i[2:5] + i[25:len(i) - 1]))
                    vectorTargetTmp.append(int(i[len(i) - 1]))

            secondClassifier = svm.SVC(kernel='linear', C=0.8).fit(matrixDataTmp, vectorTargetTmp)
            prediction = secondClassifier.predict(x)[0]
            if prediction == 1:
                return y_predict_Naive
            else:
                return 0
        # Check is fit had been called
        check_is_fitted(self, ['X_', 'y_'])

        # Input validation
        X = check_array(X)

        y_predicted = [hibridModel(x) for x in X]
        return y_predicted


def split_train(X, y, test_size=0.2):
    index = random.sample(range(len(X)), int(len(X)*test_size))
    return index


matrixData = []
vectorTarget = []
realVectorTarget = []
with open('../LearningInformation/learningBayesianMulticlassGenuine.csv') as f:
    readerGenuine = csv.reader(f)

    readerGenuine.next()
    for i in readerGenuine:
        matrixData.append(map(float,  i[:len(i)-1]))
        #matrixData.append(map(float, i[2:5] + i[25:len(i) - 1]))
        vectorTarget.append(int(i[len(i)-1]))
        realVectorTarget.append(int(i[len(i)-1]))

with open('../LearningInformation/learningBayesianMulticlassForgeries.csv') as f:
    readerForgeriestmp = csv.reader(f)
    readerForgeriestmp.next()
    for i in readerForgeriestmp:
        matrixData.append(map(float,  i[:len(i)-1]))
        #matrixData.append(map(float, i[2:5] + i[25:len(i) - 1]))
        vectorTarget.append(int(i[len(i)-1]))
        realVectorTarget.append(0)

matrixData = np.array(matrixData)
vectorTarget = np.array(vectorTarget)
scores = []

for i in range(10):
    X_train, X_test, y_train, y_test, y_realTest = [],[],[],[],[]

    indexTest = set(split_train(matrixData, vectorTarget))


    for index in range(len(matrixData)):
        if index in indexTest:
            X_test.append(matrixData[index])
            y_test.append(vectorTarget[index])
            y_realTest.append(realVectorTarget[index])
        else:
            X_train.append(matrixData[index])
            y_train.append(vectorTarget[index])

    asdsada = TemplateClassifier().fit(X_train, y_train)
    print asdsada
    y_predict = asdsada.predict(X_test)

    scores.append(accuracy_score(y_realTest, y_predict))

    #print accuracy_score(y_test, y_predict_Naive)

print("Accuracy SVM: %0.4f (+/- %0.4f)" % (np.array(scores).mean(), np.array(scores).std() * 2))

#scores = cross_val_score(naiveClassifier, matrixData, vectorTarget, cv=5)
#print("Accuracy Naive: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))





