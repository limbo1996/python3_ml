'''
Author: wangxuan
Date: 2020-12-22 22:50:25
LastEditors: wangxuan
LastEditTime: 2020-12-22 23:32:45
Description: file content
'''
import numpy as np
import operator

def createDataset():
    group = np.array([[1.0, 1.1],
                    [1.0, 1.0],
                    [0,0],
                    [0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels



'''
# >>> group
# array([[1. , 1.1],
#         [1. , 1. ],
#         [0. , 0. ],
#         [0. , 0.1]])
# >>> labels
# ['A', 'A', 'B', 'B']
'''
# 计算距离
def classfy0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0] # 行数
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet 
    '''
    # 在行上重复inX dataSetSize次，列上1次， 
    '''
    sqSiffMat = diffMat ** 2 # 计算两个距离地平方
    sqDistance = sqSiffMat.sum(axis = 1) # 计算平方和, sum(1) 行相加
    distance = sqDistance ** 0.5 # 开根号得到距离
    sortedDistIndicies = distance.argsort()# 返回从小到大地索引
    # 一个记录次数地字典
    classCount = {}
    # 取出前k个元素
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]# 遍历每一个label
        # get 函数 在classCOunt中查找该label， 如果没有返回指定的值, 如果有就返回指定键的值, 
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1 
        
    #python3中用items()替换python2中的iteritems()
    #key=operator.itemgetter(1)根据字典的值进行排序
    #key=operator.itemgetter(0)根据字典的键进行排序
    #reverse降序排列
        
    sortedClassCount = sorted(classCount.items(), 
                                key = operator.itemgetter(1), 
                                reverse=True)
    
    # 返回次数最多的类别
    # [('B', 3), ('A', 1)] 返回的样式是一个列表
    
    return sortedClassCount[0][0]




if __name__ == '__main__':
    group, labels = createDataset()
    test = [101, 20]
    
    test_class = classfy0(test, group, labels, 3)
    print(test_class)