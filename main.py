from datasetParser import initilizeDataset, parseDataset, segmentData, datasetIsCached, cacheDataset, loadCachedDataset
from matplotlib import pyplot as plt
from model import prepareData, defineModel, plot
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

#get dataset

if datasetIsCached():
    data, labels = loadCachedDataset()
else:
    initilizeDataset()
    images, masks, labels = parseDataset()
    data = images
    data = segmentData(images, masks)
    cacheDataset(data, labels)

#train model

X_train, X_test, y_train, y_test = prepareData(data, labels)
model = defineModel()
results = model.fit(X_train, y_train, validation_data = (X_test, y_test), batch_size = 128, epochs = 10, verbose = 1)
model.evaluate(X_test, y_test)
plot(results)

#validate model

Y_pred = model.predict(X_test)
Y_pred = np.argmax(Y_pred, axis = 1)
y_test = np.argmax(y_test, axis = 1)
target_names = ["1","2","3","4","5","6","7","8","9","10"]
print(confusion_matrix(y_test, Y_pred))
print(classification_report(y_test, Y_pred, target_names = target_names, zero_division = 1))
