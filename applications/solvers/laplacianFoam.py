"""
         _____     _ _   _     ___ _____                 | pySolids4Foam
 ___ _ _|   __|___| |_|_| |___| | |   __|___ ___ _____   | Python Version: 3.10
| . | | |__   | . | | | . |_ -|_  |   __| . | .'|     |  | Code Version: 0.0
|  _|_  |_____|___|_|_|___|___| |_|__|  |___|__,|_|_|_|  | License: GPLv3
|_| |___|                                            

Description
    Steady-state Laplace's equation solver
"""
__author__ = 'Ivan Batistić & Philip Cardiff'
__email__  = 'ibatistic@fsb.hr, philip.cardiff@ucd.ie'

import time as timeModule
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../.")
from src.finiteVolume.fvMesh import fvMesh
from src.foam.argList import arg_parser
from src.finiteVolume.cfdTools import solutionControl

# Execution start time, used to measured elapsed clock time
exec_start_time = timeModule.perf_counter()

# Get command line arguments
args = arg_parser().parse_args()

mesh = fvMesh()
solControl = solutionControl()

while(solControl.loop()):

    print(f'Time = {solControl.time()} \n')

    '''
        Assemble and solve system of equations
    '''

    print(f'Execution time = '
          f'{timeModule.perf_counter() - exec_start_time:.2f} s \n')

print('End\n')