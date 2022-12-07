import pandas as pd
import scipy.io as scio
import numpy as np


#total
def getOdataDieselTotal():
    dataFile = '../data/'
    dataName = 'diesel_total.mat'
    data = scio.loadmat(dataFile + dataName)
    datax_train = data['Xcal']
    datax_test = data['Xtest']
    datay_train = data['Ycal']
    datay_test = data['Ytest']
    dataxcal = np.empty(620, dtype=float)
    dataxtest = np.empty(164, dtype=float)
    tempDataViscxcal = []
    tempDataViscxtest = []
    for i1 in range(len(datay_train)):
        if(np.isnan(datay_train[i1])):
            tempDataViscxcal.append(i1)
    for i2 in range(len(datay_test)):
        if(np.isnan(datay_test[i2])):
            tempDataViscxtest.append(i2)
    datax_train = np.delete(datax_train, tempDataViscxcal, axis=0)
    datax_test = np.delete(datax_test, tempDataViscxtest, axis=0)
    print(len(datax_test))
    datay_train = np.delete(datay_train, tempDataViscxcal)
    datay_test = np.delete(datay_test, tempDataViscxtest)
    a = len(datax_train)
    b = len(datax_test)
    datax_train -= datax_train.mean(axis=0)
    datax_test -= datax_test.mean(axis=0)
    datax_train /= datax_train.std(axis=0)
    datax_test /= datax_test.std(axis=0)
    datax_train = datax_train.astype('float32')
    datax_test = datax_test.astype('float32')
    datay_train = datay_train.astype('float32')
    datay_test = datay_test.astype('float32')
    datax_train = datax_train.reshape(a, 401)
    datax_test = datax_test.reshape(b, 401)
    print(a, b)

    return datax_test, datay_test, datax_train, datay_train

## 向CSV中写入数据
def write_To_Csv_Total(write_data):
    df = pd.DataFrame(write_data,
                      columns=['num', 'model_name', 'epochs', 'batch_size', 'RMSEC', 'R_C', 'RMSEP', 'R_P'])  # 列表数据转为数据框
    df.to_csv('dataResultsDieselTotal.csv', mode='a', index=False, header=False)
    return
