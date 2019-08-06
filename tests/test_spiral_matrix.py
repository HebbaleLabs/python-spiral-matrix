import unittest
from parameterized import parameterized
from spiral_matrix import do_spiral_order


class SpiralOrderMatrixTest(unittest.TestCase):

    @parameterized.expand([
        (2, [[1, 2], [4, 3]]),
        (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
        (1, [[1]]),
        (5, [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]),
        (0, [[]]),
        (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]),
    ])
    def test_spiral_order(self, input_value, expected_result):
        self.longMessage = True
        actual = do_spiral_order(input_value)
        message = 'For input {0}, expected result = {1}, and actual value = {2}'.format(input_value, expected_result, actual)
        self.assertEqual(expected_result, actual, message)
