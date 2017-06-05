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


from matplotlib import transforms
import matplotlib.pyplot as plt
import resize as rz
import bayesianNetwork as bN
import gaussianSmoothing as GaussS
import os
import numpy as np

if __name__ == "__main__":

    # Header of CSV file
    print "CenterX,CenterY,Eccentricity,KurtosisX,KurtosisY," \
          "GrdGrid1_x,GrdGrid1_y,GrdGrid2_x,GrdGrid2_y,GrdGrid3_x,GrdGrid3_y,GrdGrid4_x,GrdGrid4_y," \
          "GrdGrid1_5,GrdGrid5_y,GrdGrid6_x,GrdGrid6_y,GrdGrid7_x,GrdGrid7_y,GrdGrid8_x,GrdGrid8_y," \
          "PressGrid1,PressGrid2,PressGrid3,PressGrid4,PressGrid5,PressGrid6,PressGrid7,PressGrid8," \
          "PressGrid9,PressGrid10,PressGrid11,PressGrid12,PressGrid13,PressGrid14,PressGrid15,PressGrid16," \
          "Label"
    #################################################
    # Genuine Files
    #################################################
    allFiles = next(os.walk("../TestSet"))[1]

    dataToTrain = {}

    for files in allFiles:
        folderFiles = next(os.walk("../TestSet/" + files))[2]

        for signature in folderFiles:

            img = rz.resizeSignature("../TestSet/" + files + "/" + signature)
            # Image filtering
            imgSmooted = GaussS.gaussianBlur(1, 0.5, img)
            imgFiltered = bN.filter(imgSmooted)

            # Calculate the ones in the matrix.
            blackPoints = bN.calculateBlackPoints(imgFiltered)

            # Calculate the center of mass
            centerMass = bN.centroid(blackPoints)

            # Calculate the eccentricity
            eccentricity = bN.calculateEccentricity(blackPoints)

            # Calculate the representative points of a signature
            # densePoints = bN.calculateDensePoints(blackPoints)

            # Calculate Kurtosis of blackpoints in signature
            kurtosis = bN.calculateKurtosis(blackPoints)

            # Print skew detection
            #  testSkew = bN.skewDetection(imgFiltered)

            # Calculate gradient in a grid 4x4 - Choosen just 2x2 important grid in the middle
            matrixGradient = bN.calculateGradient(blackPoints, imgFiltered.shape)

            # Calculate pressure in a grid 4x4
            matrixPresure = bN.calculatePressure(imgSmooted)

            label = 0
            if len(signature) < 11:
                label = int(files)

            print signature

            print str(round(centerMass[0], 4)) + "," + str(round(centerMass[1], 4)) + "," + str(
                round(eccentricity, 4)) + "," + \
                  str(round(kurtosis[0], 4)) + "," + str(round(kurtosis[1], 4)) + "," + \
                  str(round(matrixGradient[0][0][0], 4)) + "," + str(round(matrixGradient[0][0][1], 4)) + "," + str(
                round(
                    matrixGradient[0][1][0], 4)) + "," + str(round(matrixGradient[0][1][1], 4)) + "," + \
                  str(round(matrixGradient[0][2][0], 4)) + "," + str(round(matrixGradient[0][2][1], 4)) + "," + str(
                round(
                    matrixGradient[0][3][0], 4)) + "," + str(round(matrixGradient[0][3][1], 4)) + "," + \
                  str(round(matrixGradient[1][0][0], 4)) + "," + str(round(matrixGradient[1][0][1], 4)) + "," + str(
                round(
                    matrixGradient[1][1][0], 4)) + "," + str(round(matrixGradient[1][1][1], 4)) + "," + \
                  str(round(matrixGradient[1][2][0], 4)) + "," + str(round(matrixGradient[1][2][1], 4)) + "," + str(
                round(
                    matrixGradient[1][3][0], 4)) + "," + str(round(matrixGradient[1][3][1], 4)) + "," + \
                  str(round(matrixPresure[0][0], 4)) + "," + str(round(matrixPresure[0][1], 4)) + "," + str(
                round(matrixPresure[0][2], 4)) + "," + \
                  str(round(matrixPresure[0][3], 4)) + "," + \
                  str(round(matrixPresure[1][0], 4)) + "," + str(round(matrixPresure[1][1], 4)) + "," + str(round(
                matrixPresure[1][2], 4)) + "," + str(round(
                matrixPresure[1][3], 4)) + "," + \
                  str(round(matrixPresure[2][0], 4)) + "," + str(round(matrixPresure[2][1], 4)) + "," + str(round(
                matrixPresure[2][2], 4)) + "," + str(round(
                matrixPresure[2][3], 4)) + "," + \
                  str(round(matrixPresure[3][0], 4)) + "," + str(round(matrixPresure[3][1], 4)) + "," + str(round(
                matrixPresure[3][2], 4)) + "," + str(round(
                matrixPresure[3][3], 4)) + "," + \
                  str(int(label))


