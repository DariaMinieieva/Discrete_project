'''
Tasks 3, 4 and 6 for discrete project
'''

from copy import deepcopy

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
    return matrix == warshall_algorithm(matrix)


def generate_fragment(lenght: int, fragment: list, counter: int = 0) -> list:
    '''
    Recursive function, which generates all binary strings
    and return list of these strings
    >>> generate_fragment(1, [0])
    [[0], [1]]
    >>> generate_fragment(2, [0, 0])
    [[0, 0], [0, 1], [1, 0], [1, 1]]
    '''
    if counter == lenght:
        return [fragment[:]]

    fragment[counter] = 0
    fragment_list = generate_fragment(lenght, fragment, counter + 1)
    fragment[counter] = 1
    fragment_list += generate_fragment(lenght, fragment, counter + 1)
    return fragment_list


def count_of_transitive_relations(elements: int) -> int:
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
