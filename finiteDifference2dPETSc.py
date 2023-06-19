import sys
import time
import petsc4py
from petsc4py import PETSc

# Function to convert row (r) to 2-D grid indices (i, j)
def index_to_grid(r):
    """Convert a row number into a grid point."""
    return (r // n, r % n)

# User parameters
n = 1000 # number of rows
nnz = 5 # estimate of the number of non-zeros per row
h = 1.0 / (n + 1) # mesh spacing

#
#  Main
#

# Pass command-line arguments to PETSc
petsc4py.init(sys.argv)

# Read PETSc options file
OptDB = PETSc.Options()

# Create matrix
print('Creating the matrix')
A = PETSc.Mat()
A.create(comm=PETSc.COMM_WORLD)

# Set matrix size
A.setSizes((n * n, n * n))

# Set global decomposition
A.setSizes(((PETSc.DECIDE, n * n), (PETSc.DECIDE, n * n)))

# Set matrix format
A.setType(PETSc.Mat.Type.AIJ)

# Allow matrix options set from options file
A.setFromOptions()

# Estimate the number of nonzeros to be expected on each row
A.setPreallocationNNZ(nnz)

# Insert coefficients]
start_time = time.time()
print('Insert the coefficients')
rstart, rend = A.getOwnershipRange()
for row in range(rstart, rend):
    i, j = index_to_grid(row)
    A[row, row] = 4.0 / h**2
    if i > 0:
        column = row - n
        A[row, column] = -1.0 / h**2
    if i < n - 1:
        column = row + n
        A[row, column] = -1.0 / h**2
    if j > 0:
        column = row - 1
        A[row, column] = -1.0 / h**2
    if j < n - 1:
        column = row + 1
        A[row, column] = -1.0 / h**2

# Perform global syncing
print('Global matrix operations')
A.assemblyBegin()
A.assemblyEnd()
print("--- Matrix assembly: %s seconds ---" % (time.time() - start_time))

# Create solution and source vectors
print('Create source and solution vector')
x, b = A.createVecs()
b.set(1.0)


# Create linear solver
print('Create linear solver')
ksp = PETSc.KSP()
ksp.create(comm=A.getComm())
ksp.setType(PETSc.KSP.Type.CG)
ksp.getPC().setType(PETSc.PC.Type.GAMG)
ksp.setOperators(A)
ksp.setFromOptions()

# Solver linear system
print('Solve linear system')
start_time = time.time()
ksp.solve(b, x)
print("--- System solution: %s seconds ---" % (time.time() - start_time))

# Allow solution to be viewed
x.viewFromOptions('-view_sol')

print('End')
