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


def Analyze(inputfilename,outputfilename):
#データのロード
    with open(inputfilename) as f:
        reader = csv.reader(f)
        l = [row for row in reader]

    #データの分割

    #ID = [int(row[0])for row in l ]
    #random.shuffle(ID)
    #randomID = list(np.array_split(ID,k))
    #sorted_ID = []
    #for i in randomID:
    #    a= np.sort(i)
    #    sorted_ID.append(a.tolist())

    #np.savetxt('crossd_ID.csv',sorted_ID,delimiter =",",fmt ='% s')
    #with open('crossd_ID.csv') as f:
    #    reader =  csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    #    crossd_ID = [[int(v) for v in row]for row in reader]


    #主成分分析
    df = pd.read_csv(inputfilename,names =label)
    dfID = df.iloc[:,:2]
    dfID = dfID.to_numpy()
    dfs = df.iloc[:, 2:].apply(lambda x: (x-x.mean())/x.std(), axis=0)#データの標準化
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
    plt.savefig(r"output/analysis.png")
    plt.show()

    #次元削減
    pca1 = PCA(n_components = k)
    #pca1 = PCA(n_components = 0.8)
    pca1.fit(dfs)
    X = pca1.transform(dfs)#次元削減後
    Y= np.hstack([dfID,np.array(X)])
    #低次元化したものを保存する
    np.savetxt(outputfilename, Y, delimiter =",",fmt ='% s')
    #with open('d=15_reduction_data.csv') as f:
    #    reader =  csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    #    acoeffs = [[int(v) for v in row]for row in reader]






