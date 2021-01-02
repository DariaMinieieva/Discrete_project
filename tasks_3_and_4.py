'''
Tasks 3 and 4 for discrete project
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

     
