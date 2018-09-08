import csv
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn import svm
from sklearn import metrics
from sklearn.cross_validation import train_test_split
import numpy as np
data = pd.read_csv('fh.csv',encoding='iso-8859-1')
data1 = pd.read_csv('fg.csv',encoding='iso-8859-1')
data2 = pd.read_csv('fi.csv',encoding='iso-8859-1')

print("\n \t Initial Training")
data1['label']=np.resize(['Standing']*270,(270,1))
data['label']=np.resize(['Running']*270,(270,1))
data2['label']=np.resize(['Cycling']*270,(270,1))
d=[data, data1, data2]
p=pd.concat(d)
headers=list(p)
train_x, test_x, train_y, test_y = train_test_split(p[headers[:-1]],p[headers[-1]], train_size=0.7)
lr = linear_model.LogisticRegression()
lr.fit(train_x, train_y)
mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg').fit(train_x, train_y)
print("Logistic regression Train Accuracy :: ", metrics.accuracy_score(train_y, lr.predict(train_x)))
print("Logistic regression Test Accuracy :: ", metrics.accuracy_score(test_y, lr.predict(test_x)))
print("Multinomial Logistic regression Train Accuracy :: ", metrics.accuracy_score(train_y, mul_lr.predict(train_x)))
print("Multinomial Logistic regression Test Accuracy :: ", metrics.accuracy_score(test_y, mul_lr.predict(test_x)))
svc = svm.SVC(kernel='linear').fit(train_x, train_y)
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7).fit(train_x, train_y)
poly_svc = svm.SVC(kernel='poly', degree=3).fit(train_x, train_y)
print("SVM linear Train Accuracy :: ", metrics.accuracy_score(train_y, svc.predict(train_x)))
print("SVM linear Test Accuracy :: ", metrics.accuracy_score(test_y, svc.predict(test_x)))
print("rbf SVM Train Accuracy :: ", metrics.accuracy_score(train_y, rbf_svc.predict(train_x)))
print("rbf SVM Test Accuracy :: ", metrics.accuracy_score(test_y, rbf_svc.predict(test_x)))
print("poly SVM Train Accuracy :: ", metrics.accuracy_score(train_y, poly_svc.predict(train_x)))
print("poly SVM Test Accuracy :: ", metrics.accuracy_score(test_y, poly_svc.predict(test_x))) 


print("\n \t Initial Testing")
data4 = pd.read_csv('fk.csv',encoding='iso-8859-1')
data3 = pd.read_csv('fj.csv',encoding='iso-8859-1')
data5 = pd.read_csv('fl.csv',encoding='iso-8859-1')
data3['label']=np.resize(['Standing']*80,(80,1))
data4['label']=np.resize(['Running']*60,(60,1))
data5['label']=np.resize(['Cycling']*79,(79,1))
d=[data3, data4, data5]
q=pd.concat(d)
print("Logistic regression Test Accuracy :: ", metrics.accuracy_score(q[headers[-1]], lr.predict(q[headers[:-1]])))
print("Multinomial Logistic regression Test Accuracy :: ", metrics.accuracy_score(q[headers[-1]], mul_lr.predict(q[headers[:-1]])))
print("SVM linear Test Accuracy :: ", metrics.accuracy_score(q[headers[-1]], svc.predict(q[headers[:-1]])))
print("rbf SVM Test Accuracy :: ", metrics.accuracy_score(q[headers[-1]], rbf_svc.predict(q[headers[:-1]])))
print("poly SVM Test Accuracy :: ", metrics.accuracy_score(q[headers[-1]], poly_svc.predict(q[headers[:-1]])))


print("\n \t Final Training and Testing")
d=[p,q]
r=pd.concat(d)
train_x, test_x, train_y, test_y = train_test_split(r[headers[:-1]],r[headers[-1]], train_size=0.7)
lr1 = linear_model.LogisticRegression()
lr1.fit(train_x, train_y)
mul_lr1 = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg').fit(train_x, train_y)
print("Logistic regression Train Accuracy :: ", metrics.accuracy_score(train_y, lr1.predict(train_x)))
print("Logistic regression Test Accuracy :: ", metrics.accuracy_score(test_y, lr1.predict(test_x)))
print("Multinomial Logistic regression Train Accuracy :: ", metrics.accuracy_score(train_y, mul_lr1.predict(train_x)))
print("Multinomial Logistic regression Test Accuracy :: ", metrics.accuracy_score(test_y, mul_lr1.predict(test_x)))
svc1 = svm.SVC(kernel='linear').fit(train_x, train_y)
rbf_svc1 = svm.SVC(kernel='rbf', gamma=0.7).fit(train_x, train_y)
poly_svc1 = svm.SVC(kernel='poly', degree=3).fit(train_x, train_y)
print("SVM linear Train Accuracy :: ", metrics.accuracy_score(train_y, svc1.predict(train_x)))
print("SVM linear Test Accuracy :: ", metrics.accuracy_score(test_y, svc1.predict(test_x)))
print("rbf SVM Train Accuracy :: ", metrics.accuracy_score(train_y, rbf_svc1.predict(train_x)))
print("rbf SVM Test Accuracy :: ", metrics.accuracy_score(test_y, rbf_svc1.predict(test_x)))
print("poly SVM Train Accuracy :: ", metrics.accuracy_score(train_y, poly_svc1.predict(train_x)))
print("poly SVM Test Accuracy :: ", metrics.accuracy_score(test_y, poly_svc1.predict(test_x)))