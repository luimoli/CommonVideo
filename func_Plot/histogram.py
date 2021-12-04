import matplotlib.pyplot as plt
import numpy as np
import os

from collections import Counter

alist = (0, 1, 1, 1, 2, 3, 7, 7, 23)

def count_elements(seq):
    """[Tally elements from `seq`]
    Args:
        seq ([list]): [[e1,e2,...en]]
    Returns:
        [dict]: [{e1:number, e2:number, e3:number ...}]
    """
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

def count_elements_counter(seq):
    """[Tally elements from `seq` using python API]
    Args:
        seq ([list]): [[e1,e2,...en]]
    Returns:
        [dict]: [{e1:number, e2:number, e3:number ...}]
    """
    from collections import Counter
    recounted = Counter(seq)
    return recounted


def plot_his(x, y, save_path):
    """[summary]

    Args:
        x ([arr]): [x axis]
        y ([arr]): [y axis]
        save_path ([str]): [the path to save histogram figure]
        plt.barh:
            alpha：透明度
            facecolor：柱填充色
            edgecolor：柱轮廓色
            lw：柱子轮廓的宽度
            label：图例
    """
    plt.figure(figsize=(10,20)) #设置画布的尺寸
    plt.title('Histogram',fontsize=15)#标题，并设定字号大小
    plt.xlabel(u'num',fontsize=14)#设置x轴，并设定字号大小
    plt.ylabel(u'name',fontsize=14)#设置y轴，并设定字号大小
    plt.barh(x,y, alpha=0.6, facecolor='deeppink', edgecolor='deeppink', label='number of points')
    plt.legend(loc=4)#图例展示位置，数字代表第几象限
    plt.savefig(save_path, dpi=300, format='png', bbox_inches='tight')

def plot_dic_his(dic, save_path):
    xname,ynum = [],[]
    for i,v in dic.items():
        xname.append(i)
        ynum.append(v)
    plot_his(xname,ynum, save_path)






if __name__ == '__main__':
    data = ['a','b','c','d']
    data2 = [5,4,3,5]
    # plot_his(data, data2, 'test.png')


    import pandas as pd

    size, scale = 1000, 10
    commutes = pd.Series(np.random.gamma(scale, size=size) ** 1.5)

    commutes.plot.hist(grid=True, bins=20, rwidth=0.9,
                    color='#607c8e')
    plt.title('Commute Times for 1,000 Commuters')
    plt.xlabel('Counts')
    plt.ylabel('Commute Time')
    plt.grid(axis='y', alpha=0.75)

    # Y_hdr = np.load(r'../data/Y_hdr.npy')
    # x_diff = np.load(r'../data/x_diff.npy')
    # y_diff = np.load(r'../data/y_diff.npy')

    # Y_f = (np.floor(Y_hdr))

    # dic_x = {}
    # dic_y = {}
    # h, w = Y_hdr.shape
    # for i in range(h):
    #     for j in range(w):
    #         Y_index = Y_f[i][j]
    #         if str(Y_index) in dic_x:
    #             if x_diff[i][j] > 0.01:
    #                 dic_x[str(Y_index)] += 1
    #         else:
    #             dic_x[str(Y_index)] = 0

    #         if str(Y_index) in dic_y:
    #             if y_diff[i][j] > 0.01:
    #                 dic_y[str(Y_index)] += 1
    #         else:
    #             dic_y[str(Y_index)] = 0
    
    # print('.')
    # plot_dic_his(dic_x, 'x_diff.png')
    # plot_dic_his(dic_y, 'y_diff.png')





