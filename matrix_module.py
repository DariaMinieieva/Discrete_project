'''
This module contains functions to work
with sets represented as a matrix
'''

from copy import deepcopy

def read_file(path: str) -> list:
    """
    Read file with a matrix and return is as list of lists.
    >>> read_file('test.csv')
    [[0, 1, 0], [1, 0, 0], [1, 1, 1]]
    """
    with open(path) as matrix_file:
        matrix = matrix_file.read().splitlines()
    matrix = [i.split() for i in matrix]
    matrix = [list(map(int, i)) for i in matrix]
    return matrix


def write_file(matrix: list, path='matrix.csv'):
    """
    Write given matrix to a file.
    """
    matrix = [list(map(str, i)) for i in matrix]
    matrix = [','.join(i) + '\n' for i in matrix]
    with open(path, 'w') as matrix_file:
        matrix_file.writelines(matrix)


def reflexive_closure(matrix: list) -> list:
    """
    Returns a list (matrix) that contains a reflexive closure of a relation.
    >>> reflexive_closure([[0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]])
    [[1, 0, 0, 1], [1, 1, 1, 0], [1, 0, 1, 1], [0, 0, 1, 1]]
    >>> reflexive_closure([[1, 0, 0, 1], [1, 1, 1, 0], [1, 0, 1, 1], [0, 0, 1, 1]])
    [[1, 0, 0, 1], [1, 1, 1, 0], [1, 0, 1, 1], [0, 0, 1, 1]]
    >>> reflexive_closure([[0, 1, 0, 1], [1, 1, 1, 0], [0, 0, 0, 1], [0, 0, 1, 1]])
    [[1, 1, 0, 1], [1, 1, 1, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
    >>> reflexive_closure([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    """
    copy_matrix = deepcopy(matrix)

    for ind, elem in enumerate(copy_matrix):
        elem[ind] = 1
    return copy_matrix


def symmetric_closure(matrix: list) -> list:
    """
    Returns a list (matrix) that contains a symmetric closure of a relation.
    >>> symmetric_closure([[0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]])
    [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    >>> symmetric_closure([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    >>> symmetric_closure([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    >>> symmetric_closure([[1, 1, 1, 0], [0, 1, 0, 1], [0, 1, 1, 0], [0, 0, 0, 1]])
    [[1, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 0], [0, 1, 0, 1]]
    """
    copy_matrix = deepcopy(matrix)

    for row_ind, row in enumerate(copy_matrix):
        for col_ind, _ in enumerate(row):
            if row[col_ind] == 1:
                copy_matrix[col_ind][row_ind] = 1
    return copy_matrix


def warshall_algorithm(matrix: list) -> list:
    '''
    Return transitive closure of given matrix

    >>> warshall_algorithm([[0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]])
    [[1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]]
    '''
    copy_matrix = deepcopy(matrix)
    m_len = len(copy_matrix)

    for i in range(m_len):
        for j in range(m_len):
            if (i != j) and (copy_matrix[j][i] == 1):
                for k in range(m_len):
                    # 1 == 1 and 0 == 0 in binary so binary OR can be used here
                    copy_matrix[j][k] = copy_matrix[j][k] | copy_matrix[i][k]

    return copy_matrix


def check_transitive_closure(matrix: list) -> bool:
    '''
    Return True if matrix is transitive and False otherwise

    >>> check_transitive_closure([[0, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]])
    False
    >>> check_transitive_closure([[1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]])
    True
    '''
    copy_matrix = deepcopy(matrix)
    m_len = len(copy_matrix)

    for i in range(m_len):
        for j in range(m_len):
            if (i != j) and (copy_matrix[j][i] == 1):
                for k in range(m_len):
                    # if at least one 0 will be changed - it is not transitive closure
                    if copy_matrix[j][k] == 0  and copy_matrix[i][k] == 1:
                        return False

                    # 1 == 1 and 0 == 0 in binary so binary OR can be used here
                    copy_matrix[j][k] = copy_matrix[j][k] | copy_matrix[i][k]

    return True


def find_indexes(matrix: list) -> list:
    """
    Convert boolean matrix to the list of tuples.
    >>> find_indexes([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    [('a0', 'a0'), ('a0', 'a1'), ('a0', 'a2'), ('a1', 'a0'), ('a1', 'a1'), ('a1', 'a2'),\
('a2', 'a0'), ('a2', 'a1'), ('a2', 'a2')]
    >>> find_indexes([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    []
    >>> find_indexes([[1, 0, 0], [0, 0, 0], [0, 0, 1]])
    [('a0', 'a0'), ('a2', 'a2')]
    """
    indexes_list = []
    for row_index, lst in enumerate(matrix):
        for column_index, element in enumerate(lst):
            if element == 1:
                indexes_list.append(
                    ('a' + str(row_index), 'a' + str(column_index)))
    return indexes_list


def find_classes(matrix: list) -> list:
    """
    Return list of equivalence classes on given matrix.
    >>> find_classes([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 1, 0],[0, 0, 1, 1, 0], [0, 0, 0, 0, 1]])
    [['a0', 'a1'], ['a3', 'a2], ['a4']]
    >>> find_classes([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    [['a0', 'a1'], ['a2']]
    """
    relation = find_indexes(matrix)
    classes = []
    while relation != []:
        represent = relation[0][0]
        eq_class = [i[1] for i in list(filter(lambda x: x[0] == represent, relation))]
        classes.append(eq_class)
        for i in eq_class:
            relation = list(filter(lambda x: i not in x, relation))
    return classes


def generate_fragment(length: int, fragment: list, counter: int = 0) -> list:
    '''
    Recursive function, which generates all binary strings
    and return list of these strings
    >>> generate_fragment(1, [0])
    [[0], [1]]
    >>> generate_fragment(2, [0, 0])
    [[0, 0], [0, 1], [1, 0], [1, 1]]
    '''
    if counter == length:
        return [fragment[:]]

    fragment[counter] = 0
    fragment_list = generate_fragment(length, fragment, counter + 1)
    fragment[counter] = 1
    fragment_list += generate_fragment(length, fragment, counter + 1)
    return fragment_list


def count_of_transitive_relations(elements: int):
    '''
    Return count of all different transitive relations
    >>> count_of_transitive_relations(0)
    1
    >>> count_of_transitive_relations(1)
    2
    >>> count_of_transitive_relations(2)
    13
    >>> count_of_transitive_relations(3)
    171
    >>> count_of_transitive_relations(-1)

    '''
    if elements < 0:
        return None

    matrix_list = [[]]
    fragment_list = generate_fragment(elements, [0] * elements)

    for row in range(elements):
        new_list = []
        for matrix in matrix_list:
            for fragment in fragment_list:
                check_matrix = matrix + [fragment]
                if row == 0 or check_transitive_closure(check_matrix):
                    new_list.append(check_matrix)

        matrix_list = new_list
        new_list = []

    return len(matrix_list)
