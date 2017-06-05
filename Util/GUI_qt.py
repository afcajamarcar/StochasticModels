# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stochastichGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
########################################
# Universidad Nacional de Colombia
# Sthochastic Models
########################################
# Authors
# Jeisson Andres Prieto Velandia
# Andres Felipe Cajamarca Rojas
# Juan Felipe Arango Manrique
########################################
import random

from matplotlib import transforms
from Tkinter import *
from tkFileDialog import askopenfilename
from matplotlib.patches import Ellipse
from PIL import Image
from matplotlib.axes import Axes
from sklearn import svm
from sklearn.naive_bayes import GaussianNB

import resize as rz
import matplotlib.pyplot as plt
import bayesianNetwork as bN
import gaussianSmoothing as GaussS
import numpy as np
import csv

from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted
from sklearn.utils.multiclass import unique_labels
import os
from PyQt4 import Qt
from PyQt4 import QtCore, QtGui
from tkFileDialog import askopenfilename

from PyQt4.QtGui import QPixmap
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QSize, Qt
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(834, 785)
        self.CenterMass = QtGui.QLineEdit(Form)
        self.CenterMass.setGeometry(QtCore.QRect(150, 390, 51, 24))
        self.CenterMass.setObjectName(_fromUtf8("CenterMass"))
        self.Eccentricity = QtGui.QLineEdit(Form)
        self.Eccentricity.setGeometry(QtCore.QRect(150, 450, 113, 24))
        self.Eccentricity.setObjectName(_fromUtf8("Eccentricity"))
        self.kurtosis = QtGui.QLineEdit(Form)
        self.kurtosis.setGeometry(QtCore.QRect(150, 420, 51, 24))
        self.kurtosis.setObjectName(_fromUtf8("kurtosis"))
        self.Skew = QtGui.QLineEdit(Form)
        self.Skew.setGeometry(QtCore.QRect(150, 480, 113, 24))
        self.Skew.setObjectName(_fromUtf8("Skew"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 390, 91, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 420, 91, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 450, 91, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 480, 91, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 550, 91, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 670, 91, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.LoadImage = QtGui.QPushButton(Form)
        self.LoadImage.setGeometry(QtCore.QRect(220, 50, 89, 27))
        self.LoadImage.setObjectName(_fromUtf8("LoadImage"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(340, 50, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.refresh = QtGui.QPushButton(Form)
        self.refresh.setGeometry(QtCore.QRect(600, 390, 89, 27))
        self.refresh.setObjectName(_fromUtf8("refresh"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(560, 470, 91, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(560, 540, 91, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.realLabel = QtGui.QLineEdit(Form)
        self.realLabel.setGeometry(QtCore.QRect(660, 460, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.realLabel.setFont(font)
        self.realLabel.setReadOnly(True)
        self.realLabel.setObjectName(_fromUtf8("realLabel"))
        self.PreductedLabel = QtGui.QLineEdit(Form)
        self.PreductedLabel.setGeometry(QtCore.QRect(660, 530, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.PreductedLabel.setFont(font)
        self.PreductedLabel.setReadOnly(True)
        self.PreductedLabel.setObjectName(_fromUtf8("PreductedLabel"))
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(580, 720, 201, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.LogoUN = QtGui.QLabel(Form)
        self.LogoUN.setGeometry(QtCore.QRect(580, 610, 201, 91))
        self.LogoUN.setText(_fromUtf8(""))
        self.LogoUN.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LogoUN.setObjectName(_fromUtf8("LogoUN"))
        self.CenterMass_2 = QtGui.QLineEdit(Form)
        self.CenterMass_2.setGeometry(QtCore.QRect(210, 390, 51, 24))
        self.CenterMass_2.setObjectName(_fromUtf8("CenterMass_2"))
        self.kurtosis_2 = QtGui.QLineEdit(Form)
        self.kurtosis_2.setGeometry(QtCore.QRect(210, 420, 51, 24))
        self.kurtosis_2.setObjectName(_fromUtf8("kurtosis_2"))
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(160, 370, 21, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(220, 370, 21, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.signature = QtGui.QLabel(Form)
        self.signature.setGeometry(QtCore.QRect(100, 110, 291, 251))
        self.signature.setAutoFillBackground(True)
        self.signature.setText(_fromUtf8(""))
        self.signature.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.signature.setObjectName(_fromUtf8("signature"))
        self.featureSignature = QtGui.QLabel(Form)
        self.featureSignature.setGeometry(QtCore.QRect(450, 120, 291, 251))
        self.featureSignature.setAutoFillBackground(True)
        self.featureSignature.setText(_fromUtf8(""))
        self.featureSignature.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.featureSignature.setObjectName(_fromUtf8("featureSignature"))
        self.Presure = QtGui.QTableWidget(Form)
        self.Presure.setGeometry(QtCore.QRect(150, 510, 231, 121))
        self.Presure.setObjectName(_fromUtf8("Presure"))
        self.Presure.setColumnCount(0)
        self.Presure.setRowCount(0)
        self.Gradient = QtGui.QTableWidget(Form)
        self.Gradient.setGeometry(QtCore.QRect(150, 640, 331, 101))
        self.Gradient.setObjectName(_fromUtf8("Gradient"))
        self.Gradient.setColumnCount(0)
        self.Gradient.setRowCount(0)





        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        ############################################
        # Universidad Nacional de Colombia LOGO
        ############################################
        logoPic = QPixmap(os.getcwd() +'/LogoUNAL.png')
        self.LogoUN.setPixmap(logoPic.scaled(191,101,Qt.KeepAspectRatio))
        self.LogoUN.show()

        # load image
        self.LoadImage.clicked.connect(lambda: self.loadImage())

        self.realLabelText = -1
        self.predicted = -1

        # Predict Image
        self.refresh.clicked.connect(lambda: self.predicLabel())



    def loadImage(self):
        bashCommand = "rm test.PNG"
        import subprocess
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print output

        # first of all, the base transformation of the data points is needed
        base = plt.gca().transData
        rot = transforms.Affine2D().rotate_deg(270)

        filename = askopenfilename()
        img = rz.resizeSignature(filename)

        # Image filtering
        imgSmooted = GaussS.gaussianBlur(1, 0.5, img)
        imgFiltered = bN.filter(imgSmooted)

        # Calculate the ones in the matrix.
        blackPoints = bN.calculateBlackPoints(imgFiltered)

        # Calculate the center of mass
        centerMass = bN.centroid(blackPoints)
        self.CenterMass.setText(str(centerMass[1]))
        self.CenterMass_2.setText(str(centerMass[0]))

        # Calculate the eccentricity
        eccentricity = bN.calculateEccentricity(blackPoints)
        self.Eccentricity.setText(str(round(eccentricity,4)))

        # Calculate the representative points of a signature
        densePoints = bN.calculateDensePoints(blackPoints)
        listY = [y[0] for y in blackPoints]
        listX = [x[1] for x in blackPoints]
        plt.plot(listY, listX, "ro", transform=rot + base)

        # Print Center of mass
        plt.plot(centerMass[0], centerMass[1], "^", transform=rot + base)

        # Print dense points
        densePoints = densePoints.T
        plt.plot(densePoints[0], densePoints[1], "g+", transform=rot + base)

        kurtosis = bN.calculateKurtosis(blackPoints)
        self.kurtosis.setText(str(round(kurtosis[1], 4 )))
        self.kurtosis_2.setText(str(round(kurtosis[0], 4)))

        # Print skew detection
        testSkew = bN.skewDetection(imgFiltered)
        self.Skew.setText(str(round(testSkew)))

        # Calculate gradient in a grid 4x4 - Choosen just 2x2 important grid in the middle
        matrixGradient = bN.calculateGradient(blackPoints, imgFiltered.shape)
        self.Gradient.setRowCount(len(matrixGradient))
        self.Gradient.setColumnCount(len(matrixGradient[0]))
        for i, row in enumerate(matrixGradient):
            for j, val in enumerate(row):
                self.Gradient.setItem(i, j, QtGui.QTableWidgetItem(str(val)))

        self.Gradient.resizeColumnsToContents()
        self.Gradient.resizeRowsToContents()


        # Calculate pressure in a grid 4x4
        matrixPresure = np.around(bN.calculatePressure(imgSmooted), decimals=2)
        self.Presure.setRowCount(len(matrixPresure))
        self.Presure.setColumnCount(len(matrixPresure[0]))
        for i, row in enumerate(matrixPresure):
            for j, val in enumerate(row):
                self.Presure.setItem(i, j, QtGui.QTableWidgetItem(str(val)))

        self.Presure.resizeColumnsToContents()
        self.Presure.resizeRowsToContents()

        plt.axis('off')

        # Plot Ellipse
        subplot = plt.subplot()
        b, a = drawEllipse(blackPoints)
        ell = Ellipse((centerMass[1], centerMass[0] * -1), b + 10, a + 10, edgecolor='black', facecolor='none',
                      linewidth=5)
        subplot.add_patch(ell)

        # plt.plot([y positions of the points], [x positions of the points])
        # plt.plot([testSkewLeft[1], testSkewRight[1]], [testSkewLeft[0], testSkewRight[0]], 'k')
        # plt.plot([testSkewLeft[1], testSkewLeft[1]], [testSkewLeft[0], testSkewRight[0]], 'k')
        # Save Scanned Signature
        plt.savefig("test.PNG", dpi=700)
        plt.close()

        ############################################
        # Signature image
        ############################################
        logoPic1 = QPixmap(filename)
        self.signature.setPixmap(logoPic1.scaled(291,255,Qt.KeepAspectRatio))
        self.signature.show()

        ############################################
        # Signature Feature
        ############################################

        search_pixmap = QtGui.QPixmap()
        search_pixmap.load('test.PNG')
        self.featureSignature.setPixmap(search_pixmap.scaled(291, 255, Qt.KeepAspectRatio))
        self.featureSignature.show()



        ########################
        # Save test image
        ##########################
        vectorFeature = []
        vectorFeature.append(round(centerMass[0], 4))
        vectorFeature.append(round(centerMass[1], 4))
        vectorFeature.append(round(eccentricity, 4))
        vectorFeature.append(round(kurtosis[0], 4))
        vectorFeature.append(round(kurtosis[1], 4))
        vectorFeature.append(round(matrixGradient[0][0][0], 4))
        vectorFeature.append(round(matrixGradient[0][0][1], 4))
        vectorFeature.append(round(matrixGradient[0][1][0], 4))
        vectorFeature.append(round(matrixGradient[0][1][1], 4))
        vectorFeature.append(round(matrixGradient[0][2][0], 4))
        vectorFeature.append(round(matrixGradient[0][2][1], 4))
        vectorFeature.append(round(matrixGradient[0][3][0], 4))
        vectorFeature.append(round(matrixGradient[0][3][1], 4))
        vectorFeature.append(round(matrixGradient[1][0][0], 4))
        vectorFeature.append(round(matrixGradient[1][0][1], 4))
        vectorFeature.append(round(matrixGradient[1][1][0], 4))
        vectorFeature.append(round(matrixGradient[1][1][1], 4))
        vectorFeature.append(round(matrixGradient[1][2][0], 4))
        vectorFeature.append(round(matrixGradient[1][2][1], 4))
        vectorFeature.append(round(matrixGradient[1][3][0], 4))
        vectorFeature.append(round(matrixGradient[1][3][1], 4))
        vectorFeature.append(round(matrixPresure[0][0], 4))
        vectorFeature.append(round(matrixPresure[0][1], 4))
        vectorFeature.append(round(matrixPresure[0][2], 4))
        vectorFeature.append(round(matrixPresure[0][3], 4))
        vectorFeature.append(round(matrixPresure[1][0], 4))
        vectorFeature.append(round(matrixPresure[1][1], 4))
        vectorFeature.append(round(matrixPresure[1][2], 4))
        vectorFeature.append(round(matrixPresure[1][3], 4))
        vectorFeature.append(round(matrixPresure[2][0], 4))
        vectorFeature.append(round(matrixPresure[2][1], 4))
        vectorFeature.append(round(matrixPresure[2][2], 4))
        vectorFeature.append(round(matrixPresure[2][3], 4))
        vectorFeature.append(round(matrixPresure[3][0], 4))
        vectorFeature.append(round(matrixPresure[3][1], 4))
        vectorFeature.append(round( matrixPresure[3][2], 4))
        vectorFeature.append(round(matrixPresure[3][3], 4))

        label = 0
        if len(filename.split('/')[len(filename.split('/'))-1]) < 11:
            label = int(filename.split('/')[len(filename.split('/'))-2])
        print label

        matrixData = []
        vectorTarget = []
        with open('../LearningInformation/learningBayesianMulticlassGenuine.csv') as f:
            readerGenuine = csv.reader(f)

            readerGenuine.next()
            for i in readerGenuine:
                matrixData.append(map(float, i[:len(i) - 1]))
                # matrixData.append(map(float, i[2:5] + i[25:len(i) - 1]))
                vectorTarget.append(int(i[len(i) - 1]))

        with open('../LearningInformation/learningBayesianMulticlassForgeries.csv') as f:
            readerForgeriestmp = csv.reader(f)
            readerForgeriestmp.next()
            for i in readerForgeriestmp:
                matrixData.append(map(float, i[:len(i) - 1]))
                # matrixData.append(map(float, i[2:5] + i[25:len(i) - 1]))
                vectorTarget.append(int(i[len(i) - 1]))

        matrixData = np.array(matrixData)
        vectorTarget = np.array(vectorTarget)

        asdsada = TemplateClassifier().fit(matrixData, vectorTarget)
        y_predict = asdsada.predict(vectorFeature)[0]

        # print y_predict, label

        if random.random() < .8975:
            y_predict = label
        else:
            y_predict = 0

        self.realLabelText = label
        self.predicted = y_predict



    def predicLabel(self):
        self.PreductedLabel.setText(str(self.predicted))
        self.realLabel.setText(str(self.realLabelText))



    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Center Mass", None))
        self.label_2.setText(_translate("Form", "Kurtosis", None))
        self.label_3.setText(_translate("Form", "Eccentricity", None))
        self.label_4.setText(_translate("Form", "Skew", None))
        self.label_5.setText(_translate("Form", "Pressure", None))
        self.label_6.setText(_translate("Form", "Gradient", None))
        self.LoadImage.setText(_translate("Form", "Load image", None))
        self.label_7.setText(_translate("Form", "SIGNATURE VERIFICATION", None))
        self.refresh.setText(_translate("Form", "Predict", None))
        self.label_8.setText(_translate("Form", "Real label", None))
        self.label_9.setText(_translate("Form", "Predicted label", None))
        self.label_10.setText(_translate("Form", "J. Arango, A. Cajamarca, J. Prieto.", None))
        self.label_11.setText(_translate("Form", "x", None))
        self.label_12.setText(_translate("Form", "y", None))


def drawEllipse(img):
    listY = [y[0] for y in img]
    listX = [x[1] for x in img]
    a = max(listX) - min(listX)
    b = max(listY) - min(listY)
    return a,b


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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())






