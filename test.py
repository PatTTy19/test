import unittest

def pyramid(rows):
    """Returns a list of strings representing a pyramid pattern with the given number of rows."""
    pyramid_pattern = []
    for i in range(1, rows + 1):
        row = ' ' * (rows - i) + '*' * (2 * i - 1)
        pyramid_pattern.append(row)
    return pyramid_pattern

class TestPyramid(unittest.TestCase):

    def test_single_row(self):
     
        self.assertEqual(pyramid(1), ["*"], "The pyramid with 1 row should be '*'")

    def test_three_rows(self):
       
        expected_output = [
            "  *",
            " ***",
            "*****"
        ]
        self.assertEqual(pyramid(3), expected_output, "The pyramid with 3 rows should match the expected pattern")

    def test_zero_rows(self):
  
        self.assertEqual(pyramid(0), [], "The pyramid with 0 rows should be an empty list")

    def test_five_rows(self):

        expected_output = [
            "    *",
            "   ***",
            "  *****",
            " *******",
            "*********"
        ]
        self.assertEqual(pyramid(5), expected_output, "The pyramid with 5 rows should match the expected pattern")

if __name__ == '__main__':
    unittest.main()
