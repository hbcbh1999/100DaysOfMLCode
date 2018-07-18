import random as rnd
from matplotlib import pyplot as plt
from numpy import *
from sklearn.datasets.samples_generator import make_blobs

data = make_blobs(n_samples=200, n_features=2, centers=3)

c_1 = [rnd.uniform(-10.0, 10.0), rnd.uniform(-10.0, 10.0)]
c_2 = [rnd.uniform(-10.0, 10.0), rnd.uniform(-10.0, 10.0)]
c_3 = [rnd.uniform(-10.0, 10.0), rnd.uniform(-10.0, 10.0)]

S_a = data[0][:,0]
P_a = data[0][:,1]

for num in range(0, 10):

    Dist1 = []
    Dist2 = []
    Dist3 = []

    Dist1 = ((S_a - c_1[0]) ** 2 + (P_a - c_1[1]) ** 2) ** 0.5
    Dist2 = ((S_a - c_2[0]) ** 2 + (P_a - c_2[1]) ** 2) ** 0.5
    Dist3 = ((S_a - c_3[0]) ** 2 + (P_a - c_3[1]) ** 2) ** 0.5

    centroid = []

    for i in range(0, len(data[0])):
        if Dist1[i] < Dist2[i] and Dist1[i] < Dist3[i]:
            centroid.append('1')
            #print('centroid1 added')
        if Dist2[i] < Dist1[i] and Dist2[i] < Dist3[i]:
            centroid.append('2')
            #print('centroid2 added')
        if Dist3[i] < Dist1[i] and Dist3[i] < Dist2[i]:
            centroid.append('3')
            #print('centroid3 added')

    l1 = []
    l2 = []
    l3 = []

    for i in range(0, len(centroid)):
        if centroid[i] == '1':
            l1.append([S_a[i], P_a[i]])
        if centroid[i] == '2':
            l2.append([S_a[i], P_a[i]])
        if centroid[i] == '3':
            l3.append([S_a[i], P_a[i]])

    l1_sumx = 0.0
    l1_sumy = 0.0
    l2_sumy = 0.0
    l3_sumx = 0.0
    l3_sumy = 0.0
    l2_sumx = 0.0

    for i in range(1, len(l1)):
        l1_sumx += float(str(l1[i][0]))
        l1_sumy += float(str(l1[i][1]))

    x = l1_sumx / float(len(l1) + 1)
    y = l1_sumy / float(len(l1) + 1)

    c_1[0] = x
    c_1[1] = y

    for i in range(1, len(l2)):
        l2_sumx += float(str(l2[i][0]))
        l2_sumy += float(str(l2[i][1]))

    x2 = l2_sumx / float(len(l2) + 1)
    y2 = l2_sumy / float(len(l2) + 1)

    c_2[0] = x2
    c_2[1] = y2

    for i in range(1, len(l3)):
        l3_sumx += float(str(l3[i][0]))
        l3_sumy += float(str(l3[i][1]))

    x3 = l3_sumx / float(len(l3) + 1)
    y3 = l3_sumy / float(len(l3) + 1)

    c_3[0] = x3
    c_3[1] = y3

    print(c_1, c_2, c_3)

plt.plot(S_a, P_a, 'ro', color='blue')
plt.plot(c_1[0], c_1[1], 'ro', color='red')
plt.plot(c_2[0], c_2[1], 'ro', color='red')
plt.plot(c_3[0], c_3[1], 'ro', color='red')
plt.savefig('fig1.png')
