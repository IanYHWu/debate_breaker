# Debate Breaker

A Python program to predict the break at BP debating tournaments

# Introduction

The number of points required to break at a debating tournament is of much interest to
its participants, as it provides a clear target for teams to aim for, and provides
an indication for how well a particular team is doing at any given point. The exact 
placement of the break is highly variable, and depends on the total number of teams, number
of rounds, as well as the number of breaking teams.

By simulating a large number of tournaments, this program gives an estimate of the likelihood
of breaking on a given number of points. In addition to simulating a tournament from scratch,
this program can also begin simulation at any given point in the tournament, and thus provide
an improved estimate of the break by accounting for the current distribution of points.

In order to more accurately reflect real tournament conditions, users may specify a particular
distribution of team strengths. Teams with a higher strength will tend to win debates more often
against teams with lower strengths. 


# Installation

Clone into directory using: 

```git clone https://github.com/HerrHruby/debate_breaker.git```

Alternatively, install with pip using:

```pip install -i https://test.pypi.org/simple/ debate-breaker-HerrHruby==1.0.0```

The package is currently hosted on TestPyPI. I will migrate this to PyPI once it is 
properly published.


# Usage

The Python files are located in the ```src``` folder. The main program is run 
from the command line using ```run_breaker.py [INPUT_FILE.txt]```, where ```[INPUT_FILE.txt]``` is a text file 
containing the input parameters. These include:

    TEAM COUNT: the total number of teams in the tournament
    ROUNDS: the total number of in-rounds
    BREAK COUNT: the total number of breaking teams
    DISTRIBUTION: the desired team strength distribution. Options include 
    'Random', 'Gaussian' and 'Uniform' (default = 'Random')
    TRIALS: number of simulations (default = 1000)
    
For simulations beginning midway through a tournament, two additional input parameters 
are needed:

    INPUT ROUND: the next round to be simulated
    STANDINGS: the current standings
    [points] [number of teams] 
    end

See the ```samples``` folder for examples of input files. See the documentation
for more detailed descriptions of the program.


