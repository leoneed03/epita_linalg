import numpy as np
from matplotlib import pyplot as plt

class Error(Exception):
    pass

class WrongInputError(Error):
    pass

def print_welcome_message():
    print('Welcome to the change of basis app')

def read_vector(N):
    print('Please input a vector of dimension N using \',\' as a delimeter', N)
    s = input()
    values = s.split(',')

    v = np.array([float(x) for x in values])

    if len(v) != N:
        print('Expected vector of dimension N =', N, 'and actual N =', len(v))
        raise WrongInputError()

    return v

def read_matrix(N):
    print('Please input a square matrix of dimension N = ',
          N, '\n line by line using \',\' as a delimeter representing N linearly independent vectors as a basis column wise')
    m = np.eye(N)

    for i in range(N):
        s = input()
        values = s.split(',')

        v = np.array([float(x) for x in values])

        if len(v) != N:
            print('Expected vector of dimension N =', N, 'and actual N =', len(v))
            raise WrongInputError()
        m[i] = v

    if abs(np.linalg.det(m)) < 1e-6:
        print('Provided matrix is singular, it does not represent a basis')
        raise WrongInputError()

    return m

def change_basis():
    print('Please input N = number of dimensions')
    N = int(input())

    v = read_vector(N)
    m = read_matrix(N)

    if N == 2:
        print('Do you want to save a plot with your vector and basis? y/n')
        answer = input()
        if (answer == "y"):
            print('Please provide a filename')
            filename = input()

            xs = np.append(np.array(m[0, :]), v[0])
            ys = np.append(np.array(m[1, :]), v[1])
            plt.quiver([0, 0, 0], [0, 0, 0], xs, ys, color=['b', 'b', 'g'], angles='xy', scale_units='xy', scale=1)

            lim_x = max([max(abs(m[0, :])), abs(v[0])]) + 1
            lim_y = max([max(abs(m[1, :])), abs(v[1])]) + 1
            print(max(abs(m[0, :])))
            print()
            plt.xlim(-lim_x, lim_x)
            plt.ylim(-lim_y, lim_y)

            plt.savefig(filename)

    return np.linalg.inv(m).dot(v)

if __name__ == '__main__':
    try:
        print_welcome_message()
        result = change_basis()
        print('Vector in the new basis: ', result)
    except WrongInputError:
        print("Please provide correct input next time\nGoodbye!")
