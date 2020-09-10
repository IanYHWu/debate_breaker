"""
Main program for debate breaker. Simulates many tournaments to obtain the break statistics
"""

from collections import Counter
from src import breaker_class, input_reader
import sys


def simulation(input_file):
    """Function to simulate many debate tournaments using input from the read_input function in input_reader"""

    # read in input file contents in a dictionary
    input_dict = input_reader.read_input(input_file)
    team_count = input_dict['team_count']
    rounds = input_dict['rounds']
    break_count = input_dict['break_count']
    distribution = input_dict['distribution']
    trials = input_dict['trials']
    input_round = input_dict['input_round']
    standings = input_dict['standings']

    options = {'std': input_dict['std']}

    print('--------------------------')
    print('DEBATE BREAKER v1.0 \n')
    print('Performing {} simulations for a tournament with {} teams, {} rounds and {} breaking teams')\
        .format(trials, team_count, rounds, break_count)
    if input_round and standings:
        print('Starting from round {} using custom standings \n').format(input_round)
    print('Team Strength Distribution: {}'.format(distribution))
    print('--------------------------')

    # counter objects to hold the cumulative results of single tournaments
    total_results = Counter()
    break_results = Counter()
    final_results = {}
    # simulate debate tournaments
    for trial in range(0, trials):
        if trial % 100 == 0:
            print('Performing trial {} out of {}...'.format(trial, trials))
        # use NewTournament class if no standings included, and RunningTournament if standings included
        if not standings:
            tournament = breaker_class.NewTournament(team_count, rounds, break_count, distribution, options)
        else:
            tournament = breaker_class.RunningTournament(team_count, rounds, break_count,
                                                         distribution, standings, input_round, options)
        break_results += tournament.simulate()[0]
        total_results += tournament.simulate()[1]

    print('Complete!')
    print('--------------------------')
    for result in break_results:
        final_results[result] = round(100*float(break_results[result])/total_results[result], 1)

    print('RESULTS \n')

    straights = 2*rounds
    min_printed = False
    for final_points in final_results:
        while not min_printed:
            print('The chance of breaking on {} points ({}) or below is ~0%')\
                .format(final_points - 1, final_points - 1 - straights)
            min_printed = True
        if final_results[final_points] == 100.0:
            print('The chance of breaking on {} points ({}) or above is ~100%')\
                .format(final_points, final_points - straights)
            break
        print('The chance of breaking on {} points ({}) is {}%')\
            .format(final_points, final_points - straights, final_results[final_points])


if __name__ == '__main__':
    f = sys.argv[1]
    simulation(f)

