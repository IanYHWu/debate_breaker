import unittest
from src.breaker_class import Team


class TeamTest(unittest.TestCase):
    """Test the Team class from breaker_class module"""

    def set_up(self):
        """Initialise teams using all three different strength distributions"""
        self.team_gaussian = Team('Gaussian', options={'std': 0.25})
        self.team_uniform = Team('Uniform', options={'std': 0.25})
        self.team_random = Team('Random', options={'std': 0.25})

    def assertBetween(self, val, minimum, maximum):
        """Check that a value falls between two other values"""
        self.assertGreaterEqual(val, minimum)
        self.assertLessEqual(val, maximum)

    def test_strength_assignment(self):
        """Check that strengths lie between 0 and 1"""
        for trial in range(0, 100):
            self.set_up()
            self.assertBetween(self.team_gaussian.get_points(), 0, 1)
            self.assertBetween(self.team_random.get_points(), 0, 1)
            self.assertBetween(self.team_uniform.get_points(), 0, 1)

    def test_increment_points(self):
        """Test increment_points method
        Check that points are incremented correctly"""
        self.set_up()
        self.team_gaussian.increment_points(3)
        self.assertEqual(self.team_gaussian.get_points(), 3)


if __name__ == '__main__':
    unittest.main()
