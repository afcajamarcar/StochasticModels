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
    print "CenterX,CenterY,Eccentricity," \
          "Km_x1,Km_y1,Km_x2,Km_y2,Km_x3,Km_y3,Km_x4,Km_y4,Km_x5,Km_y5,Km_x6,Km_y6,Km_x7,Km_y7," \
          "Km_x8,Km_y8,Km_x9,Km_y9,Km_x10,Km_y10," \
          "KurtosisX,KurtosisY,AngleSig," \
          "GrdGrid1_x,GrdGrid1_y,GrdGrid2_x,GrdGrid2_y,GrdGrid3_x,GrdGrid3_y,GrdGrid4_x,GrdGrid4_y," \
          "GrdGrid1_5,GrdGrid5_y,GrdGrid6_x,GrdGrid6_y,GrdGrid7_x,GrdGrid7_y,GrdGrid8_x,GrdGrid8_y," \
          "PressGrid1,PressGrid2,PressGrid3,PressGrid4,PressGrid5,PressGrid6,PressGrid7,PressGrid8," \
          "PressGrid9,PressGrid10,PressGrid11,PressGrid12,PressGrid13,PressGrid14,PressGrid15,PressGrid16," \
          "PressGrid17,PressGrid18,PressGrid19,PressGrid19,PressGrid20,PressGrid21,PressGrid22,PressGrid23,PressGrid24,Genuine"

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
            if len(signature) > 10:
                img = rz.resizeSignature("../Questioned(1287)/"+ files +"/"+ signature)

                # Image filtering
                imgSmooted = GaussS.gaussianBlur(1, 0.55, img)
                imgFiltered = bN.filter(imgSmooted)

                # Calculate the ones in the matrix.
                blackPoints = bN.calculateBlackPoints(imgFiltered)

                # Calculate the center of mass
                centerMass = bN.centroid(blackPoints)

                # Calculate the eccentricity
                #eccentricity = bN.calculateEccentricity(blackPoints)

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

                print str(centerMass[0]) + "," + str(centerMass[1]) + "," + \
                      str(kurtosis[0]) + "," + str(kurtosis[1]) + "," + str(testSkew) + "," + \
                      str(densePoints[0][0]) + "," + str(densePoints[0][1]) + "," + str(densePoints[1][0]) + "," + str(
                    densePoints[1][1]) + "," + str(densePoints[2][0]) + "," + str(densePoints[2][1]) + "," + \
                      str(densePoints[3][0]) + "," + str(densePoints[3][1]) + "," + str(densePoints[4][0]) + "," + str(
                    densePoints[4][1]) + "," + str(densePoints[5][0]) + "," + str(densePoints[5][1]) + "," + \
                      str(densePoints[6][0]) + "," + str(densePoints[6][1]) + "," + str(densePoints[7][0]) + "," + str(
                    densePoints[7][1]) + "," + str(densePoints[8][0]) + "," + str(densePoints[8][1]) + "," + \
                      str(densePoints[9][0]) + "," + str(densePoints[9][1]) + "," + \
                      str(matrixGradient[0][0][0]) + "," + str(matrixGradient[0][0][1]) + "," + str(
                    matrixGradient[0][1][0]) + "," + str(matrixGradient[0][1][1]) + "," + \
                      str(matrixGradient[0][2][0]) + "," + str(matrixGradient[0][2][1]) + "," + str(
                    matrixGradient[0][3][0]) + "," + str(matrixGradient[0][3][1]) + "," + \
                      str(matrixGradient[0][4][0]) + "," + str(matrixGradient[0][4][1]) + "," + \
                      str(matrixGradient[1][0][0]) + "," + str(matrixGradient[1][0][1]) + "," + str(
                    matrixGradient[1][1][0]) + "," + str(matrixGradient[1][1][1]) + "," + \
                      str(matrixGradient[1][2][0]) + "," + str(matrixGradient[1][2][1]) + "," + str(
                    matrixGradient[1][3][0]) + "," + str(matrixGradient[1][3][1]) + "," + \
                      str(matrixGradient[1][4][0]) + "," + str(matrixGradient[1][4][1]) + "," + \
                      str(matrixGradient[2][0][0]) + "," + str(matrixGradient[2][0][1]) + "," + str(
                    matrixGradient[2][1][0]) + "," + str(matrixGradient[2][1][1]) + "," + \
                      str(matrixGradient[2][2][0]) + "," + str(matrixGradient[2][2][1]) + "," + str(
                    matrixGradient[2][3][0]) + "," + str(matrixGradient[2][3][1]) + "," + \
                      str(matrixGradient[2][4][0]) + "," + str(matrixGradient[2][4][1]) + "," + \
                      str(matrixPresure[0][0]) + "," + str(matrixPresure[0][1]) + "," + str(matrixPresure[0][2]) + "," + str(
                    matrixPresure[0][3]) + "," + str(matrixPresure[0][4]) + "," + \
                      str(matrixPresure[1][0]) + "," + str(matrixPresure[1][1]) + "," + str(matrixPresure[1][2]) + "," + str(
                    matrixPresure[1][3]) + "," + str(matrixPresure[1][4]) + "," +\
                      str(matrixPresure[2][0]) + "," + str(matrixPresure[2][1]) + "," + str(matrixPresure[2][2]) + "," + str(
                    matrixPresure[2][3]) + "," +  str(matrixPresure[2][4]) + "," +\
                      str(matrixPresure[3][0]) + "," + str(matrixPresure[3][1]) + "," + str(matrixPresure[3][2]) + "," + str(
                    matrixPresure[3][3]) + "," + str(matrixPresure[3][4]) + "," + \
                      str(matrixPresure[4][0]) + "," + str(matrixPresure[4][1]) + "," + str(matrixPresure[4][2]) + "," + str(
                    matrixPresure[4][3]) + "," + str(matrixPresure[4][4]) + "," + \
                    str(0)
            else:
                img = rz.resizeSignature("../Questioned(1287)/"+ files +"/"+ signature)

                # Image filtering
                imgSmooted = GaussS.gaussianBlur(1, 0.55, img)
                imgFiltered = bN.filter(imgSmooted)

                # Calculate the ones in the matrix.
                blackPoints = bN.calculateBlackPoints(imgFiltered)

                # Calculate the center of mass
                centerMass = bN.centroid(blackPoints)

                # Calculate the eccentricity
                # eccentricity = bN.calculateEccentricity(blackPoints)

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

                print str(centerMass[0]) + "," + str(centerMass[1]) + "," + \
                      str(kurtosis[0]) + "," + str(kurtosis[1]) + "," + str(testSkew) + "," + \
                      str(densePoints[0][0]) + "," + str(densePoints[0][1]) + "," + str(densePoints[1][0]) + "," + str(
                    densePoints[1][1]) + "," + str(densePoints[2][0]) + "," + str(densePoints[2][1]) + "," + \
                      str(densePoints[3][0]) + "," + str(densePoints[3][1]) + "," + str(densePoints[4][0]) + "," + str(
                    densePoints[4][1]) + "," + str(densePoints[5][0]) + "," + str(densePoints[5][1]) + "," + \
                      str(densePoints[6][0]) + "," + str(densePoints[6][1]) + "," + str(densePoints[7][0]) + "," + str(
                    densePoints[7][1]) + "," + str(densePoints[8][0]) + "," + str(densePoints[8][1]) + "," + \
                      str(densePoints[9][0]) + "," + str(densePoints[9][1]) + "," + \
                      str(matrixGradient[0][0][0]) + "," + str(matrixGradient[0][0][1]) + "," + str(
                    matrixGradient[0][1][0]) + "," + str(matrixGradient[0][1][1]) + "," + \
                      str(matrixGradient[0][2][0]) + "," + str(matrixGradient[0][2][1]) + "," + str(
                    matrixGradient[0][3][0]) + "," + str(matrixGradient[0][3][1]) + "," + \
                      str(matrixGradient[0][4][0]) + "," + str(matrixGradient[0][4][1]) + "," + \
                      str(matrixGradient[1][0][0]) + "," + str(matrixGradient[1][0][1]) + "," + str(
                    matrixGradient[1][1][0]) + "," + str(matrixGradient[1][1][1]) + "," + \
                      str(matrixGradient[1][2][0]) + "," + str(matrixGradient[1][2][1]) + "," + str(
                    matrixGradient[1][3][0]) + "," + str(matrixGradient[1][3][1]) + "," + \
                      str(matrixGradient[1][4][0]) + "," + str(matrixGradient[1][4][1]) + "," + \
                      str(matrixGradient[2][0][0]) + "," + str(matrixGradient[2][0][1]) + "," + str(
                    matrixGradient[2][1][0]) + "," + str(matrixGradient[2][1][1]) + "," + \
                      str(matrixGradient[2][2][0]) + "," + str(matrixGradient[2][2][1]) + "," + str(
                    matrixGradient[2][3][0]) + "," + str(matrixGradient[2][3][1]) + "," + \
                      str(matrixGradient[2][4][0]) + "," + str(matrixGradient[2][4][1]) + "," + \
                      str(matrixPresure[0][0]) + "," + str(matrixPresure[0][1]) + "," + str(
                    matrixPresure[0][2]) + "," + str(
                    matrixPresure[0][3]) + "," + str(matrixPresure[0][4]) + "," + \
                      str(matrixPresure[1][0]) + "," + str(matrixPresure[1][1]) + "," + str(
                    matrixPresure[1][2]) + "," + str(
                    matrixPresure[1][3]) + "," + str(matrixPresure[1][4]) + "," + \
                      str(matrixPresure[2][0]) + "," + str(matrixPresure[2][1]) + "," + str(
                    matrixPresure[2][2]) + "," + str(
                    matrixPresure[2][3]) + "," + str(matrixPresure[2][4]) + "," + \
                      str(matrixPresure[3][0]) + "," + str(matrixPresure[3][1]) + "," + str(
                    matrixPresure[3][2]) + "," + str(
                    matrixPresure[3][3]) + "," + str(matrixPresure[3][4]) + "," + \
                      str(matrixPresure[4][0]) + "," + str(matrixPresure[4][1]) + "," + str(
                    matrixPresure[4][2]) + "," + str(
                    matrixPresure[4][3]) + "," + str(matrixPresure[4][4]) + "," + \
                      str(1)


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
#         img = rz.resizeSignature("../TrainingSet/Offline Genuine/"+file)
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
#         print str(centerMass[0]) + "," + str(centerMass[1]) + "," + str(eccentricity) + "," + \
#               str(kurtosis[0]) + "," + str(kurtosis[1]) + "," + str(testSkew) + "," + \
#               str(densePoints[0][0]) + "," + str(densePoints[0][1]) + "," + str(densePoints[1][0]) + "," + str(
#             densePoints[1][1]) + "," + str(densePoints[2][0]) + "," + str(densePoints[2][1]) + "," + \
#               str(densePoints[3][0]) + "," + str(densePoints[3][1]) + "," + str(densePoints[4][0]) + "," + str(
#             densePoints[4][1]) + "," + str(densePoints[5][0]) + "," + str(densePoints[5][1]) + "," + \
#               str(densePoints[6][0]) + "," + str(densePoints[6][1]) + "," + str(densePoints[7][0]) + "," + str(
#             densePoints[7][1]) + "," + str(densePoints[8][0]) + "," + str(densePoints[8][1]) + "," + \
#               str(densePoints[9][0]) + "," + str(densePoints[9][1]) + "," + \
#             str(matrixGradient[0][0][0]) + "," + str(matrixGradient[0][0][1]) + "," + str(
#             matrixGradient[0][1][0]) + "," + str(matrixGradient[0][1][1]) + "," + \
#               str(matrixGradient[0][2][0]) + "," + str(matrixGradient[0][2][1]) + "," + str(
#             matrixGradient[0][3][0]) + "," + str(matrixGradient[0][3][1]) + "," + \
#               str(matrixGradient[0][4][0]) + "," + str(matrixGradient[0][4][1]) + "," + \
#               str(matrixGradient[1][0][0]) + "," + str(matrixGradient[1][0][1]) + "," + str(
#             matrixGradient[1][1][0]) + "," + str(matrixGradient[1][1][1]) + "," + \
#               str(matrixGradient[1][2][0]) + "," + str(matrixGradient[1][2][1]) + "," + str(
#             matrixGradient[1][3][0]) + "," + str(matrixGradient[1][3][1]) + "," + \
#               str(matrixGradient[1][4][0]) + "," + str(matrixGradient[1][4][1]) + "," + \
#               str(matrixGradient[2][0][0]) + "," + str(matrixGradient[2][0][1]) + "," + str(
#             matrixGradient[2][1][0]) + "," + str(matrixGradient[2][1][1]) + "," + \
#               str(matrixGradient[2][2][0]) + "," + str(matrixGradient[2][2][1]) + "," + str(
#             matrixGradient[2][3][0]) + "," + str(matrixGradient[2][3][1]) + "," + \
#               str(matrixGradient[2][4][0]) + "," + str(matrixGradient[2][4][1]) + "," + \
#               str(matrixPresure[0][0]) + "," + str(matrixPresure[0][1]) + "," + str(matrixPresure[0][2]) + "," + str(
#             matrixPresure[0][3]) + "," + str(matrixPresure[0][4]) + "," + \
#               str(matrixPresure[1][0]) + "," + str(matrixPresure[1][1]) + "," + str(matrixPresure[1][2]) + "," + str(
#             matrixPresure[1][3]) + "," + str(matrixPresure[1][4]) + "," + \
#               str(matrixPresure[2][0]) + "," + str(matrixPresure[2][1]) + "," + str(matrixPresure[2][2]) + "," + str(
#             matrixPresure[2][3]) + "," + str(matrixPresure[2][4]) + "," + \
#               str(matrixPresure[3][0]) + "," + str(matrixPresure[3][1]) + "," + str(matrixPresure[3][2]) + "," + str(
#             matrixPresure[3][3]) + "," + str(matrixPresure[3][4]) + "," + \
#               str(matrixPresure[4][0]) + "," + str(matrixPresure[4][1]) + "," + str(matrixPresure[4][2]) + "," + str(
#             matrixPresure[4][3]) + "," + str(matrixPresure[4][4]) + "," + \
#               str(1)
#
#         '''
#                 str(densePoints[0][0]) + "," + str(densePoints[0][1]) + "," + str(densePoints[1][0]) + "," + str(densePoints[1][1]) + "," + str(densePoints[2][0]) + "," + str(densePoints[2][1]) + "," + \
#                 str(densePoints[3][0]) + "," + str(densePoints[3][1]) + "," + str(densePoints[4][0]) + "," + str(densePoints[4][1]) + "," + str(densePoints[5][0]) + "," + str(densePoints[5][1]) + "," + \
#                 str(densePoints[6][0]) + "," + str(densePoints[6][1]) + "," + str(densePoints[7][0]) + "," + str(densePoints[7][1]) + "," + str(densePoints[8][0]) + "," + str(densePoints[8][1]) + "," + \
#                 str(densePoints[9][0]) + "," + str(densePoints[9][1]) + "," + str(densePoints[10][0]) + "," + str(densePoints[10][1]) + "," + str(densePoints[11][0]) + "," + str(densePoints[11][1]) + "," + \
#                 str(densePoints[12][0]) + "," + str(densePoints[12][1]) + "," + str(densePoints[13][0]) + "," + str(densePoints[14][1]) + "," + str(densePoints[14][0]) + "," + str(densePoints[14][1]) + "," + \
#                 str(densePoints[15][0]) + "," + str(densePoints[15][1]) + "," + str(densePoints[16][0]) + "," + str(densePoints[16][1]) + "," + str(densePoints[17][0]) + "," + str(densePoints[17][1]) + "," + \
#                 str(densePoints[18][0]) + "," + str(densePoints[18][1]) + "," + str(densePoints[19][0]) + "," + str(densePoints[19][1]) + ","  + \
#                 str(densePoints[20][0]) + "," + str(densePoints[20][1]) + "," + str(densePoints[21][0]) + "," + str(
#                 densePoints[21][1]) + "," + \
#                 str(densePoints[22][0]) + "," + str(densePoints[22][1]) + "," + str(densePoints[23][0]) + "," + str(
#                 densePoints[23][1]) + "," + \
#                 str(densePoints[24][0]) + "," + str(densePoints[24][1]) + "," + str(densePoints[25][0]) + "," + str(
#                 densePoints[25][1]) + "," + \
#                 str(densePoints[26][0]) + "," + str(densePoints[26][1]) + "," + str(densePoints[27][0]) + "," + str(
#                 densePoints[27][1]) + "," + \
#                 str(densePoints[28][0]) + "," + str(densePoints[28][1]) + "," + str(densePoints[29][0]) + "," + str(
#                 densePoints[29][1]) + "," + \
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
#         print str(centerMass[0]) + "," + str(centerMass[1]) + "," + str(eccentricity) + "," + \
#               str(kurtosis[0]) + "," + str(kurtosis[1]) + "," + str(testSkew) + "," + \
#               str(densePoints[0][0]) + "," + str(densePoints[0][1]) + "," + str(densePoints[1][0]) + "," + str(
#             densePoints[1][1]) + "," + str(densePoints[2][0]) + "," + str(densePoints[2][1]) + "," + \
#               str(densePoints[3][0]) + "," + str(densePoints[3][1]) + "," + str(densePoints[4][0]) + "," + str(
#             densePoints[4][1]) + "," + str(densePoints[5][0]) + "," + str(densePoints[5][1]) + "," + \
#               str(densePoints[6][0]) + "," + str(densePoints[6][1]) + "," + str(densePoints[7][0]) + "," + str(
#             densePoints[7][1]) + "," + str(densePoints[8][0]) + "," + str(densePoints[8][1]) + "," + \
#               str(densePoints[9][0]) + "," + str(densePoints[9][1]) + "," + \
#               str(matrixGradient[0][0][0]) + "," + str(matrixGradient[0][0][1]) + "," + str(
#             matrixGradient[0][1][0]) + "," + str(matrixGradient[0][1][1]) + "," + \
#               str(matrixGradient[0][2][0]) + "," + str(matrixGradient[0][2][1]) + "," + str(
#             matrixGradient[0][3][0]) + "," + str(matrixGradient[0][3][1]) + "," + \
#               str(matrixGradient[0][4][0]) + "," + str(matrixGradient[0][4][1]) + "," + \
#               str(matrixGradient[1][0][0]) + "," + str(matrixGradient[1][0][1]) + "," + str(
#             matrixGradient[1][1][0]) + "," + str(matrixGradient[1][1][1]) + "," + \
#               str(matrixGradient[1][2][0]) + "," + str(matrixGradient[1][2][1]) + "," + str(
#             matrixGradient[1][3][0]) + "," + str(matrixGradient[1][3][1]) + "," + \
#               str(matrixGradient[1][4][0]) + "," + str(matrixGradient[1][4][1]) + "," + \
#               str(matrixGradient[2][0][0]) + "," + str(matrixGradient[2][0][1]) + "," + str(
#             matrixGradient[2][1][0]) + "," + str(matrixGradient[2][1][1]) + "," + \
#               str(matrixGradient[2][2][0]) + "," + str(matrixGradient[2][2][1]) + "," + str(
#             matrixGradient[2][3][0]) + "," + str(matrixGradient[2][3][1]) + "," + \
#               str(matrixGradient[2][4][0]) + "," + str(matrixGradient[2][4][1]) + "," + \
#               str(matrixPresure[0][0]) + "," + str(matrixPresure[0][1]) + "," + str(matrixPresure[0][2]) + "," + str(
#             matrixPresure[0][3]) + "," + str(matrixPresure[0][4]) + "," + \
#               str(matrixPresure[1][0]) + "," + str(matrixPresure[1][1]) + "," + str(matrixPresure[1][2]) + "," + str(
#             matrixPresure[1][3]) + "," + str(matrixPresure[1][4]) + "," +\
#               str(matrixPresure[2][0]) + "," + str(matrixPresure[2][1]) + "," + str(matrixPresure[2][2]) + "," + str(
#             matrixPresure[2][3]) + "," +  str(matrixPresure[2][4]) + "," +\
#               str(matrixPresure[3][0]) + "," + str(matrixPresure[3][1]) + "," + str(matrixPresure[3][2]) + "," + str(
#             matrixPresure[3][3]) + "," + str(matrixPresure[3][4]) + "," + \
#               str(matrixPresure[4][0]) + "," + str(matrixPresure[4][1]) + "," + str(matrixPresure[4][2]) + "," + str(
#             matrixPresure[4][3]) + "," + str(matrixPresure[4][4]) + "," + \
#         str(0)
#
#         '''
#               str(densePoints[0][0]) + "," + str(densePoints[0][1]) + "," + str(densePoints[1][0]) + "," + str(
#             densePoints[1][1]) + "," + str(densePoints[2][0]) + "," + str(densePoints[2][1]) + "," + \
#               str(densePoints[3][0]) + "," + str(densePoints[3][1]) + "," + str(densePoints[4][0]) + "," + str(
#             densePoints[4][1]) + "," + str(densePoints[5][0]) + "," + str(densePoints[5][1]) + "," + \
#               str(densePoints[6][0]) + "," + str(densePoints[6][1]) + "," + str(densePoints[7][0]) + "," + str(
#             densePoints[7][1]) + "," + str(densePoints[8][0]) + "," + str(densePoints[8][1]) + "," + \
#               str(densePoints[9][0]) + "," + str(densePoints[9][1]) + "," + str(densePoints[10][0]) + "," + str(
#             densePoints[10][1]) + "," + str(densePoints[11][0]) + "," + str(densePoints[11][1]) + "," + \
#               str(densePoints[12][0]) + "," + str(densePoints[12][1]) + "," + str(densePoints[13][0]) + "," + str(
#             densePoints[14][1]) + "," + str(densePoints[14][0]) + "," + str(densePoints[14][1]) + "," + \
#               str(densePoints[15][0]) + "," + str(densePoints[15][1]) + "," + str(densePoints[16][0]) + "," + str(
#             densePoints[16][1]) + "," + str(densePoints[17][0]) + "," + str(densePoints[17][1]) + "," + \
#               str(densePoints[18][0]) + "," + str(densePoints[18][1]) + "," + str(densePoints[19][0]) + "," + str(
#             densePoints[19][1]) + "," + \
#               str(densePoints[20][0]) + "," + str(densePoints[20][1]) + "," + str(densePoints[21][0]) + "," + str(
#             densePoints[21][1]) + "," + \
#               str(densePoints[22][0]) + "," + str(densePoints[22][1]) + "," + str(densePoints[23][0]) + "," + str(
#             densePoints[23][1]) + "," + \
#               str(densePoints[24][0]) + "," + str(densePoints[24][1]) + "," + str(densePoints[25][0]) + "," + str(
#             densePoints[25][1]) + "," + \
#               str(densePoints[26][0]) + "," + str(densePoints[26][1]) + "," + str(densePoints[27][0]) + "," + str(
#             densePoints[27][1]) + "," + \
#               str(densePoints[28][0]) + "," + str(densePoints[28][1]) + "," + str(densePoints[29][0]) + "," + str(
#             densePoints[29][1]) + "," + \
#         '''
#

