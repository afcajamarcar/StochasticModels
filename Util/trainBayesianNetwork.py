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
          "Genuine"

    '''
    # Header of CSV file
    print "CenterX,CenterY,Eccentricity," \
          "KurtosisX,KurtosisY,AngleSig," \
          "GrdGrid1_x,GrdGrid1_y,GrdGrid2_x,GrdGrid2_y,GrdGrid3_x,GrdGrid3_y,GrdGrid4_x,GrdGrid4_y,GrdGrid5_x,GrdGrid5_y," \
          "GrdGrid1_6,GrdGrid6_y,GrdGrid7_x,GrdGrid7_y,GrdGrid8_x,GrdGrid8_y,GrdGrid9_x,GrdGrid9_y,GrdGrid10_x,GrdGrid10_y," \
          "GrdGrid1_11,GrdGrid11_y,GrdGrid12_x,GrdGrid12_y,GrdGrid13_x,GrdGrid13_y,GrdGrid14_x,GrdGrid14_y,GrdGrid15_x,GrdGrid15_y," \
          "PressGrid1,PressGrid2,PressGrid3,PressGrid4,PressGrid5,PressGrid6,PressGrid7,PressGrid8," \
          "PressGrid9,PressGrid10,PressGrid11,PressGrid12,PressGrid13,PressGrid14,PressGrid15,PressGrid16,Genuine"
    '''
    #################################################
    # Genuine Files
    #################################################
    allFiles = next(os.walk("../Questioned(1287)"))[1]

    for files in allFiles:
        folderFiles = next(os.walk("../Questioned(1287)/"+files))[2]
        for signature in folderFiles:
            isGenuine = 1
            if len(signature) > 10:
                isGenuine = 0

            img = rz.resizeSignature("../Questioned(1287)/" + files + "/" + signature)
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
            densePoints = bN.calculateDensePoints(blackPoints)

            # Calculate Kurtosis of blackpoints in signature
            kurtosis = bN.calculateKurtosis(blackPoints)

            # Print skew detection
            testSkew = bN.skewDetection(imgFiltered)

            # Calculate gradient in a grid 4x4 - Choosen just 2x2 important grid in the middle
            matrixGradient = bN.calculateGradient(blackPoints, imgFiltered.shape)

            # Calculate pressure in a grid 4x4
            matrixPresure = bN.calculatePressure(imgSmooted)

            print str(round(centerMass[0],4)) + "," + str(round(centerMass[1],4)) + "," + str(round(eccentricity,4)) + "," +\
                  str(round(kurtosis[0],4)) + "," + str(round(kurtosis[1],4)) + "," + \
                  str(round(matrixGradient[0][0][0],4)) + "," + str(round(matrixGradient[0][0][1],4)) + "," + str(round(
                matrixGradient[0][1][0],4)) + "," + str(round(matrixGradient[0][1][1],4)) + "," + \
                  str(round(matrixGradient[0][2][0],4)) + "," + str(round(matrixGradient[0][2][1],4)) + "," + str(round(
                matrixGradient[0][3][0],4)) + "," + str(round(matrixGradient[0][3][1],4)) + "," + \
                  str(round(matrixGradient[0][4][0],4)) + "," + str(round(matrixGradient[0][4][1],4)) + "," + \
                  str(round(matrixGradient[1][0][0],4)) + "," + str(round(matrixGradient[1][0][1],4)) + "," + str(round(
                matrixGradient[1][1][0],4)) + "," + str(round(matrixGradient[1][1][1],4)) + "," + \
                  str(round(matrixGradient[1][2][0],4)) + "," + str(round(matrixGradient[1][2][1],4)) + "," + str(round(
                matrixGradient[1][3][0],4)) + "," + str(round(matrixGradient[1][3][1],4)) + "," + \
                  str(round(matrixGradient[1][4][0],4)) + "," + str(round(matrixGradient[1][4][1],4)) + "," + \
                  str(round(matrixPresure[0][0],4)) + "," + str(round(matrixPresure[0][1],4)) + "," + str(round(matrixPresure[0][2],4)) + "," + \
                  str(round(matrixPresure[0][3],4)) + "," + \
                  str(round(matrixPresure[1][0],4)) + "," + str(round(matrixPresure[1][1],4)) + "," + str(round(
                matrixPresure[1][2],4)) + "," + str(round(
                matrixPresure[1][3],4)) + "," + \
                  str(round(matrixPresure[2][0],4)) + "," + str(round(matrixPresure[2][1],4)) + "," + str(round(
                matrixPresure[2][2],4)) + "," + str(round(
                matrixPresure[2][3],4)) + "," + \
                  str(round(matrixPresure[3][0],4)) + "," + str(round(matrixPresure[3][1],4)) + "," + str(round(
                matrixPresure[3][2],4)) + "," + str(round(
                matrixPresure[3][3],4)) + "," + \
                  str(isGenuine)

            '''
            print str(round(centerMass[0],4)) + "," + str(round(centerMass[1],4)) + "," + str(round(eccentricity,4)) + "," +\
                  str(round(kurtosis[0],4)) + "," + str(round(kurtosis[1],4)) + "," + str(round(testSkew,4)) + "," + \
                  str(round(densePoints[0][0],4)) + "," + str(round(densePoints[0][1],4)) + "," + str(round(densePoints[1][0],4)) + "," + str(round(
                densePoints[1][1],4)) + "," + str(round(densePoints[2][0],4)) + "," + str(round(densePoints[2][1],4)) + "," + \
                  str(round(densePoints[3][0],4)) + "," + str(round(densePoints[3][1],4)) + "," + str(round(densePoints[4][0],4)) + "," + str(round(
                densePoints[4][1],4)) + "," + str(round(densePoints[5][0],4)) + "," + str(round(densePoints[5][1],4)) + "," + \
                  str(round(densePoints[6][0],4)) + "," + str(round(densePoints[6][1],4)) + "," + str(round(densePoints[7][0],4)) + "," + str(round(
                densePoints[7][1],4)) + "," + str(round(densePoints[8][0],4)) + "," + str(round(densePoints[8][1],4)) + "," + \
                  str(round(densePoints[9][0],4)) + "," + str(round(densePoints[9][1],4)) + "," + \
                  str(round(matrixGradient[0][0][0],4)) + "," + str(round(matrixGradient[0][0][1],4)) + "," + str(round(
                matrixGradient[0][1][0],4)) + "," + str(round(matrixGradient[0][1][1],4)) + "," + \
                  str(round(matrixGradient[0][2][0],4)) + "," + str(round(matrixGradient[0][2][1],4)) + "," + str(round(
                matrixGradient[0][3][0],4)) + "," + str(round(matrixGradient[0][3][1],4)) + "," + \
                  str(round(matrixGradient[0][4][0],4)) + "," + str(round(matrixGradient[0][4][1],4)) + "," + \
                  str(round(matrixGradient[1][0][0],4)) + "," + str(round(matrixGradient[1][0][1],4)) + "," + str(round(
                matrixGradient[1][1][0],4)) + "," + str(round(matrixGradient[1][1][1],4)) + "," + \
                  str(round(matrixGradient[1][2][0],4)) + "," + str(round(matrixGradient[1][2][1],4)) + "," + str(round(
                matrixGradient[1][3][0],4)) + "," + str(round(matrixGradient[1][3][1],4)) + "," + \
                  str(round(matrixGradient[1][4][0],4)) + "," + str(round(matrixGradient[1][4][1],4)) + "," + \
                  str(round(matrixGradient[2][0][0],4)) + "," + str(round(matrixGradient[2][0][1],4)) + "," + str(round(
                matrixGradient[2][1][0],4)) + "," + str(round(matrixGradient[2][1][1],4)) + "," + \
                  str(round(matrixGradient[2][2][0],4)) + "," + str(round(matrixGradient[2][2][1],4)) + "," + str(round(
                matrixGradient[2][3][0],4)) + "," + str(round(matrixGradient[2][3][1],4)) + "," + \
                  str(round(matrixGradient[2][4][0],4)) + "," + str(round(matrixGradient[2][4][1],4)) + "," + \
                  str(round(matrixPresure[0][0],4)) + "," + str(round(matrixPresure[0][1],4)) + "," + str(round(matrixPresure[0][2],4)) + "," + \
                  str(round(matrixPresure[0][3],4)) + "," + str(round(matrixPresure[0][4],4)) + "," + \
                  str(round(matrixPresure[1][0],4)) + "," + str(round(matrixPresure[1][1],4)) + "," + str(round(
                matrixPresure[1][2],4)) + "," + str(round(
                matrixPresure[1][3],4)) + "," + str(round(matrixPresure[1][4],4)) + "," + \
                  str(round(matrixPresure[2][0],4)) + "," + str(round(matrixPresure[2][1],4)) + "," + str(round(
                matrixPresure[2][2],4)) + "," + str(round(
                matrixPresure[2][3],4)) + "," + str(round(matrixPresure[2][4],4)) + "," + \
                  str(round(matrixPresure[3][0],4)) + "," + str(round(matrixPresure[3][1],4)) + "," + str(round(
                matrixPresure[3][2],4)) + "," + str(round(
                matrixPresure[3][3],4)) + "," + str(round(matrixPresure[3][4],4)) + "," + \
                  str(round(matrixPresure[4][0],4)) + "," + str(round(matrixPresure[4][1],4)) + "," + str(round(
                matrixPresure[4][2],4)) + "," + str(round(
                matrixPresure[4][3],4)) + "," + str(round(matrixPresure[4][4],4)) + "," + \
                  str(isGenuine)
            '''

# '''
#
#     '''
#     # filename = askopenfilename()
#     img = rz.resizeSignature("../TrainingSet/Offline Genuine/" + genuineFiles[10])
#
#     # Image filtering
#     imgSmooted = GaussS.gaussianBlur(1, 0.55, img)
#     imgFiltered = bN.filter(imgSmooted)
#
#     # Calculate the ones in the matrix.
#     blackPoints = bN.calculateBlackPoints(imgFiltered)
#
#     # Calculate the center of mass
#     centerMass = bN.centroid(blackPoints)
#
#     # Calculate the eccentricity
#     eccentricity = bN.calculateEccentricity(blackPoints)
#
#     # Calculate the representative points of a signature
#     densePoints = bN.calculateDensePoints(blackPoints)
#     '''
#
#     for file in genuineFiles:
#
#         # filename = askopenfilename()
#         img = rz.resizeSignature("../TrainingSet/Offline Genuine,4)/"+file)
#
#         # Image filtering
#         imgSmooted = GaussS.gaussianBlur(1, 0.5, img)
#         imgFiltered = bN.filter(imgSmooted)
#
#         # Calculate the ones in the matrix.
#         blackPoints = bN.calculateBlackPoints(imgFiltered)
#
#         # Calculate the center of mass
#         centerMass = bN.centroid(blackPoints)
#
#         # Calculate the eccentricity
#         eccentricity = bN.calculateEccentricity(blackPoints)
#
#         # Calculate the representative points of a signature
#         densePoints = bN.calculateDensePoints(blackPoints)
#
#         # Calculate Kurtosis of blackpoints in signature
#         kurtosis = bN.calculateKurtosis(blackPoints)
#
#         # Print skew detection
#         testSkew = bN.skewDetection(imgFiltered)
#
#         # Calculate gradient in a grid 4x4 - Choosen just 2x2 important grid in the middle
#         matrixGradient = bN.calculateGradient(blackPoints, imgFiltered.shape)
#
#         # Calculate pressure in a grid 4x4
#         matrixPresure = bN.calculatePressure(imgSmooted)
#
#         print str(round(centerMass[0],4)) + "," + str(round(centerMass[1],4)) + "," + str(round(eccentricity,4)) + "," + \
#               str(round(kurtosis[0],4)) + "," + str(round(kurtosis[1],4)) + "," + str(round(testSkew,4)) + "," + \
#               str(round(densePoints[0][0],4)) + "," + str(round(densePoints[0][1],4)) + "," + str(round(densePoints[1][0],4)) + "," + str(round(
#             densePoints[1][1],4)) + "," + str(round(densePoints[2][0],4)) + "," + str(round(densePoints[2][1],4)) + "," + \
#               str(round(densePoints[3][0],4)) + "," + str(round(densePoints[3][1],4)) + "," + str(round(densePoints[4][0],4)) + "," + str(round(
#             densePoints[4][1],4)) + "," + str(round(densePoints[5][0],4)) + "," + str(round(densePoints[5][1],4)) + "," + \
#               str(round(densePoints[6][0],4)) + "," + str(round(densePoints[6][1],4)) + "," + str(round(densePoints[7][0],4)) + "," + str(round(
#             densePoints[7][1],4)) + "," + str(round(densePoints[8][0],4)) + "," + str(round(densePoints[8][1],4)) + "," + \
#               str(round(densePoints[9][0],4)) + "," + str(round(densePoints[9][1],4)) + "," + \
#             str(round(matrixGradient[0][0][0],4)) + "," + str(round(matrixGradient[0][0][1],4)) + "," + str(round(
#             matrixGradient[0][1][0],4)) + "," + str(round(matrixGradient[0][1][1],4)) + "," + \
#               str(round(matrixGradient[0][2][0],4)) + "," + str(round(matrixGradient[0][2][1],4)) + "," + str(round(
#             matrixGradient[0][3][0],4)) + "," + str(round(matrixGradient[0][3][1],4)) + "," + \
#               str(round(matrixGradient[0][4][0],4)) + "," + str(round(matrixGradient[0][4][1],4)) + "," + \
#               str(round(matrixGradient[1][0][0],4)) + "," + str(round(matrixGradient[1][0][1],4)) + "," + str(round(
#             matrixGradient[1][1][0],4)) + "," + str(round(matrixGradient[1][1][1],4)) + "," + \
#               str(round(matrixGradient[1][2][0],4)) + "," + str(round(matrixGradient[1][2][1],4)) + "," + str(round(
#             matrixGradient[1][3][0],4)) + "," + str(round(matrixGradient[1][3][1],4)) + "," + \
#               str(round(matrixGradient[1][4][0],4)) + "," + str(round(matrixGradient[1][4][1],4)) + "," + \
#               str(round(matrixGradient[2][0][0],4)) + "," + str(round(matrixGradient[2][0][1],4)) + "," + str(round(
#             matrixGradient[2][1][0],4)) + "," + str(round(matrixGradient[2][1][1],4)) + "," + \
#               str(round(matrixGradient[2][2][0],4)) + "," + str(round(matrixGradient[2][2][1],4)) + "," + str(round(
#             matrixGradient[2][3][0],4)) + "," + str(round(matrixGradient[2][3][1],4)) + "," + \
#               str(round(matrixGradient[2][4][0],4)) + "," + str(round(matrixGradient[2][4][1],4)) + "," + \
#               str(round(matrixPresure[0][0],4)) + "," + str(round(matrixPresure[0][1],4)) + "," + str(round(matrixPresure[0][2],4)) + "," + str(round(
#             matrixPresure[0][3],4)) + "," + str(round(matrixPresure[0][4],4)) + "," + \
#               str(round(matrixPresure[1][0],4)) + "," + str(round(matrixPresure[1][1],4)) + "," + str(round(matrixPresure[1][2],4)) + "," + str(round(
#             matrixPresure[1][3],4)) + "," + str(round(matrixPresure[1][4],4)) + "," + \
#               str(round(matrixPresure[2][0],4)) + "," + str(round(matrixPresure[2][1],4)) + "," + str(round(matrixPresure[2][2],4)) + "," + str(round(
#             matrixPresure[2][3],4)) + "," + str(round(matrixPresure[2][4],4)) + "," + \
#               str(round(matrixPresure[3][0],4)) + "," + str(round(matrixPresure[3][1],4)) + "," + str(round(matrixPresure[3][2],4)) + "," + str(round(
#             matrixPresure[3][3],4)) + "," + str(round(matrixPresure[3][4],4)) + "," + \
#               str(round(matrixPresure[4][0],4)) + "," + str(round(matrixPresure[4][1],4)) + "," + str(round(matrixPresure[4][2],4)) + "," + str(round(
#             matrixPresure[4][3],4)) + "," + str(round(matrixPresure[4][4],4)) + "," + \
#               str(round(1)
#
#         '''
#                 str(round(densePoints[0][0],4)) + "," + str(round(densePoints[0][1],4)) + "," + str(round(densePoints[1][0],4)) + "," + str(round(densePoints[1][1],4)) + "," + str(round(densePoints[2][0],4)) + "," + str(round(densePoints[2][1],4)) + "," + \
#                 str(round(densePoints[3][0],4)) + "," + str(round(densePoints[3][1],4)) + "," + str(round(densePoints[4][0],4)) + "," + str(round(densePoints[4][1],4)) + "," + str(round(densePoints[5][0],4)) + "," + str(round(densePoints[5][1],4)) + "," + \
#                 str(round(densePoints[6][0],4)) + "," + str(round(densePoints[6][1],4)) + "," + str(round(densePoints[7][0],4)) + "," + str(round(densePoints[7][1],4)) + "," + str(round(densePoints[8][0],4)) + "," + str(round(densePoints[8][1],4)) + "," + \
#                 str(round(densePoints[9][0],4)) + "," + str(round(densePoints[9][1],4)) + "," + str(round(densePoints[10][0],4)) + "," + str(round(densePoints[10][1],4)) + "," + str(round(densePoints[11][0],4)) + "," + str(round(densePoints[11][1],4)) + "," + \
#                 str(round(densePoints[12][0],4)) + "," + str(round(densePoints[12][1],4)) + "," + str(round(densePoints[13][0],4)) + "," + str(round(densePoints[14][1],4)) + "," + str(round(densePoints[14][0],4)) + "," + str(round(densePoints[14][1],4)) + "," + \
#                 str(round(densePoints[15][0],4)) + "," + str(round(densePoints[15][1],4)) + "," + str(round(densePoints[16][0],4)) + "," + str(round(densePoints[16][1],4)) + "," + str(round(densePoints[17][0],4)) + "," + str(round(densePoints[17][1],4)) + "," + \
#                 str(round(densePoints[18][0],4)) + "," + str(round(densePoints[18][1],4)) + "," + str(round(densePoints[19][0],4)) + "," + str(round(densePoints[19][1],4)) + ",",4)  + \
#                 str(round(densePoints[20][0],4)) + "," + str(round(densePoints[20][1],4)) + "," + str(round(densePoints[21][0],4)) + "," + str(round(
#                 densePoints[21][1],4)) + "," + \
#                 str(round(densePoints[22][0],4)) + "," + str(round(densePoints[22][1],4)) + "," + str(round(densePoints[23][0],4)) + "," + str(round(
#                 densePoints[23][1],4)) + "," + \
#                 str(round(densePoints[24][0],4)) + "," + str(round(densePoints[24][1],4)) + "," + str(round(densePoints[25][0],4)) + "," + str(round(
#                 densePoints[25][1],4)) + "," + \
#                 str(round(densePoints[26][0],4)) + "," + str(round(densePoints[26][1],4)) + "," + str(round(densePoints[27][0],4)) + "," + str(round(
#                 densePoints[27][1],4)) + "," + \
#                 str(round(densePoints[28][0],4)) + "," + str(round(densePoints[28][1],4)) + "," + str(round(densePoints[29][0],4)) + "," + str(round(
#                 densePoints[29][1],4)) + "," + \
#                 '''
#
#     ############################################################
#     # Forgeing Files
#     ############################################################
#     forgeingFiles = next(os.walk("../TrainingSet/Offline Forgeries"))[2]
#
#     for file in forgeingFiles:
#         # filename = askopenfilename()
#         img = rz.resizeSignature("../TrainingSet/Offline Forgeries/" + file)
#
#         # Image filtering
#         imgSmooted = GaussS.gaussianBlur(1, 0.5, img)
#         imgFiltered = bN.filter(imgSmooted)
#
#         # Calculate the ones in the matrix.
#         blackPoints = bN.calculateBlackPoints(imgFiltered)
#
#         # Calculate the center of mass
#         centerMass = bN.centroid(blackPoints)
#
#         # Calculate the eccentricity
#         eccentricity = bN.calculateEccentricity(blackPoints)
#
#         # Calculate the representative points of a signature
#         densePoints = bN.calculateDensePoints(blackPoints)
#
#         # Calculate Kurtosis of blackpoints in signature
#         kurtosis = bN.calculateKurtosis(blackPoints)
#
#         # Print skew detection
#         testSkew = bN.skewDetection(imgFiltered)
#
#         # Calculate gradient in a grid 4x4 - Choosen just 2x2 important grid in the middle
#         matrixGradient = bN.calculateGradient(blackPoints, imgFiltered.shape)
#
#         # Calculate pressure in a grid 4x4
#         matrixPresure = bN.calculatePressure(imgSmooted)
#
#         print str(round(centerMass[0],4)) + "," + str(round(centerMass[1],4)) + "," + str(round(eccentricity,4)) + "," + \
#               str(round(kurtosis[0],4)) + "," + str(round(kurtosis[1],4)) + "," + str(round(testSkew,4)) + "," + \
#               str(round(densePoints[0][0],4)) + "," + str(round(densePoints[0][1],4)) + "," + str(round(densePoints[1][0],4)) + "," + str(round(
#             densePoints[1][1],4)) + "," + str(round(densePoints[2][0],4)) + "," + str(round(densePoints[2][1],4)) + "," + \
#               str(round(densePoints[3][0],4)) + "," + str(round(densePoints[3][1],4)) + "," + str(round(densePoints[4][0],4)) + "," + str(round(
#             densePoints[4][1],4)) + "," + str(round(densePoints[5][0],4)) + "," + str(round(densePoints[5][1],4)) + "," + \
#               str(round(densePoints[6][0],4)) + "," + str(round(densePoints[6][1],4)) + "," + str(round(densePoints[7][0],4)) + "," + str(round(
#             densePoints[7][1],4)) + "," + str(round(densePoints[8][0],4)) + "," + str(round(densePoints[8][1],4)) + "," + \
#               str(round(densePoints[9][0],4)) + "," + str(round(densePoints[9][1],4)) + "," + \
#               str(round(matrixGradient[0][0][0],4)) + "," + str(round(matrixGradient[0][0][1],4)) + "," + str(round(
#             matrixGradient[0][1][0],4)) + "," + str(round(matrixGradient[0][1][1],4)) + "," + \
#               str(round(matrixGradient[0][2][0],4)) + "," + str(round(matrixGradient[0][2][1],4)) + "," + str(round(
#             matrixGradient[0][3][0],4)) + "," + str(round(matrixGradient[0][3][1],4)) + "," + \
#               str(round(matrixGradient[0][4][0],4)) + "," + str(round(matrixGradient[0][4][1],4)) + "," + \
#               str(round(matrixGradient[1][0][0],4)) + "," + str(round(matrixGradient[1][0][1],4)) + "," + str(round(
#             matrixGradient[1][1][0],4)) + "," + str(round(matrixGradient[1][1][1],4)) + "," + \
#               str(round(matrixGradient[1][2][0],4)) + "," + str(round(matrixGradient[1][2][1],4)) + "," + str(round(
#             matrixGradient[1][3][0],4)) + "," + str(round(matrixGradient[1][3][1],4)) + "," + \
#               str(round(matrixGradient[1][4][0],4)) + "," + str(round(matrixGradient[1][4][1],4)) + "," + \
#               str(round(matrixGradient[2][0][0],4)) + "," + str(round(matrixGradient[2][0][1],4)) + "," + str(round(
#             matrixGradient[2][1][0],4)) + "," + str(round(matrixGradient[2][1][1],4)) + "," + \
#               str(round(matrixGradient[2][2][0],4)) + "," + str(round(matrixGradient[2][2][1],4)) + "," + str(round(
#             matrixGradient[2][3][0],4)) + "," + str(round(matrixGradient[2][3][1],4)) + "," + \
#               str(round(matrixGradient[2][4][0],4)) + "," + str(round(matrixGradient[2][4][1],4)) + "," + \
#               str(round(matrixPresure[0][0],4)) + "," + str(round(matrixPresure[0][1],4)) + "," + str(round(matrixPresure[0][2],4)) + "," + str(round(
#             matrixPresure[0][3],4)) + "," + str(round(matrixPresure[0][4],4)) + "," + \
#               str(round(matrixPresure[1][0],4)) + "," + str(round(matrixPresure[1][1],4)) + "," + str(round(matrixPresure[1][2],4)) + "," + str(round(
#             matrixPresure[1][3],4)) + "," + str(round(matrixPresure[1][4],4)) + "," +\
#               str(round(matrixPresure[2][0],4)) + "," + str(round(matrixPresure[2][1],4)) + "," + str(round(matrixPresure[2][2],4)) + "," + str(round(
#             matrixPresure[2][3],4)) + "," +  str(round(matrixPresure[2][4],4)) + "," +\
#               str(round(matrixPresure[3][0],4)) + "," + str(round(matrixPresure[3][1],4)) + "," + str(round(matrixPresure[3][2],4)) + "," + str(round(
#             matrixPresure[3][3],4)) + "," + str(round(matrixPresure[3][4],4)) + "," + \
#               str(round(matrixPresure[4][0],4)) + "," + str(round(matrixPresure[4][1],4)) + "," + str(round(matrixPresure[4][2],4)) + "," + str(round(
#             matrixPresure[4][3],4)) + "," + str(round(matrixPresure[4][4],4)) + "," + \
#         str(round(0)
#
#         '''
#               str(round(densePoints[0][0],4)) + "," + str(round(densePoints[0][1],4)) + "," + str(round(densePoints[1][0],4)) + "," + str(round(
#             densePoints[1][1],4)) + "," + str(round(densePoints[2][0],4)) + "," + str(round(densePoints[2][1],4)) + "," + \
#               str(round(densePoints[3][0],4)) + "," + str(round(densePoints[3][1],4)) + "," + str(round(densePoints[4][0],4)) + "," + str(round(
#             densePoints[4][1],4)) + "," + str(round(densePoints[5][0],4)) + "," + str(round(densePoints[5][1],4)) + "," + \
#               str(round(densePoints[6][0],4)) + "," + str(round(densePoints[6][1],4)) + "," + str(round(densePoints[7][0],4)) + "," + str(round(
#             densePoints[7][1],4)) + "," + str(round(densePoints[8][0],4)) + "," + str(round(densePoints[8][1],4)) + "," + \
#               str(round(densePoints[9][0],4)) + "," + str(round(densePoints[9][1],4)) + "," + str(round(densePoints[10][0],4)) + "," + str(round(
#             densePoints[10][1],4)) + "," + str(round(densePoints[11][0],4)) + "," + str(round(densePoints[11][1],4)) + "," + \
#               str(round(densePoints[12][0],4)) + "," + str(round(densePoints[12][1],4)) + "," + str(round(densePoints[13][0],4)) + "," + str(round(
#             densePoints[14][1],4)) + "," + str(round(densePoints[14][0],4)) + "," + str(round(densePoints[14][1],4)) + "," + \
#               str(round(densePoints[15][0],4)) + "," + str(round(densePoints[15][1],4)) + "," + str(round(densePoints[16][0],4)) + "," + str(round(
#             densePoints[16][1],4)) + "," + str(round(densePoints[17][0],4)) + "," + str(round(densePoints[17][1],4)) + "," + \
#               str(round(densePoints[18][0],4)) + "," + str(round(densePoints[18][1],4)) + "," + str(round(densePoints[19][0],4)) + "," + str(round(
#             densePoints[19][1],4)) + "," + \
#               str(round(densePoints[20][0],4)) + "," + str(round(densePoints[20][1],4)) + "," + str(round(densePoints[21][0],4)) + "," + str(round(
#             densePoints[21][1],4)) + "," + \
#               str(round(densePoints[22][0],4)) + "," + str(round(densePoints[22][1],4)) + "," + str(round(densePoints[23][0],4)) + "," + str(round(
#             densePoints[23][1],4)) + "," + \
#               str(round(densePoints[24][0],4)) + "," + str(round(densePoints[24][1],4)) + "," + str(round(densePoints[25][0],4)) + "," + str(round(
#             densePoints[25][1],4)) + "," + \
#               str(round(densePoints[26][0],4)) + "," + str(round(densePoints[26][1],4)) + "," + str(round(densePoints[27][0],4)) + "," + str(round(
#             densePoints[27][1],4)) + "," + \
#               str(round(densePoints[28][0],4)) + "," + str(round(densePoints[28][1],4)) + "," + str(round(densePoints[29][0],4)) + "," + str(round(
#             densePoints[29][1],4)) + "," + \
#         '''
#

