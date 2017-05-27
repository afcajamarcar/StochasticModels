########################################
# Universidad Nacional de Colombia
# Sthochastic Models
########################################
# Authors
# Jeisson Andres Prieto Velandia
# Andres Felipe Cajamarca Rojas
# Juan Felipe Arango Manrique
########################################


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
    allFiles = next(os.walk("../TrainingSet/Offline Forgeries"))[1]

    dataToTrain = {}

    for files in allFiles[:20]:
        folderFiles = next(os.walk("../TrainingSet/Offline Forgeries/" + files))[2]

        for signature in folderFiles:

            img = rz.resizeSignature("../TrainingSet/Offline Forgeries/" + files + "/" + signature)
            # Image filtering
            imgSmooted = GaussS.gaussianBlur(1, 0.55, img)
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
                  str(int(files))