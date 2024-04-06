import MM as MM
import MM_dot as MM_dot
import numpy as np
import time

A = np.ones((3,3),dtype = 'float64')
B = np.ones((3,3),dtype = 'float64')

time_cython_array = []
time_np_array = []
time_cynp_array = []



for i in range(0,100):
    st = time.time()
    res = MM.mat_mul(A,B)
    et = time.time()
    tt_cython = et - st
    
    st = time.time()
    res = np.dot(A,B)
    et = time.time()
    tt_np = et - st
    
    # st = time.time()
    # res = MM_dot.mat_mul(A,B)
    # et = time.time()
    # tt_cython_np = et - st
    
    time_np_array.append(tt_np)
    time_cython_array.append(tt_cython)
    # time_cynp_array.append(tt_cython_np)

avg_time_np = sum(time_np_array)/len(time_np_array)
avg_time_cython = sum(time_cython_array)/len(time_cython_array)
# avg_time_cynp = sum(time_cynp_array)/len(time_cynp_array)
print('Time Cython: {}'.format(avg_time_cython))

print('Time Numpy: {}'.format(avg_time_np))


print('Speed Up: {}'.format(avg_time_np/avg_time_cython))

# print('Speed Up: {}'.format(avg_time_np/avg_time_cynp))