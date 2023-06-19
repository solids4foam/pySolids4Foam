# pySolids4Foam
This repository contains Python scripts for creating finite volume discretisations for solid mechanics and fluid-solid interaction, similar to in solids4foam, but using PETSc directly for the linear system.

# Installation
Requirements:
- mpi4py
- numpy
- petsc4py
I installed these using conda but you it can be done in others, like using pip.

# Running
The scripts can be run in serial, e.g.
- `python finiteDifference2dPETSc.py`
or in parallel, e.g.
- `mpiexec -n 4 python finiteDifference2dPETSc.py`

# Contact
philip.cardiff@ucd.ie