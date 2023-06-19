"""
         _____     _ _   _     ___ _____                 | pySolids4Foam
 ___ _ _|   __|___| |_|_| |___| | |   __|___ ___ _____   | Python Version: 3.10
| . | | |__   | . | | | . |_ -|_  |   __| . | .'|     |  | Code Version: 0.0
|  _|_  |_____|___|_|_|___|___| |_|__|  |___|__,|_|_|_|  | License: GPLv3
|_| |___|                                            

Description
    Function arg_parse returns arguments and is called from the application.
    While parsing arguments, the banner and job info are printed.
"""
__author__ = 'Ivan Batistić & Philip Cardiff'
__email__ = 'ibatistic@fsb.hr, philip.cardiff@ucd.ie'
__all__ = ['arg_parser']

import argparse
import os
from collections import namedtuple
from datetime import datetime

import __main__

BANNER = '''\
"""
         _____     _ _   _     ___ _____                 | pySolids4Foam\n\
 ___ _ _|   __|___| |_|_| |___| | |   __|___ ___ _____   | Python Version: 3.10\n\
| . | | |__   | . | | | . |_ -|_  |   __| . | .'|     |  | Code Version: 0.0\n\
|  _|_  |_____|___|_|_|___|___| |_|__|  |___|__,|_|_|_|  | License: GPLv3\n\
|_| |___|\n\
'''

def arg_parser() -> argparse.ArgumentParser:
    """ Parse arguments using argparse module"""

    _description = ''
    try:
        _description = __main__.__doc__.split('Description')[1]
    except IndexError:
        pass

    parser = argparse.ArgumentParser(description=_description)

    # Standard arguments
    parser.add_argument('-d',
                        '--debug',
                        action='store_true',
                        help='Enable debug mode')

    # Mutually exlusive arguments
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v', '--verbose', action='store_true')
    group.add_argument('-q', '--quiet', action='store_true')

    # Write banner
    print(BANNER)

    # Write job info
    print_job_info()

    return parser


def print_job_info() -> None:
    jobInfo = namedtuple('jobInfo', 'exec date time pid case')

    now = datetime.now()

    info = jobInfo(__main__.__file__.split('/')[-1],
                   f'{now:%d %B %Y}',
                   f'{now:%H:%M:%S}',
                   os.getpid(),
                   os.getcwd())

    # Print job info
    print(f'Exec   :{info.exec}')
    print(f'Date   :{info.date}')
    print(f'Time   :{info.time}')
    print(f'PID    :{info.pid}')
    print(f'Case   :{info.case}')
    print('-' * 80)

    return None
