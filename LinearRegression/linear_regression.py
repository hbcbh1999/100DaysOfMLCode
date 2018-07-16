from numpy import *
from matplotlib import pyplot as plt

def compute_error(b, m , points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(points))

def step_gradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += - (2/N) * (y - ((m_current * x) + b_current))
        m_gradient += - (2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learningRate * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    listb = []
    listm = []
    for i in range(0, len(points)):
        b, m = step_gradient(b, m, array(points), learning_rate)
        listb.append(b)
        listm.append(m)
    return [b, m], [listm, listb]

def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = array(arange(15.0, 80.0, 0.1))
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')

def create_graph(points, list_m_b):
    m = list_m_b[0]
    b = list_m_b[1]

    x = []
    y = []

    for i in range(0, len(points)):
        x.append(points[i, 0])
        y.append(points[i, 1])

    for i in range(0, 10):
        plt.plot(x, y, "ro")
        abline(m[i], b[i])
        plt.savefig("fig{0}.png".format(i))

def run():
    points = genfromtxt("data.csv", delimiter=",")
    learning_rate = 0.0001
    initial_b = 5
    initial_m = 5
    num_iterations = 1000
    print('Starting gradient descent at b = {0}, m = {1}, error = {2}'.format(initial_b, initial_m, compute_error(initial_b, initial_b, points)))
    [b, m], lista = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print("at the end y = {0} * x + {1}".format(m, b))
    create_graph(points, lista)
    
if __name__ == "__main__":
    run()
