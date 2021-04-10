import unittest

from neighbours import find_neighbours, filter_identical, filter_epsilon


class TestNeighboursMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.A = [1.25, 3.0, 3.5, 4.5, 5.2]
        self.B = [1.0, 2.0, 3.0]
        self.tupleList = [[(0, 0.5), (1, 2.5), (2, 0.0), (3, 3.0)]]
        self.epsilon = 1.0

    def test_empty_reference_list(self):
        with self.assertRaises(ValueError):
            find_neighbours(self.A, [])

    def test_filter_identical(self):
        result = [[(0, 0.5), (1, 2.5), (3, 3.0)]]
        self.assertEqual(filter_identical(self.tupleList), result)

    def test_filter_epsilon(self):
        result = [[(1, 2.5), (3, 3.0)]]
        self.assertEqual(filter_epsilon(self.tupleList, self.epsilon), result)

    def test_identical_and_epsilon_parameter(self):
        with self.assertRaises(ValueError):
            find_neighbours(self.A, self.B, skip_identical=True, epsilon=self.epsilon)

    def test_no_neighbours_with_epsilon(self):
        result = ([], [])
        self.assertEqual(find_neighbours(self.A, self.B, epsilon=10.0), result)

    def test_no_neighbours_with_skip_identical(self):
        result = ([], [])
        self.assertEqual(find_neighbours([1.0, 1.0, 1.0], [1.0, 1.0, 1.0], skip_identical=True), result)

    def test_find_neighbours_default(self):
        result = ([0, 2, 2, 2, 2], [0.25, 0.0, 0.5, 1.5, 2.2])
        self.assertEqual(find_neighbours(self.A, self.B), result)

    def test_find_neighbours_skip_identical(self):
        result = ([1, 0, 1], [1.0, 1.0, 1.0])
        self.assertEqual(find_neighbours(self.B, self.B, skip_identical=True), result)

    def test_find_neighbours_epsilon(self):
        result = ([2, 0, 1, 2, 2], [1.75, 2.0, 1.5, 1.5, 2.2])
        self.assertEqual(find_neighbours(self.A, self.B, epsilon=1.0), result)

    def test_find_neighbours_normal_nth_neighbour(self):
        result = ([1, 1, 1, 1, 1], [0.75, 1.0, 1.5, 2.5, 3.2])
        self.assertEqual(find_neighbours(self.A, self.B, n=2), result)

    def test_find_neighbours_high_nth_neighbour(self):
        result = ([2, 0, 0, 0, 0], [1.75, 2.0, 2.5, 3.5, 4.2])
        self.assertEqual(find_neighbours(self.A, self.B, n=10), result)




