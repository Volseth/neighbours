from typing import List


def find_neighbours(A: List[float], B: List[float], skip_identical=False, epsilon=None, n=None) -> (
        List[int], List[float]):
    neighbours = []
    distances = []

    if len(B) == 0:
        raise ValueError("Reference list must contain at least one element!")

    # If there is no n-th neighbour because of reference list's size, set n-th neighbour to max neighbour we can take
    if n is not None and n > len(B):
        n = len(B)
    # In other case take first element with closest distance
    elif n is None:
        n = 1

    # For each elem add its list of indexes in reference list and distances
    index_distance_tuple_matrix = []

    for number in A:
        number_distances = [abs(number - reference_number) for reference_number in B]

        # Change map distances to format (index, distance) for further filtering and receiving min values
        index_distance_tuple = list(enumerate(number_distances))
        index_distance_tuple = sorted(index_distance_tuple, key=lambda elem: elem[1])

        index_distance_tuple_matrix.append(index_distance_tuple)

    # Do list filtering
    if skip_identical and epsilon is not None:
        raise ValueError("You must either choose identical or epsilon filtering")
    elif skip_identical:
        index_distance_tuple_matrix = filter_identical(index_distance_tuple_matrix)
    elif epsilon is not None:
        index_distance_tuple_matrix = filter_epsilon(index_distance_tuple_matrix, epsilon)

    # Choose neighbours based on left neighbours after filtering
    for i in range(len(index_distance_tuple_matrix)):
        neighbours_after_filtering = len(index_distance_tuple_matrix[i])
        if neighbours_after_filtering != 0:
            index, distance = index_distance_tuple_matrix[i][n - 1 if neighbours_after_filtering > n else neighbours_after_filtering - 1]
            neighbours.append(index)
            distances.append(distance)

    return neighbours, distances


def filter_identical(matrix):
    filtered = []
    for tuple_list in matrix:
        filtered.append(list(filter(lambda distance: distance[1] != 0.0, tuple_list)))
    return filtered


def filter_epsilon(matrix, epsilon):
    filtered = []
    for tuple_list in matrix:
        filtered.append(list(filter(lambda distance: distance[1] > epsilon, tuple_list)))
    return filtered
