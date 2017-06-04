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
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.metrics import f1_score




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

            secondClassifier = svm.SVC(kernel='linear', C=0.2).fit(matrixDataTmp, vectorTargetTmp)
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

totalScores = []
totalF1Scores = []


y_predict_best = []
accuracyFlag = 0


for j in range(5):
    # Cross validation
    scores = []
    f1Scores = []

    y_predictB = []
    accuracyTmp11 = 0
    for i in range(5):
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
        y_predict = asdsada.predict(X_test)


        accuracyTmp = accuracy_score(y_realTest, y_predict)
        if accuracyTmp > accuracyTmp11:
            accuracyTmp11 = accuracyTmp
            y_predictB = y_predict

        scores.append(accuracy_score(y_realTest, y_predict))
        f1Scores.append(f1_score(y_realTest, y_predict, average='weighted'))

    accuracyCurrent = np.array(scores).mean()

    if accuracyCurrent > accuracyFlag:
        accuracyFlag = accuracyCurrent
        y_predict_best = y_predictB

    print("Accuracy Naive: %0.4f (+/- %0.4f)" % (accuracyCurrent, np.array(scores).std() * 2))
    print("F1 Naive: %0.4f (+/- %0.4f)" % (np.array(f1Scores).mean(), np.array(f1Scores).std() * 2))

    totalF1Scores.append(np.array(f1Scores).mean())
    totalScores.append(accuracyCurrent)

print
print
print("Accuracy Naive: %0.4f (+/- %0.4f)" % (np.array(scores).mean(), np.array(scores).std() * 2))
print("F1 Naive: %0.4f (+/- %0.4f)" % (np.array(f1Scores).mean(), np.array(f1Scores).std() * 2))


print y_predict_best
print y_realTest

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
cnf_matrix = confusion_matrix(y_realTest, y_predict_best)
np.set_printoptions(precision=2)

class_names = ['00','01','02','03','04','06','09','12','14','15','16']

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(np.around(cnf_matrix, decimals=3), classes=class_names, normalize=True,
                      title='Normalized confusion matrix')
plt.show()

#scores = cross_val_score(naiveClassifier, matrixData, vectorTarget, cv=5)
#print("Accuracy Naive: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))





