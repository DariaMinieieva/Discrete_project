"""
This module contains task 2 for the discrete project.
It contains functions which build reflexive and symmetric closures of relations.
"""

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
    for ind, elem in enumerate(matrix):
        if elem[ind] == 0:
            elem[ind] = 1
    return matrix


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
    for row_ind, row in enumerate(matrix):
        for col_ind, _ in enumerate(row):
            if row[col_ind] == 1:
                matrix[col_ind][row_ind] = 1
    return matrix


if __name__ == "__main__":
    from doctest import testmod
    testmod()
