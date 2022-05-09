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

def read_basis_matrix(N):
    print('Please input a square matrix of dimension N =',
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

    b_old = np.eye(N)
    print('Is your vector in canonical basic? y/n')
    answer = input()

    if (answer == "n"):
        print('Please provide matrix representing the OLD basis of your vector')
        b_old = read_basis_matrix(N)

    print('Please provide matrix representing the NEW basis')
    b_new = read_basis_matrix(N)

    if N == 2:
        print('Do you want to save a plot with your vector and basis? y/n')
        answer = input()
        if (answer == "y"):
            print('Please provide a filename')
            filename = input()

            xs = np.append(np.array(b_new[0, :]), np.array(b_old[0, :]))
            ys = np.append(np.array(b_new[1, :]), np.array(b_old[1, :]))
            xs = np.append(xs, v[0])
            ys = np.append(ys, v[1])

            plt.quiver([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], xs, ys, color=['r', 'r', 'b', 'b', 'g'], angles='xy', scale_units='xy', scale=1)

            lim_x = max([max(abs(b_old[0, :])), max(abs(b_new[0, :])), abs(v[0])]) + 1
            lim_y = max([max(abs(b_old[1, :])), max(abs(b_new[1, :])), abs(v[1])]) + 1

            lim_x_y = max(lim_x, lim_y)
            lim_x = lim_x_y
            lim_y = lim_x_y

            plt.xlim(-lim_x, lim_x)
            plt.ylim(-lim_y, lim_y)

            plt.title('Red - new basis, Blue - old basis, Green - your vector')

            plt.savefig(filename)

    return np.linalg.inv(b_new).dot(b_old).dot(v)

if __name__ == '__main__':
    try:
        print_welcome_message()
        result = change_basis()
        print('Vector in the new basis: ', result)
    except WrongInputError:
        print("Please provide correct input next time\nGoodbye!")
