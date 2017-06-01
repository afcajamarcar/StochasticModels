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

        # Check is fit had been called
        check_is_fitted(self, ['X_', 'y_'])

        # Input validation
        X = check_array(X)


        closest = np.argmin(euclidean_distances(X, self.X_), axis=1)
        print closest
        return self.y_[closest]


matrixData = []
vectorTarget = []

with open('../LearningInformation/learningBayesianMulticlassGenuine.csv') as f:
    readerGenuine = csv.reader(f)

    readerGenuine.next()
    for i in readerGenuine:
        matrixData.append(map(float,  i[:len(i)-1]))
        #matrixData.append(map(float, i[2:5] + i[25:len(i) - 1]))
        vectorTarget.append(int(i[len(i)-1]))

readerForgeries = list()
with open('../LearningInformation/learningBayesianMulticlassForgeries.csv') as f:
    readerForgeriestmp = csv.reader(f)
    readerForgeriestmp.next()
    for i in readerGenuine:
        matrixData.append(map(float,  i[:len(i)-1]))
        #matrixData.append(map(float, i[2:5] + i[25:len(i) - 1]))
        vectorTarget.append(int(i[len(i)-1]))

matrixData = np.array(matrixData)
vectorTarget = np.array(vectorTarget)

X_train, X_test, y_train, y_test = train_test_split(matrixData, vectorTarget, test_size=0.2, random_state=0)

asdsada = TemplateClassifier().fit(X_train, y_train)
print asdsada
y_predict = asdsada.predict(X_test)

print accuracy_score(y_test, y_predict)

###################### Naive Bayes
naiveClassifier = GaussianNB().fit(X_train, y_train)
y_predict_NaiveProba = naiveClassifier.predict_proba(X_test)
y_predict_Naive = naiveClassifier.predict(X_test)

#print accuracy_score(y_test, y_predict_Naive)


######## Crossvalidation
#scores = cross_val_score(asdsada, matrixData, vectorTarget, cv=5)
#print("Accuracy SVM: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))

#scores = cross_val_score(naiveClassifier, matrixData, vectorTarget, cv=5)
#print("Accuracy Naive: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))





