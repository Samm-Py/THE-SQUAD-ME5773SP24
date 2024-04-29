import module as md
import numpy as np
import time




A =  np.array([[   -5.86,   3.99,  -5.93,  -2.82,   7.69, ],
               [    3.99,   4.46,   2.58,   4.42,   4.61,],
               [   -5.93,   2.58,  -8.52,   8.57,   7.69,],
               [   -2.82,   4.42,   8.57,   3.72,   8.07,],
               [    7.69,   4.61,   7.69,   8.07,   9.83,]])

b = np.array([[   1.32,  -6.33,  -8.77,],
              [   2.22,   1.69,  -8.33,],
              [   0.12,  -1.56,   9.54,],
              [  -6.41,  -9.49,   9.56,],
              [   6.33,  -3.67,   7.48,]])





print(A)
print(b)


t_start = time.time()
res = md.mkl_solver_symm( A,b )
t_end = time.time()

print(A)
print(b)


print('Time spent: {0:.6f} s'.format(t_end-t_start))
print(A@b)


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


t_start = time.time()
res = md.mkl_solver_symm( A,b )
t_end = time.time()

print(A)
print(b)