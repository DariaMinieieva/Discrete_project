"""
Task 1 for discrete project.
"""


def read_file(path: str) -> list:
    """
    Read file with a matrix and return is as list of lists.
    >>> read_file('test.csv')
    [[0, 1, 0], [1, 0, 0], [1, 1, 1]]
    """
    with open(path) as matrix_file:
        matrix = matrix_file.read().splitlines()
    matrix = [i.split(',') for i in matrix]
    matrix = [list(map(int, i)) for i in matrix]
    return matrix


def write_file(matrix: list, path='matrix.csv'):
    """
    Write given matrix to a file.
    """
    matrix = [','.join(i) + '\n' for i in matrix]
    with open(path, 'w') as matrix_file:
        matrix_file.writelines(matrix)
