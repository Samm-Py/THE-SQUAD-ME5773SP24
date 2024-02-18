import numpy as np
import math as math
import numexpr
import time as time



exp = 9
N = 10**exp
deltax = 2/N


F1 = 0
st = time.time()
for i in range(0,N):
    if i%10**8 == 0:
        print(i)
    xi = i*deltax - 1
    f_xi = math.sqrt(4 - 4*xi**2)
    F1 = F1 + f_xi*deltax
et = time.time()
tt = et - st
print('Time to compute integral: {:.6f}'.format(tt))
print('\n')
print('The value of the integral is: {:.16f}'.format(F1))
print('\n')

st = time.time()
i_vec = np.arange(0,10**exp, 1)
x_vec = (2*i_vec/N) - 1
F_vec = np.sqrt(4 - 4*x_vec**2)*deltax
F2 = np.sum(F_vec)
et = time.time()
tt = et - st
print('Time to compute integral using vectorized values: {:.6f}'.format(tt))
print('\n')

st = time.time()
i_vec = np.arange(0,10**exp, 1)
x_vec = numexpr.evaluate('(2*i_vec/N) - 1')
F_vec = np.sqrt(numexpr.evaluate('(4 - 4*x_vec**2)*deltax'))
F2 = numexpr.evaluate('sum(F_vec)')
et = time.time()
tt = et - st
print('Time to compute integral using numexpr values: {:.6f}'.format(tt))