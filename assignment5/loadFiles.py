#!/usr/bin/env python3

import time
import numpy as np
import h5py as h5
import os 

file_names = ['A.csv', 'B.csv', 'C.csv', 'D.csv', 'E.csv', 'A.npy', 'B.npy', 'C.npy', 'D.npy', 'E.npy', 'matrix_db.hdf5']
time_load_files = []
file_size = []

for i in range(0,5):
    st = time.time()
    Mat = np.loadtxt(file_names[i])
    et = time.time()
    tt = et - st
    time_load_files.append([tt,file_names[i]])
    print('Time to load {0}: {1}'.format(file_names[i], tt))

for i in range(5,10):
    st = time.time()
    Mat = np.load(file_names[i])
    et = time.time()
    tt = et - st
    time_load_files.append([tt,file_names[i]])
    print('Time to load {0}: {1}'.format(file_names[i], tt))
    
f = h5.File('matrix_db.hdf5', 'r')
groups = list(f.keys())

for i in groups:
    
    db = f[i]
    databases = db.keys()
    for j in databases:
        st = time.time()
        Mat = db[j]
        et = time.time()
        tt = et - st
        time_load_files.append([tt, j])
        print('Time to load {0}: {1}'.format(i,tt))




