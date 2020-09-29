import unittest
from src.input_reader import read_input


class TestReader(unittest.TestCase):
    """Test the input_reader module"""

    def test_reader(self):
        """Parse the TEST_SAMPLE.txt file and ensure the input_dict returns as expected"""

        input_file = 'TEST_SAMPLE.txt'
        input_dict = read_input(input_file)
        self.assertEqual(input_dict['team_count'], 104)
        self.assertEqual(input_dict['rounds'], 5)
        self.assertEqual(input_dict['break_count'], 16)
        self.assertEqual(input_dict['distribution'], 'Gaussian')
        self.assertEqual(input_dict['trials'], 1000)
        self.assertEqual(input_dict['input_round'], 4)

        self.assertEqual(input_dict['standings'][9], 1)
        self.assertEqual(input_dict['standings'][8], 6)
        self.assertEqual(input_dict['standings'][7], 9)
        self.assertEqual(input_dict['standings'][6], 16)
        self.assertEqual(input_dict['standings'][5], 18)
        self.assertEqual(input_dict['standings'][4], 18)
        self.assertEqual(input_dict['standings'][3], 15)
        self.assertEqual(input_dict['standings'][2], 11)
        self.assertEqual(input_dict['standings'][1], 5)
        self.assertEqual(input_dict['standings'][0], 5)


if __name__ == '__main__':
    unittest.main()
