import numpy
import csv

def stat(dataset,skipindex=[]):
    attrset = [list(x) for x in zip(*dataset)]
    for i,attrs in enumerate(attrset):
        if i in skipindex:
            continue
        attrs = list(map(float,attrs))
        print('属性{0}'.format(i))
        print('平均値:'+str(numpy.mean(attrs)))
        print('中央値:'+str(numpy.median(attrs)))
        print('分散:'+str(numpy.var(attrs)))
        print('標準偏差:'+str(numpy.std(attrs)))
        
        
if __name__ == '__main__':
    openfile = r"../data/wdbc.csv"
    with open(openfile) as file:
        reader = csv.reader(file)
        rowset = [row for row in reader]
    skipindex = [1]
        
    stat(rowset,skipindex)