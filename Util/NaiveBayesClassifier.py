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

    print len(reader.next())
    for i in reader:
        #matrixData.append(map(float,  i[2:len(i)-5]))
        matrixData.append(map(float, i[2:5] + i[25:len(i) - 1]))
        vectorTarget.append(int(i[len(i)-1]))


matrixData = np.array(matrixData)
print matrixData[0]
vectorTarget = np.array(vectorTarget)
print vectorTarget



##### Support Vector machine

asdsada = svm.SVC(kernel='rbf', C=1)

X_train, X_test, y_train, y_test = train_test_split(matrixData, vectorTarget, test_size=0.2, random_state=0)

asdsada.fit(X_train, y_train)

y_predict = asdsada.predict(X_test)

print asdsada.score(X_test, y_test)

print accuracy_score(y_test, y_predict)


###################### Naive Bayes
naiveClassifier = GaussianNB().fit(X_train, y_train)

y_predict_Naive = naiveClassifier.predict(X_test)

print accuracy_score(y_test, y_predict_Naive)


######## Crossvalidation
scores = cross_val_score(asdsada, matrixData, vectorTarget, cv=5)
print("Accuracy SVM: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

scores = cross_val_score(naiveClassifier, matrixData, vectorTarget, cv=5)
print("Accuracy Naive: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


'''
clasifier = GaussianNB().fit(matrixData, vectorTarget)

y_predict = clasifier.predict(matrixData)

print accuracy_score(vectorTarget, y_predict)

print("Number of mislabeled points out of a total %d points : %d" % (matrixData.shape[0],( vectorTarget != y_predict).sum()))


X_train, X_test, y_train, y_test = train_test_split(matrixData, vectorTarget, test_size=0.4, random_state=0)

cls = svm.SVC(kernel='rbf', C=2).fit(X_train,y_train)

print cls.score(X_test, y_test)

clf = svm.SVC()

scores = cross_val_score(cls, matrixData, vectorTarget, cv=5)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
'''