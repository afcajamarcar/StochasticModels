########################################
# Universidad Nacional de Colombia
# Sthochastic Models
########################################
# Authors
# Jeisson Andres Prieto Velandia
# Andres Felipe Cajamarca Rojas
# Juan Felipe Arango Manrique
########################################


from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
import csv
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

matrixData = []
vectorTarget = []

with open('learningBayesian.csv') as f:
    reader = csv.reader(f)
    reader.next()
    for i in reader:
        matrixData.append(map(float, i[2:6] +  i[41:len(i)-5]))
        #matrixData.append(map(float, i[3:len(i) - 1]))
        vectorTarget.append(int(i[len(i)-1]))


matrixData = np.array(matrixData)
print matrixData[0]
vectorTarget = np.array(vectorTarget)
print vectorTarget

clasifier = GaussianNB().fit(matrixData, vectorTarget)

y_predict = clasifier.predict(matrixData)

print accuracy_score(vectorTarget, y_predict)

print("Number of mislabeled points out of a total %d points : %d" % (matrixData.shape[0],( vectorTarget != y_predict).sum()))

X_train, X_test, y_train, y_test = train_test_split(matrixData, vectorTarget, test_size=0.4, random_state=0)

cls = svm.SVC(kernel='rbf', C=100).fit(X_train,y_train)

print cls.score(X_test, y_test)

clf = svm.SVC()

scores = cross_val_score(cls, matrixData, vectorTarget, cv=5)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))