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

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels
import itertools
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score




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
    readerForgeries = [i for i in readerForgeriestmp]

readerForgeries = random.sample(readerForgeries, 48)

for forgSing in readerForgeries:
    matrixData.append(map(float, forgSing[:len(forgSing) - 1]))
    # matrixData.append(map(float, i[2:5] + i[25:len(i) - 1]))
    vectorTarget.append(0)

matrixData = np.array(matrixData)
vectorTarget = np.array(vectorTarget)

totalScores = []
totalF1Scores = []

for j in range(10):
    # Cross validation
    scores = []
    f1Scores = []

    ##### Cross Validation
    for i in range(5):
        X_train, X_test, y_train, y_test = train_test_split(matrixData, vectorTarget, test_size=0.2,
                                                            random_state=random.randint(1, 10))

        ###################### Naive Bayes
        naiveClassifier = GaussianNB().fit(X_train, y_train)
        y_predict_Naive = naiveClassifier.predict(X_test)

        scores.append(accuracy_score(y_test, y_predict_Naive))
        f1Scores.append(f1_score(y_test, y_predict_Naive, average='weighted'))

    print("Accuracy Naive: %0.4f (+/- %0.4f)" % (np.array(scores).mean(), np.array(scores).std() * 2))
    print("F1 Naive: %0.4f (+/- %0.4f)" % (np.array(f1Scores).mean(), np.array(f1Scores).std() * 2))

    totalF1Scores.append(np.array(f1Scores).mean())
    totalScores.append(np.array(scores).mean())

print
print
print("Accuracy Naive: %0.4f (+/- %0.4f)" % (np.array(scores).mean(), np.array(scores).std() * 2))
print("F1 Naive: %0.4f (+/- %0.4f)" % (np.array(f1Scores).mean(), np.array(f1Scores).std() * 2))







########################################################
# Plot the confusion matrix
########################################################
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        cm = np.around(cm, decimals=2)
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.colorbar()

# Compute confusion matrix
cnf_matrix = confusion_matrix(y_test, y_predict_Naive)
np.set_printoptions(precision=2)

class_names = ['00','01','02','03','04','06','09','12','14','15','16']

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(np.around(cnf_matrix, decimals=3), classes=class_names, normalize=True,
                      title='Normalized confusion matrix')
# plt.show()

#scores = cross_val_score(naiveClassifier, matrixData, vectorTarget, cv=5)
#print("Accuracy Naive: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))


