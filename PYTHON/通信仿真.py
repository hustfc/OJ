import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import random
import statsmodels.api as sm
from numpy.core.multiarray import ndarray

R = 500    #蜂窝小区半径500m
Ndd = 10   #D2D用户数为10对
Ncell = 50  #蜂窝用户数为50个
Lmin = 25  #用户距基站的最小距离为25米
Lmax = 50   #D2D用户对之间的最大距离为50米
Pmax = 24   #最大发射功率为24dBm
P0 = -78   #P0=-78dBm，最小接受功率
a = 0.8     #计算功率控制的加权系数
N = 116    #热噪声功率N=116dBm
N_UE = 9   #用户的噪声指数为9dB
N_eNB = 5  #基站的噪声指数为5dB
B = 180     #带宽为180kHz
nSum = 1000   #循环次数

#路径损耗
PLdd = np.zeros([Ndd, 1])
PLcell = np.zeros([Ndd,1])
PLcell_dd = np.zeros([Ndd,1])
PLdd_eNB = np.zeros([Ndd,1])

#距离
Ddd_cell = np.zeros([Ndd, 1])
Ddd_eNB = np.zeros([Ndd ,1])
Dcell_eNB = np.zeros([Ndd,1])

#信干燥比与吞吐量
G_SINRdd = np.zeros([nSum,Ndd])
G_SINRcell = np.zeros([nSum,Ndd])
G_Thdd = np.zeros([nSum,Ndd])
G_Thcell = np.zeros([nSum,Ndd])

#确定蜂窝用户的位置
for j in range(nSum):
    xcell = np.random.random((Ncell, 1)) * R * 3/2 - R
    ycell = math.sqrt(3) * np.random.random((Ncell, 1)) * R - math.sqrt(3) * R / 2
    #print(ycell)
    for i in range(Ncell):
        if (xcell[i] <= -R/2) and (ycell[i] >= math.sqrt(3) * (xcell[i] + R)):
            xcell[i] = xcell[i] + 3 / 2 * R
            ycell[i] = ycell[i] - math.sqrt(3) * R / 2
        if (xcell[i] <= -R/2) and (ycell[i] <= -math.sqrt(3) * (xcell[i] + R)):
            xcell[i] = xcell[i] + 3 / 2 * R
            ycell[i] = ycell[i] + math.sqrt(3) * R / 2
        if xcell[i] ** 2 + ycell[i] ** 2 < Lmin ** 2:
            xcell[i] = random.random() * 3 / 2 * R - R
            ycell[i] = math.sqrt(3) * random.random() * R - math.sqrt(3) * R / 2
            i = i - 1
    Hcell = np.hstack((xcell, ycell)) #合并两个矩阵
    #print(Hcell)

    #确定D2D用户的位置，D2D发送方
    xddt = np.random.random((Ndd, 1)) * 3 / 2 * R - R
    yddt = math.sqrt(3) * np.random.random((Ndd, 1)) * R - math.sqrt(3) * R / 2
    i = 0
    while i < Ndd:
        if (xddt[i] <= -R/2) and (yddt[i] >= math.sqrt(3) * (xddt[i] + R)):
            xddt[i] = xddt[i] + 3 / 2 * R
            yddt[i] = yddt[i] - math.sqrt(3) * R / 2
        if (xddt[i] <= -R/2) and (yddt[i] <= -math.sqrt(3) * (xddt[i] + R)):
            xddt[i] = xddt[i] + 3 / 2 * R
            yddt[i] = yddt[i] + math.sqrt(3) * R / 2
        if xddt[i] ** 2 + yddt[i] ** 2 < Lmin ** 2:
            xddt[i] = random.random() * 3 / 2 * R - R
            yddt[i] = math.sqrt(3) * random.random() * R - math.sqrt(3) * R / 2
            i = i - 1
        i = i + 1
    Hddt = np.hstack((xddt, yddt))

    #D2D接收方
    Ddd_dd = np.random.random((Ndd, 1)) * Lmax
    xddr = np.zeros([Ndd, 1])
    yddr = np.zeros([Ndd, 1])
    i = 0
    while i < Ndd:
        z = random.random() * 2 * math.pi
        xddr[i] = xddt[i] + Ddd_dd[i] * math.cos(z)
        yddr[i] = yddt[i] + Ddd_dd[i] * math.sin(z)
        if yddr[i] > math.sqrt(3) / 2 * R or yddr[i] < -math.sqrt(3) / 2 * R:
            continue
        if xddr[i] < -R / 2 and (yddr[i] >= math.sqrt(3) * (xddr[i] + R) or yddr[i] < -math.sqrt(3) * (xddr[i] + R)):
            continue
        if xddr[i] > R / 2 and (yddr[i] >= -math.sqrt(3) * (xddr[i] - R) or yddr[i] < math.sqrt(3) * (xddr[i] - R)):
            continue
        i = i + 1
    Hddr = np.hstack((xddr, yddr))

    #资源复用
    Hdd_cell = np.zeros([Ndd, 2])
    n =np.arange(Ncell)
    random.shuffle(n)
    for i in range(Ndd):
        Hdd_cell[i, :] = Hcell[n[i], :]
    #print(Hdd_cell)
    H = Hddr - Hdd_cell  #距离矢量
    # print(H)
    # print(H[0,0])
    # print(H[0,1])

    #计算路径损耗
    for i in range(Ndd):
        #D2D用户之间的路径损耗
        if Ddd_dd[i] < 44.2:
            PLdd[i] = 38.47 + 20 * math.log(Ddd_dd[i], 10)
        else:
            PLdd[i] = 40.3 + 40 * math.log(Ddd_dd[i], 10)
        #蜂窝到D2D接收端的路径损耗
        Ddd_cell[i] = math.sqrt(H[i, 0] ** 2 + H[i, 1] ** 2)
        if Ddd_cell[i] < 44.2:
            PLcell_dd[i] = 38.47 + 20 * math.log(Ddd_cell[i], 10)
        else:
            PLcell_dd[i] = 40.3 + 40 * math.log(Ddd_cell[i], 10)
        #蜂窝用户的路径损耗
        Dcell_eNB[i] = math.sqrt(Hdd_cell[i, 0] ** 2 + Hdd_cell[i, 1] ** 2)
        if Dcell_eNB[i] < 35:
            PLcell[i] = 89.3
        else:
            PLcell[i] = 35.24 + 35 * math.log(Dcell_eNB[i], 10)
        #D2D发送端eNB的路径损耗
        Ddd_eNB[i] = math.sqrt(Hddt[i, 0] ** 2 + Hddt[i, 1] ** 2)
        if Ddd_eNB[i] < 35:
            PLdd_eNB[i] = 89.3;
        else:
            PLdd_eNB[i] =35.24 + 35 * math.log(Ddd_eNB[i])

    #发射功率
    TPdd = np.zeros([Ndd, 1])
    TPcell = np.zeros([Ndd, 1])
    for i in range(Ndd):
        TPdd[i] = min(Pmax, P0 + a * PLdd[i])
        TPcell[i] = min(Pmax, P0 + a * PLcell[i])

    #接受功率
    RPdd = TPdd - PLdd - N_UE
    RPcell = TPcell - PLcell - N_eNB
    #print(RPdd)

    #干扰计算
    Idd = TPdd - PLdd_eNB
    Icell = TPcell - PLcell_dd

    #用户的信干噪比(SINR)
    SINRdd = np.zeros([1, Ndd])
    SINRcell: ndarray = np.zeros([1, Ndd])
    for i in range(Ndd):
        SINRdd[0, i] = 10 * math.log(10 ** (RPdd[i] / 10 ) / (10 ** (Icell[i] / 10) + 10 ** (-N / 10)), 10)
        SINRcell[0, i] = 10 * math.log(10 ** (RPcell[i] / 10 ) / (10 ** (Idd[i] / 10) + 10 ** (-N / 10)), 10)
    #print(SINRdd)
    #用户的吞吐量
    Thdd = np.zeros([1, Ndd])
    Thcell = np.zeros([1, Ndd])
    for i in range(Ndd):
        Thdd[0, i] = B * math.log(1 + 10 ** (SINRdd[0, i] / 10), 2)
        Thcell[0, i] = B * math.log(1 + 10 ** (SINRcell[0, i] / 10), 2)

    G_SINRdd[j, :] = SINRdd
    G_SINRcell[j, :] = SINRcell
    G_Thdd[j, :] = Thdd
    G_Thcell[j, :] = Thcell



plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(1)
plt.plot(0,0,'mx',label='基站')
plt.plot(xcell, ycell, 'ro', label='蜂窝用户')
plt.plot(xddt, yddt, 'b*', label='D2D发送方')
plt.plot(xddr, yddr, 'c*', label='D2D接收方')
plt.title('蜂窝网络边界及用户分布')
plt.legend(loc='best')
plt.plot([-0.5 * R, 0.5 * R], [math.sqrt(3) * R/2, math.sqrt(3) * R/2],'k-')
plt.plot([-0.5 * R, 0.5 * R],[-math.sqrt(3) * R/2,-math.sqrt(3) * R/2],'k-')
plt.plot([- 1 * R,- 0.5 *R],[0, math.sqrt(3) * R/2],'k-')
plt.plot([- 1 * R,- 0.5 * R],[0,-math.sqrt(3) * R/2],'k-')
plt.plot([0.5 * R,R],[math.sqrt(3) * R/2,0],'k-')
plt.plot([0.5 * R,R],[-math.sqrt(3) * R/2,0],'k-')
plt.show()


plt.figure(2)
plt.title('用户SINR直方图')
plt.xlabel('SINR[dB]')
plt.ylabel('频数')
Range = np.arange(-20, 35, 1)
M = plt.hist(G_SINRdd, Range)
plt.show()

plt.figure(3)
plt.title('用户SINR分布图')
plt.xlabel('SINR[dB]')
plt.ylabel('CDF')
sample_dd = G_SINRdd.flatten()  #返回一个折叠成一堆的数组
ecdf = sm.distributions.ECDF(sample_dd)
#x = np.linspace(min(sample), max(sample))
x = np.linspace(-10, 35, 1000)
y = ecdf(x)
plt.plot(x, y, 'b-')
sample_cell = G_SINRcell.flatten()
ecdf = sm.distributions.ECDF(sample_cell)
x = np.linspace(-10, 35, 1000)
y = ecdf(x)
plt.plot(x, y, 'r-')
plt.show()


