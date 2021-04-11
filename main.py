import tests
from neighbours import find_neighbours
import unittest


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(tests)
    unittest.TextTestRunner(verbosity=2).run(suite)

    a = [1.5, 2.0, 4.2, 3.0]
    b = [1.0, 4.0, 3.2]
    neighbours, distances = find_neighbours(a, b)
    print("List: " + str(a))
    print("Reference list: " + str(b))
    print("Neighbours:" + str(neighbours))
    print("Distances: " + str(distances))
