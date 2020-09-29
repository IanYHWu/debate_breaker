import unittest
from src.breaker_class import Team
from src.breaker_class import NewTournament


class TournamentTest(unittest.TestCase):
    """Test the NewTournament class in breaker_class.py"""

    def set_up(self):
        """Set up a simple tournament"""
        self.tournament = NewTournament(8, 3, 4, 'gaussian', options={})
        self.tournament.tournament = [Team('Gaussian', options={'std': 0.25}), Team('Gaussian', options={'std': 0.25}),
                                      Team('Gaussian', options={'std': 0.25}), Team('Gaussian', options={'std': 0.25}),
                                      Team('Gaussian', options={'std': 0.25}), Team('Gaussian', options={'std': 0.25}),
                                      Team('Gaussian', options={'std': 0.25}), Team('Gaussian', options={'std': 0.25})]
        points = 7
        for team in self.tournament.tournament:
            team.set_points(points)
            points -= 1

    def test__quick_sort(self):
        """Test _quick_sort.
        Check that the tournament list is sorted properly given set_up yields an out-of-order list"""
        self.set_up()
        self.sort_results = self.tournament._quick_sort(self.tournament.tournament)
        counter = 0
        for team in self.sort_results:
            self.assertEqual(counter, team.get_points())
            counter += 1

    def test__get_results(self):
        """Test _get_results.
        Check that the returned Counter objects are correct, given known team points and break count"""
        self.set_up()
        self.tournament.tournament = self.tournament._quick_sort(self.tournament.tournament)
        break_results, total_results = self.tournament._get_results()
        break_points = [7, 6, 5, 4]
        for key in break_results:
            self.assertIn(key, break_points)
            break_points = [i for i in break_points if i != key]
        total_points = [i for i in range(0, 8)]
        for key in total_results:
            self.assertIn(key, total_points)
            total_points = [i for i in total_points if i != key]


if __name__ == '__main__':
    unittest.main()
