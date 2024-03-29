from mpi4py import MPI
import time
import math


# Start timer
start = time.perf_counter()

# Start the MPI process
comm = MPI.COMM_WORLD

# Determine total number of tasks
size = comm.Get_size()

# Determine id of "this" task
rank = comm.Get_rank()


def f(x):
    return x*math.exp(x)

def gauleg(x1, x2, x, w, n):
    EPS = 3.0e-16
    m = (n + 1) // 2
    xm = 0.50 * (x2 + x1)
    xl = 0.50 * (x2 - x1)
    
    for i in range(1, m + 1):
        z = math.cos(math.pi * (i - 0.25) / (n + 0.50))
        while True:
            p1 = 1.0
            p2 = 0.0
            for j in range(1, n + 1):
                p3 = p2
                p2 = p1
                p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j
            
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            z1 = z
            z = z1 - p1 / pp
            
            if abs(z - z1) > EPS:
                continue
            
            x[i - 1] = xm - xl * z
            x[n - i] = xm + xl * z
            w[i - 1] = 2.0 * xl / ((1.0 - z * z) * pp * pp)
            w[n - i] = w[i - 1]
            break

# Example usage:




# --- Master ---
if rank == 0:
    
    # Set parameters (integrate from a to b using n trapezoids)
    n = 20
    x = [0.0] * n
    w = [0.0] * n
    x1, x2 = -1.0, 1.0
    gauleg(x1, x2, x, w, n)

    
    partial = 0.  # partial integral result returned by a Worker
    integral = 0.  # running total of the integral

    # Loop over all tasks waiting for result
    for i in range(1, size):
        comm.send([x,w], dest=i)
        partial = comm.recv(source=i)  # receive result from Worker i
        integral += partial  # accumulate integral
        print(f"Master received value {partial} from process {i}")  # report who sent results

    # Integral complete - write results
    finish = time.perf_counter()
    print(f'The integral is {integral}')
    print(f'Finish in {round(finish - start, 3)} seconds')

# --- Worker ---
else:
    # Print notification including process id
    vals = comm.recv(source = 0)
    x = vals[0]
    w = vals[1]
    
    print(f"Process {rank} starts")
    partial  = w[rank-1]*f(x[rank-1])

    # Send results back to Master (rank = 0)
    comm.send(partial, dest=0)



# Example usage:
# n = 3
# x = [0.0] * n
# w = [0.0] * n
# x1, x2 = -1.0, 1.0
# gauleg(x1, x2, x, w, n)
# print("x =", x)
# print("w =", w)

# sum = 0.0
# for i in range(0,n):
#     sum = sum + w[i]*f(x[i])
# print(f"sum = ",{sum})
# exact = 2/math.exp(1)
# print(f"Relative error =",{abs(sum-exact)/exact})
