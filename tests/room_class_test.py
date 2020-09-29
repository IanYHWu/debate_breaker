import unittest
from src.breaker_class import Room
from src.breaker_class import Team


class RoomTest(unittest.TestCase):
    """Test the Room class in breaker_class module"""

    def set_up(self):
        """Initialise a Room"""
        self.room = Room([Team('Gaussian', options={'std': 0.25}), Team('Gaussian', options={'std': 0.25}),
                          Team('Gaussian', options={'std': 0.25}), Team('Gaussian', options={'std': 0.25})])

    def test_random_debate(self):
        """Test random_debate
        Ensure that all teams are assigned a unique score in the room after a random_debate"""
        self.set_up()
        self.room.random_debate()
        points_list = []
        for team in self.room.room:
            points = team.get_points()
            self.assertNotIn(points, points_list)
            points_list.append(points)

    def test_debate(self):
        """Test debate
        Ensure that all teams are assigned a unique score in the room after a debate"""
        self.set_up()
        self.room.debate()
        points_list = []
        for team in self.room.room:
            points = team.get_points()
            self.assertNotIn(points, points_list)
            points_list.append(points)


if __name__ == '__main__':
    unittest.main()
