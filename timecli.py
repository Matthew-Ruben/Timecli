# ----------------------------------------------------------------------
# Name:        Timecli
# Purpose:     Easily add and subtract times
#
# Author:      Matthew Ruben
# Date:        3/30/2019
# ----------------------------------------------------------------------
"""
Perform math on times
"""
import argparse


def get_arguments():
    """
    Parse and validate the command line arguments
    :return: tuple containing:
             the first time (string),
             operator (string),
             the second time (string),
             and the verbose option (boolean)
    """
    parser = argparse.ArgumentParser()
    # Add time1 argument
    parser.add_argument(name='time1',
                        help='The time to add to or subtract from',
                        type=str,
                        required=True,)

    # Add operator argument
    parser.add_argument(name='operator',
                        help='Whether to add or subtract the operands',
                        type=str,
                        required=True,
                        choices=['+', '-'])

    # Add time2 argument
    parser.add_argument(name='time2',
                        help='The time to add or subtract from time1',
                        type=str,
                        required=True)

    # Add verbose option
    parser.add_argument('-v', '--verbose',
                        help='Print all information?',
                        action='store_true')

    arguments = parser.parse_args()
    time1 = arguments.time1
    time2 = arguments.time2
    operator = arguments.operator
    verbose = arguments.verbose

    return time1, operator, time2, verbose





class Timecli:
    """
    Class that implements a command line application that lets users
    add and subtract times
    """

    def main(self):

    def __init__(self, time1, operator, time2, verbose):
        self.time1 = time1
        self.operator = operator
        self.time2 = time2
        self.verbose = verbose





