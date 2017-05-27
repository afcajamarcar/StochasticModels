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


matrixData = []
vectorTarget = []

with open('learningBayesianMulticlassGenuine.csv') as f:
    readerGenuine = csv.reader(f)

    readerGenuine.next()
    for i in readerGenuine:
        matrixData.append(map(float,  i[:len(i)-1]))
        #matrixData.append(map(float, i[2:5] + i[25:len(i) - 1]))
        vectorTarget.append(int(i[len(i)-1]))

matrixData = np.array(matrixData)
vectorTarget = np.array(vectorTarget)

X_train, X_test, y_train, y_test = train_test_split(matrixData, vectorTarget, test_size=0.1, random_state=0)


asdsada = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
y_predict = asdsada.predict(X_test)

print accuracy_score(y_test, y_predict)

###################### Naive Bayes
naiveClassifier = GaussianNB().fit(X_train, y_train)
y_predict_NaiveProba = naiveClassifier.predict_proba(X_test)
y_predict_Naive = naiveClassifier.predict(X_test)

print y_predict_NaiveProba
print
print y_predict_Naive
print y_test
#print accuracy_score(y_test, y_predict_Naive)


######## Crossvalidation
scores = cross_val_score(asdsada, matrixData, vectorTarget, cv=10)
print("Accuracy SVM: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))

scores = cross_val_score(naiveClassifier, matrixData, vectorTarget, cv=10)
print("Accuracy Naive: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))





