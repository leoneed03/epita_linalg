import numpy as np


class Error(Exception):
    pass

class WrongInputError(Error):
    pass

def get_exit_command():
    return 'escape'

def check_if_need_to_exit(input):
    return input == get_exit_command()

def print_welcome_message():
    print('Welcome to the change of basis app\nPrint ', get_exit_command(), ' to exit')

def read_vector(N):
    print('Please input a vector of dimension N using \',\' as a delimeter', N)
    s = input()
    values = s.split(',')

    vv = np.array([float(x) for x in values])

    if len(vv) != N:
        print('Expected vector of dimension N =', N, 'and actual N =', len(vv))
        raise WrongInputError()

    return vv

def read_matrix(N):
    print('Please input a square matrix of dimension N = ',
          N, '\n line by line using \',\' as a delimeter representing N linearly independent vectors as a basis')
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

    return np.linalg.inv(m).dot(v)

if __name__ == '__main__':

    try:
        print_welcome_message()

        result = change_basis()
        print('Vector in the new basis: ', result)
    except WrongInputError:
        print("Please provide correct input next time\nGoodbye!")
