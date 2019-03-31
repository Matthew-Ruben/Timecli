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
    parser.add_argument('time1',
                        help='The time to add to or subtract from',
                        type=str,
                        default='1:10')

    # Add operator argument
    parser.add_argument('operator',
                        help='Whether to add or subtract the operands',
                        type=str,
                        choices=['+', '-'])

    # Add time2 argument
    parser.add_argument('time2',
                        help='The time to add or subtract from time1',
                        type=str,
                        default='3:30')

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
    time1: str
    time2: str
    operator: str
    verbose: bool

    def __init__(self):
        self.time1, self.operator, self.time2, self.verbose = get_arguments()
        self.parse()

    def parse(self):
        hour1, min1 = self.time1.split(':', 2)
        hour2, min2 = self.time2.split(':', 2)
        if len(min2) == 4:
            ampm = min2[2:]
            min2 = min2[:-2]
            print(min2)
            print(ampm)
        if self.operator == '-':
            hours = int(hour1) - int(hour2)
            mins = int(min1) - int(min2)
            if mins < 0:
                temp = abs(mins)
                hours -= 1
                mins = 60 - temp

        print(f'{hours}:{mins}')


class Time:
    hour: int
    minute: int
    ampm: str

    def __init__(self, string):
        self.hour = string[0:2]
        self.minute = string[3:5]
        if len(string) > 5:
            self.ampm = string[5:]
        else:
            self.ampm = None

    def __str__(self):
        if self.ampm:
            return f'{self.hour}:{self.minute}{self.ampm}'
        else:
            return f'{self.hour}:{self.minute}'



def main():
    Timecli()

if __name__ == '__main__':
    main()
