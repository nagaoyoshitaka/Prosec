# 必要なライブラリの import
import numpy as np
import pandas as pd
import array
import csv
import random

# 図やグラフを図示するためのライブラリをインポートする。
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

#主成分分析後の次元
k = 15

label = ['ID',
         'revue',
         
         'mean radius',
         'mean texture', 
         'mean perimeter',
         'mean area',
         'mean smoothness',
         'mean compactness',
         'mean concavity',
         'mean concave points',
         'mean symmetry',
         'mean fractal dimension',
         
         'radius SE',
         'texture SE', 
         'perimeter SE',
         'area SE',
         'smoothness SE',
         'compactness SE',
         'concavity SE',
         'concave points',
         'symmetry SE',
         'fractal dimension SE',
         
         'worst radius',
         'worst texture', 
         'worst perimeter',
         'worst area',
         'worst smoothness',
         'worst compactness',
         'worst concavity',
         'worst concave points',
         'worst symmetry',
         'worst fractal dimension']


def Analyze(inputfilename,outputfilename,outputglaphname):
#データのロード
    with open(inputfilename) as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        
        
    #主成分分析
    df = pd.read_csv(inputfilename,names =label)
    dfID = df.iloc[:,:2]
    dfID = dfID.to_numpy()
    if not "LDP" in inputfilename:
        dfs = df.iloc[:, 2:].apply(lambda x: (x-x.mean())/x.std(), axis=0)#データの標準化
    else:
        dfs = df.iloc[:,2:]
    pca = PCA()
    pca.fit(dfs)
    # 寄与率
    contribution = pd.DataFrame(pca.explained_variance_ratio_, index=["PC{}".format(x + 1) for x in range(len(dfs.columns))])
    # 累積寄与率を図示する
    plt.figure()
    plt.gca().get_xaxis().set_major_locator(ticker.MaxNLocator(integer=True))
    plt.plot([0] + list( np.cumsum(pca.explained_variance_ratio_)), "-o")
    plt.xlabel("Number of principal components")
    plt.ylabel("Cumulative contribution rate")
    plt.grid()
    plt.savefig(outputglaphname)
    plt.show()

    #次元削減
    pca1 = PCA(n_components = k)
    #pca1 = PCA(n_components = 0.8)
    pca1.fit(dfs)
    X = pca1.transform(dfs)#次元削減後
    Y= np.hstack([dfID,np.array(X)])
    #低次元化したものを保存する
    np.savetxt(outputfilename, Y, delimiter =",",fmt ='% s')


def SVM(inputfilename,IDs):
    # データのロード
    with open(inputfilename)as file:
        reader = csv.reader(file)
        DATA = []
        #二列目だけ"M"or"B"なので、"1"と"0"に対応付ける
        for row in reader:
            rowData = []
            for v in row:
                if v == "M":
                    rowData.append(float(1))
                elif v == "B":
                    rowData.append(float(0))
                else:
                    rowData.append(float(v))
            DATA.append(rowData)
            
    with open(IDs)as file:
        reader = csv.reader(file)
        crossed_ID = [[int(v) for v in row]for row in reader]
 
    scores = []
    # 線形SVMのインスタンスを生成
    model = SVC(kernel='linear', random_state=None)
    for IDs in crossed_ID:
    # データの分割  
        X_train = []#data
        y_train = []#target
        X_test = []#data
        y_test = []#target
        for data in DATA:
            if data[0] in IDs:
                X_test.append(data[2:])
                y_test.append(data[1])
            else:
                X_train.append(data[2:])
                y_train.append(data[1])

    #モデルの学習
        model.fit(X_train,y_train)       
    # テストデータに対する精度
        pred_test = model.predict(X_test)
        score = accuracy_score(y_test, pred_test)
        scores.append(score)
        
    ave_score = np.mean(scores)
    return (ave_score)