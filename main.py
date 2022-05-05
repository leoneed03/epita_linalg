import numpy as np

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
        raise ValueError('Expected vector of dimension N =', N, 'and actual N =', len(vv))

    return vv

def read_matrix(N):
    print('Please input a square matrix of dimension N', N, '\n line by line using \',\' as a delimeter')
    m = np.eye(N)

    for i in range(N):
        s = input()
        values = s.split(',')

        v = np.array([float(x) for x in values])

        if len(v) != N:
            raise ValueError('Expected vector of dimension N =', N, 'and actual N =', len(v))
        m[i] = v

    return m

def change_basis():
    print('Please input N = number of dimensions')
    N = int(input())

    v = read_vector(N)
    m = read_matrix(N)

    print(v)
    print(m)

    return np.linalg.inv(m).dot(v)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_welcome_message()

    result = change_basis()
    print('End: ', result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
