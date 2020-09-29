"""
Classes for debate breaker. Includes classes Team, Room, NewTournament and RunningTournament, which enables
the simulation of a single debate tournament.
"""
import random
import numpy as np
from collections import Counter


class Team:
    """A single participating team.

    Attributes:
         points: the number of points accumulated by the team
         strength: a team strength score between 0 and 1. Assigned at initialisation
    """

    def __init__(self, distribution, options, points=0):
        """Initialise Team class. Strength is initialised randomly from the specified distribution"""
        self.points = points
        if distribution == 'Gaussian':
            self.strength = self._set_gaussian_strength(options['std'])
        elif distribution == 'Uniform':
            self.strength = self._set_uniform_strength()

    def get_points(self):
        """Get team points points"""
        return self.points

    def set_points(self, points):
        """Set team points"""

        self.points = points

    def get_strength(self):
        """Get strength"""
        return self.strength

    def increment_points(self, incr):
        """Increment points by amount incr"""
        self.points += incr

    @staticmethod
    def _set_gaussian_strength(std):
        """Set the team strength based on a Gaussian distribution"""
        mean = 0.5
        accept = False
        strength = 0
        # resample if strength falls outside 0 < strength < 1
        while not accept:
            strength = np.random.normal(mean, std)
            if 0 < strength < 1:
                accept = True
        return strength

    @staticmethod
    def _set_uniform_strength():
        """Set the team strength based on a uniform distribution"""
        strength = random.uniform(0, 1)
        return strength


class Room:
    """A single debate room, consisting of Teams

        Attributes:
             room: a list containing the Teams assigned to the room
        """

    def __init__(self, room_list):
        """Initialise the Room class from room_list, a list of Teams"""
        self.room = room_list

    def get_teams(self):
        """Get room_list"""
        return self.room

    def random_debate(self):
        """Simulate a debate in the Room, with results determined completely randomly"""
        result = random.sample(range(0, 4), 4)
        for ind, team in enumerate(self.get_teams()):
            team.increment_points(result[ind])

    def debate(self):
        """Simulate a debate in the Room, with results determined by strength.
         Uses the _call private method to determine rankings"""
        strength_list = []
        for team in self.get_teams():
            strength_list.append(team.get_strength())
        self._call(strength_list)

    def _call(self, strength_list):
        """Generate call (i.e. determines the rankings) of a debate.
        The call is influenced by the strength of the Teams"""

        # normalise the strengths
        strength_sum = sum(strength_list)
        summed_strength_list = [strength / strength_sum for strength in strength_list]
        # generate a number line between 0 and 1 from the normalised strengths
        # each team holds a certain region in the number line, with length reflecting their comparative strengths
        for i in range(0, len(strength_list) - 1):
            summed_strength_list[i + 1] = summed_strength_list[i] + summed_strength_list[i + 1]
        selected = []

        counter = 3  # the number of points currently up for grabs
        while counter > 0:
            # draw sample P from a uniform distribution
            P = random.uniform(0, 1)
            for ind, strength in enumerate(summed_strength_list):
                # assign points to the team whose region P lands in
                if P <= strength:
                    # if P lands in a region belonging to a team that has already been assigned points, redraw P
                    if ind not in selected:
                        selected.append(ind)
                        self.get_teams()[ind].increment_points(counter)
                        counter -= 1
                        break
                    else:
                        break


class NewTournament:
    """A tournament starting from round 1. Consists of many Teams that will be assigned Rooms

    Attributes:
        tournament: the list of participating Teams. Created at initialisation
        team_count: the total number of Teams
        break_count: the number of breaking teams
        rounds: the total number of rounds in the tournament
        round: the current round. Starts at 1
        distribution: the distribution of team strengths
    """

    def __init__(self, team_count, rounds, break_count, distribution, options):
        """Initialise the NewTournament"""
        self.tournament = []
        self.team_count = team_count
        self.break_count = break_count
        self.rounds = rounds
        self.round = 1
        self.distribution = distribution

        # generate teams
        if self.team_count % 4 != 0:
            raise Exception('Team count is not a multiple of 4')
        for team in range(0, self.team_count):
            self.tournament.append(Team(self.distribution, options))

    def get_round(self):
        """Get the current round"""
        return self.round

    def get_break_count(self):
        """Get the break_count"""
        return self.break_count

    def _quick_sort(self, s):  # s here is the tournament list i.e. self.tournament
        """Sort the teams in a tournament by the number of points they possess.
        Employs a recursive version of Quicksort. Returns a sorted list of Team objects"""

        # base case
        if len(s) <= 1:
            return s
        else:
            # randomly assign a pivot
            pivot = s[random.randint(0, len(s) - 1)].get_points()
            smaller = []
            equal = []
            bigger = []

            # split the list s based on the pivot
            for team in s:
                if team.get_points() < pivot:
                    smaller.append(team)
                elif team.get_points() == pivot:
                    equal.append(team)
                else:
                    bigger.append(team)

        # recursively call the function
        return self._quick_sort(smaller) + equal + self._quick_sort(bigger)

    def _hold_round(self):
        """Simulate a single debate round. Assigns teams to their debate rooms, holds the debate,
        and then returns teams to the tournament. Increments the round.
        """

        counter = 0
        while counter < self.team_count:
            counter += 4
            room_list = []
            # remove the first four Teams from the tournament list, and assign them to a room
            for i in range(0, 4):
                room_list.append(self.tournament.pop(0))
            room = Room(room_list)
            # hold the debate
            if self.distribution == 'Random':
                room.random_debate()
            elif self.distribution == 'Gaussian' or self.distribution == 'Uniform':
                room.debate()
            # return the teams to the tournament list
            for team in room.get_teams():
                self.tournament.append(team)

        self.round += 1

    def _get_results(self):
        """Extract the final results of a tournament. Returns Counter objects (dictionary-like)
        containing the results of the breaking teams, as well as the overall results"""

        break_count = self.get_break_count()
        points_list = []
        # extract the final number of points per team
        for team in self.tournament:
            points_list.append(team.get_points())

        # get the list of breaking teams and then generate Counter objects
        break_list = points_list[-break_count:]
        break_results = Counter(break_list)  # results of breaking teams
        total_results = Counter(points_list)  # overall results

        return break_results, total_results

    def simulate(self):
        """Simulate a entire debate tournament. Returns the final results"""

        # simulate a round
        while self.get_round() <= self.rounds:
            self._hold_round()  # draw and then hold a single round of debates
            self.tournament = self._quick_sort(self.tournament)  # sort the teams by points after the round
        # extract the final results
        results = self._get_results()
        return results


class RunningTournament(NewTournament):
    """A tournament starting from an arbitrary round, accounting for the existing standings.
     Consists of many Teams that will be assigned Rooms. Inherits from NewTournament.

        Attributes:
            tournament: the list of participating Teams. Created at initialisation
            team_count: the total number of Teams
            break_count: the number of breaking teams
            rounds: the total number of rounds in the tournament
            round: the current round. Starts at input_round
            distribution: the distribution of team strengths
            standings: a dictionary consisting of the number of teams on a given number of points as of the input_round
        """

    def __init__(self, team_count, rounds, break_count, distribution, standings, input_round, options):
        """Initialise the RunningTournament"""

        NewTournament.__init__(self, team_count, rounds, break_count, distribution, options)

        self.standings = standings
        self.round = input_round
        self.tournament = []
        # extract a list of points from the standings dict
        points_list = sorted(list(Counter(self.standings).elements()))

        # initialise the tournament list with Teams based on the standings
        if self.team_count % 4 != 0:
            raise Exception('Team count is not a multiple of 4')
        if len(points_list) != team_count:
            raise Exception('Standings input error: incorrect number of teams')
        for team in range(0, self.team_count):
            self.tournament.append(Team(self.distribution, options, points=points_list[team]))

