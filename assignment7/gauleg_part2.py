from mpi4py import MPI
import time
import math
import pandas as pd
import numpy as np
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

if size > 21:
    print(size)
    raise Exception("Number of processes exceeds the number of quadrature points!")


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
    num_partitions = size - 1
    size_partition = math.floor(20/num_partitions)
    remainder = 20 - (num_partitions*size_partition)
    x_list = [x[i*size_partition:(i+1)*size_partition] for i in range(0,num_partitions,1)]
    stragglers_x = x[(20 - remainder):]
    if len(stragglers_x)!=0:
        for i in stragglers_x:
           x_list[-1].append(i)
    w_list =[w[i*size_partition:(i+1)*size_partition] for i in range(0,num_partitions,1)]
    stragglers_w = w[(20 - remainder):]
    if len(stragglers_w)!=0:
        for i in stragglers_w:
           w_list[-1].append(i)
    # Loop over all tasks waiting for result
    data = {"Integration Result": [0 for i in range(1,len(x_list)+1)], "Percent Error": [0 for i in range(1,len(x_list)+1)], "Run Time": [0 for i in range(1,len(x_list)+1)]}
    index = ["Quadrature Number " + str(i) for i in range(1,len(x_list)+1)]
    for i in range(1,len(x_list)+1):
        comm.send([x_list[i-1],w_list[i-1]], dest=i)
        res = comm.recv(source=i)  # receive result from Worker i
        partial = res[0]
        time_worker = res[1]
        integral += partial
        data["Integration Result"][i-1] = integral
        data["Run Time"][i-1] = time_worker 
        error = ((2/np.exp(1)) - integral)/((2/np.exp(1)))
        data["Percent Error"][i-1] = error                           

    # Integral complete - write results
    finish = time.perf_counter()
    data = pd.DataFrame(data, index = index)
    print(data)
    data.to_csv('part1.txt', sep='\t', index=False)
    # print(f'The integral is {integral}')
    # print(f'Finish in {round(finish - start, 3)} seconds')

# --- Worker ---
else:
    # Print notification including process id
    st = time.time()
    vals = comm.recv(source = 0)
    x = vals[0]
    w = vals[1]
    
    print(f"Process {rank} starts")
    partial = 0
    for i in range(0,len(x)):
        partial  = partial + w[i]*f(x[i])
    et = time.time()
    tt = et - st
    
    # Send results back to Master (rank = 0)
    comm.send([partial, tt], dest=0)



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
