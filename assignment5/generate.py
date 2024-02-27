#!/usr/bin/env python3

import time
import numpy as np
import h5py as h5
import os 

file_names = ['A.csv', 'B.csv', 'C.csv', 'D.csv', 'E.csv', 'A.npy', 'B.npy', 'C.npy', 'D.npy', 'E.npy', 'matrix_db.hdf5']
time_save_files = []
file_size = []
# Creates matrix A
## min = 1, max = 9, shape (5000x5000) and 64-bit int data type
matrix_A = np.random.randint(2, 10, size=(5000, 5000), dtype=np.int64)


# Creates matrix B
## min = 100, max = 127, shape (5000x5000) and 8-bit int data type
matrix_B = np.random.randint(100, 128, size=(5000, 5000), dtype=np.int8)


# Creates matrix C
## min = 0.33333, max = 0.33333, shape (5000x5000) and 64-bit int data type
matrix_C = np.full((5000, 5000), 0.33333, dtype=np.float64, order='C')


# Creates matrix D
## min = 1001, max = 1100, shape (10,10) and 16-bit int data type
matrix_D = np.linspace(1001, 1101, 100, dtype=np.int16).reshape(10, 10)


# Creates matrix E
## min = 350.0, max = 350.3, shape (10,10) and 32-bit float data type
matrix_E = np.linspace(350.0, 350.4, 4, dtype=np.float32).reshape(2, 2)


st = time.time()
np.savetxt('A.csv', matrix_A, fmt='%d')
et = time.time()
tt = et - st
time_save_files.append([tt, 'A.csv'])
print('Time to save matrix A: {0}, {1}X{2} matrix of {3}'.format(tt, 5000,5000, 'int64'))



st = time.time()
np.savetxt('B.csv', matrix_B, fmt='%d')
et = time.time()
tt = et - st
time_save_files.append([tt, 'B.csv'])
print('Time to save matrix B: {0}, {1}X{2} matrix of {3}'.format(tt, 5000,5000, 'int8'))



st = time.time()
np.savetxt('C.csv', matrix_C, fmt='%.18e')
et = time.time()
tt = et - st
time_save_files.append([tt, 'C.csv'])
print('Time to save matrix C: {0}, {1}X{2} matrix of {3}'.format(tt, 5000,5000, 'float64'))



st = time.time()
np.savetxt('D.csv', matrix_D, fmt='%d')
et = time.time()
tt = et - st
time_save_files.append([tt, 'D.csv'])
print('Time to save matrix D: {0}, {1}X{2} matrix of {3}'.format(tt, 10,10, 'int16'))



st = time.time()
np.savetxt('E.csv', matrix_E, fmt='%.7e')
et = time.time()
tt = et - st
time_save_files.append([tt, 'E.csv'])
print('Time to save matrix E: {0}, {1}X{2} matrix of {3}'.format(tt, 2,2, 'float32'))



st = time.time()
np.save('A.npy', matrix_A)
et = time.time()
tt = et - st
time_save_files.append([tt, 'A.npy'])
print('Time to save matrix A: {0}, {1}X{2} matrix of {3}'.format(tt, 5000,5000, 'int64'))



st = time.time()
np.save('B.npy', matrix_B)
et = time.time()
tt = et - st
time_save_files.append([tt, 'B.npy'])
print('Time to save matrix B: {0}, {1}X{2} matrix of {3}'.format(tt, 5000,5000, 'int8'))



st = time.time()
np.save('C.npy', matrix_C)
et = time.time()
tt = et - st
time_save_files.append([tt, 'C.npy'])
print('Time to save matrix C: {0}, {1}X{2} matrix of {3}'.format(tt, 5000,5000, 'float64'))



st = time.time()
np.save('D.npy', matrix_D)
et = time.time()
tt = et - st
time_save_files.append([tt, 'D.npy'])
print('Time to save matrix D: {0}, {1}X{2} matrix of {3}'.format(tt, 10,10, 'int16'))



st = time.time()
np.save('E.npy', matrix_E)
et = time.time()
tt = et - st
time_save_files.append([tt, 'E.npy'])
print('Time to save matrix E: {0}, {1}X{2} matrix of {3}'.format(tt, 2,2, 'float32'))


f = h5.File('matrix_db.hdf5', 'w')
G1 = f.create_group("integer_group")
G1.attrs['description'] = 'Various integer type matricies'
st = time.time()
G1.create_dataset("Matrix A", data = matrix_A, compression = 'gzip', chunks = (500,500))
et = time.time()
tt = et - st
time_save_files.append([tt, 'A db'])
print('Time to create database for matrix A: {0}, {1}X{2} matrix of {3}'.format(tt, 5000,5000, 'int64'))



st = time.time()
G1.create_dataset("Matrix B", data = matrix_B, compression = 'gzip', chunks = (1000,1000))
et = time.time()
tt = et - st
time_save_files.append([tt, 'B db'])
print('Time to create database for matrix B: {0}, {1}X{2} matrix of {3}'.format(tt, 5000,5000, 'int8'))

st = time.time()
G1.create_dataset("Matrix D", data = matrix_D)
et = time.time()
tt = et - st
time_save_files.append([tt, 'D db'])
print('Time to create database for matrix D: {0}, {1}X{2} matrix of {3}'.format(tt, 10,10, 'int16'))


G2 = f.create_group("float_group")
G2.attrs['description'] = 'Various float type matricies'
st = time.time()
G2.create_dataset("Matrix C", data = matrix_C, compression = 'gzip')
et = time.time()
tt = et - st
time_save_files.append([tt, 'C db'])
print('Time to create database for matrix C: {0}, {1}X{2} matrix of {3}'.format(tt, 5000,5000, 'float64'))



st = time.time()
G2.create_dataset("Matrix E", data = matrix_E)
et = time.time()
tt = et - st
time_save_files.append([tt, 'E db'])
print('Time to create database for matrix E: {0}, {1}X{2} matrix of {3}'.format(tt, 2,2, 'float32'))


for i in file_names:
    file_size.append([os.path.getsize(i), i])
