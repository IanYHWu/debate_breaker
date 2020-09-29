"""
File containing the input_reader function, for parsing input files
"""


def read_input(FILE):
    """Read in a sample input file and returns a dictionary containing the inputs to be used by the main program"""

    input_dict = {'team_count': None,
                  'rounds': None,
                  'break_count': None,
                  'distribution': 'Random',
                  'trials': 1000,
                  'standings': {},  # nested dictionary for standings - standings[points] = no. of teams
                  'input_round': None,
                  'std': 0.25}

    with open(FILE, 'r') as lines:
        for line in lines:
            if 'TEAM COUNT' in line:
                input_dict['team_count'] = int(line.split(':')[1])
            elif 'ROUNDS' in line:
                input_dict['rounds'] = int(line.split(':')[1])
            elif 'BREAK COUNT' in line:
                input_dict['break_count'] = int(line.split(':')[1])
            elif 'DISTRIBUTION' in line:
                input_dict['distribution'] = line.split(':')[1].strip()
            elif 'TRIALS' in line:
                input_dict['trials'] = int(line.split(':')[1])
            elif 'INPUT ROUND' in line:
                input_dict['input_round'] = int(line.split(':')[1])
            elif 'STD' in line:
                input_dict['std'] = int(line.split(':')[1])
            # read in lines after 'STANDINGS' until 'end' as input round standings
            elif 'STANDINGS' in line:
                for line in lines:
                    if 'end' in line:
                        break
                    else:
                        input_dict['standings'][int(line.split()[0])] = int(line.split()[1])
            elif 'end' or '' in line:
                pass
            else:
                raise Exception('Unknown input {}'.format(line))

    if not input_dict['team_count'] or not input_dict['break_count'] or not input_dict['rounds']:
        raise Exception('Missing input data. All input files must contain TEAM COUNT, ROUNDS, and BREAK COUNT')
    if input_dict['input_round'] and not input_dict['standings']:
        raise Exception('If input round is specified, include custom standings')
    if input_dict['standings'] and not input_dict['input_round']:
        raise Exception('If custom standings specified, include input round')

    return input_dict
