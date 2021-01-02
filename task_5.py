"""
This module contains functions to work with divisions of relations of
equivalence on the classes of equivalence.
"""
def find_indexes(matrix: list) -> list:
    """
    Convert boolean matrix to the list of tuples.
    >>> find_indexes([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'),\
 ('c', 'a'), ('c', 'b'), ('c', 'c')]
    >>> find_indexes([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    []
    >>> find_indexes([[1, 0, 0], [0, 0, 0], [0, 0, 1]])
    [('a', 'a'), ('c', 'c')]
    """
    all_letters = 'abcdefghijklmnopqrstuvwxyz'
    indexes_list = []
    for row_index, lst in enumerate(matrix):
        for column_index, element in enumerate(lst):
            if element == 1:
                indexes_list.append(
                    (all_letters[row_index], all_letters[column_index]))
    return indexes_list


def find_matrix_elements(matrix: list) -> tuple:
    """
    Find all elements in the matrix. Return tuple of two elements that are lists.
    The first list contains all the elements and includes repetitive ones, while
    second list does not (it contains only the inuque elements).
    >>> find_matrix_elements([('a', 'a'), ('a', 'b'), ('a', 'c'),\
 ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')])
    (['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'], ['a', 'b', 'c'])
    >>> find_matrix_elements([])
    ([], [])
    >>> find_matrix_elements([('a', 'a'), ('c', 'c')])
    (['a', 'c'], ['a', 'c'])
    """
    all_elements = []  # all elements
    for _, col1 in matrix:
        for _, col2 in matrix:
            if col1 == col2:
                all_elements.append(col1)
                break

    unique_elements = []  # all elements without dublicates
    for element in all_elements:
        if element in unique_elements:
            continue
        unique_elements.append(element)
    return all_elements, unique_elements


def find_elements_amount(all_elements: list, unique_elements: list) -> list:
    """
    Find the number of occurrences of each element in the matrix. Return a
    list of tuples, where the first element is letter and the second one is
    its number of occurences.
    >>> find_elements_amount(['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'], ['a', 'b', 'c'])
    [('a', 3), ('b', 3), ('c', 3)]
    >>> find_elements_amount([], [])
    []
    >>> find_elements_amount(['a', 'c'], ['a', 'c'])
    [('a', 1), ('c', 1)]
    """
    tuples_list = []  # will be a list of all elements and their repetitions number
    # add the element to the list of tuples if it repeats more than 1 time
    for index1, elem1 in enumerate(all_elements):
        for index2, elem2 in enumerate(all_elements):
            if elem1 == elem2 and index1 != index2:
                if (index2 - index1) > 0:
                    number = index2 - index1  # how much times element repeates
                    tuples_list.append((elem1, number))
                break

    repetitive_letters = [tuples_list[i][0]
                          for i in range(len(tuples_list))]  # choose only letters
    # add the element to the list of tuples if it repeats only 1 time
    for letter in unique_elements:
        if letter not in repetitive_letters:
            tuples_list.append((letter, 1))
    return tuples_list


def find_all_classes(tuples_list: list) -> list:
    """
    Find all the equivalence classes. Return them as a list of lists
    (each class is a separate sublist).
    >>> find_all_classes([('a', 3), ('b', 3), ('c', 3)])
    [['a', 'b', 'c']]
    >>> find_all_classes([])
    []
    >>> find_all_classes([('a', 1), ('c', 1)])
    [['a'], ['c']]
    """
    dictionary = {}
    # add all the elements to the dict with the occurences numbers as its keys
    for letter, number in tuples_list:
        try:
            dictionary[number].append(letter)
        except KeyError:
            dictionary[number] = [letter]

    final_classes = []
    for number, letters in dictionary.items():
        if len(letters) > number:  # different classes with same elements number in one list
            if number == 1:
                classes = [[letter] for letter in letters]
            else:
                classes_number = int(len(letters) / number)
                # divide one list into several classes
                classes = [letters[i:i + classes_number]
                           for i in range(0, len(letters), classes_number)]
            final_classes.extend(classes)
        else:
            final_classes.append(letters)
    return final_classes


def find_equivalence_classes(matrix: list) -> list:
    """
    Find equivalence classes by the boolean matrix.
    >>> find_equivalence_classes([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    [['a', 'b', 'c']]
    >>> find_equivalence_classes([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    []
    >>> find_equivalence_classes([])
    []
    >>> find_equivalence_classes([[1, 0, 0], [0, 0, 0], [0, 0, 1]])
    [['a'], ['c']]
    >>> find_equivalence_classes([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 1, 0],\
 [0, 0, 1, 1, 0], [0, 0, 0, 0, 1]])
    [['a', 'b'], ['c', 'd'], ['e']]
    """
    matrix_indexes = find_indexes(matrix)
    all_elements, unique_elements = find_matrix_elements(matrix_indexes)
    tuples_list = find_elements_amount(all_elements, unique_elements)
    return find_all_classes(tuples_list)
