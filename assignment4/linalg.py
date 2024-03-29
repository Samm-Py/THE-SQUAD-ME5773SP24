#!/usr/bin/env python3


import numpy as np
import time as time


N = 10000
print("N =",N)


start_time = time.time()
K = np.zeros((N, N)) # Define matrix K
for i in range(N):
    for j in range(N):
        if j == i:
            K[i, j] = 2
        elif j == i + 1:
            K[i, j] = -1
        elif j == i - 1:
            K[i, j] = -1

K[N-1, N-1] = 1

print("K =",K)

f = np.zeros(N) # Define vector f
f[-1] = 1 / N

f_stacked = f.reshape(-1, 1) # Reshape f into a stacked vector

print("f =",f_stacked)

elapsed_time = time.time() - start_time # Calculate elapsed time of K and f

print("K and f elapsed time =","{:.9f}".format(elapsed_time))

start_time_u = time.time()

u = np.linalg.solve(K, f_stacked)

elapsed_time = time.time() - start_time_u # Calculate elapsed time of uN

print("uN elapsed time =","{:.9f}".format(elapsed_time))

print("uN = ", u[-1])

elapsed_time = time.time() - start_time # Calculate total elapsed time

print("Total elapsed time =","{:.9f}".format(elapsed_time))

