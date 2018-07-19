import random as rnd
from matplotlib import pyplot as plt
from numpy import *
from sklearn.datasets.samples_generator import make_blobs

def clustering(X, Y, c_1, c_2, c_3):
    counter = 0
    new_c1, new_c2, new_c3 = [], [], []
    while new_c1 != c_1 and new_c2 != c_2 and new_c3 != c_3:
        '''Updating centroids coordinates'''
        if counter != 0: c_1, c_2, c_3 = new_c1, new_c2, new_c3
        print(c_1, c_2, c_3)

        '''Computing the distances'''
        Dist1 = []
        Dist2 = []
        Dist3 = []
        Dist1 = ((X - c_1[0]) ** 2 + (Y - c_1[1]) ** 2) ** 0.5
        Dist2 = ((X - c_2[0]) ** 2 + (Y - c_2[1]) ** 2) ** 0.5
        Dist3 = ((X - c_3[0]) ** 2 + (Y - c_3[1]) ** 2) ** 0.5

        centroid = []

        '''Linking points and centroids'''
        for i in range(0, len(X)):
            if Dist1[i] < Dist2[i] and Dist1[i] < Dist3[i]:
                centroid.append('1')
            if Dist2[i] < Dist1[i] and Dist2[i] < Dist3[i]:
                centroid.append('2')
            if Dist3[i] < Dist1[i] and Dist3[i] < Dist2[i]:
                centroid.append('3')

        l1, l2, l3 = [], [], []

        for i in range(0, len(centroid)):
            if centroid[i] == '1':
                l1.append([X[i], Y[i]])
            if centroid[i] == '2':
                l2.append([X[i], Y[i]])
            if centroid[i] == '3':
                l3.append([X[i], Y[i]])

        '''Computing new centroids coordinates'''
        l1_sumx, l1_sumy = 0.0, 0.0
        l2_sumx, l2_sumy = 0.0, 0.0
        l3_sumx, l3_sumy = 0.0, 0.0

        for i in range(1, len(l1)):
            l1_sumx += float(str(l1[i][0]))
            l1_sumy += float(str(l1[i][1]))


        for i in range(1, len(l2)):
            l2_sumx += float(str(l2[i][0]))
            l2_sumy += float(str(l2[i][1]))

        for i in range(1, len(l3)):
            l3_sumx += float(str(l3[i][0]))
            l3_sumy += float(str(l3[i][1]))

        x1 = l1_sumx / float(len(l1) + 1)
        y1 = l1_sumy / float(len(l1) + 1)

        x2 = l2_sumx / float(len(l2) + 1)
        y2 = l2_sumy / float(len(l2) + 1)

        x3 = l3_sumx / float(len(l3) + 1)
        y3 = l3_sumy / float(len(l3) + 1)

        new_c1 = [x1, y1]
        new_c2 = [x2, y2]
        new_c3 = [x3, y3]

        counter += 1

    lx_centroids = [c_1[0], c_2[0], c_3[0]]
    ly_centroids = [c_1[1], c_2[1], c_3[1]]

    return lx_centroids, ly_centroids

def run():
    '''Generating dataset'''
    data = make_blobs(n_samples=200, n_features=2, centers=3)
    X = data[0][:,0]
    Y = data[0][:,1]
    x_max, x_min = amax(X), amin(X)
    y_max, y_min = amax(Y), amin(Y)
    c_1 = [rnd.uniform(x_min, x_max), rnd.uniform(y_min, y_max)]
    c_2 = [rnd.uniform(x_min, x_max), rnd.uniform(y_min, y_max)]
    c_3 = [rnd.uniform(x_min, x_max), rnd.uniform(y_min, y_max)]

    '''Running K-Means Clustering'''
    cx, cy = clustering(X, Y, c_1, c_2, c_3)

    '''Plotting points and centroids'''
    plt.plot(X, Y, 'ro', color='blue')
    plt.plot(cx, cy, 'ro', color='red')
    plt.plot()

if __name__ == '__main__':
    run()
