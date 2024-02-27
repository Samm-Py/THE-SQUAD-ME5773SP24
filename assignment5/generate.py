#!/usr/bin/env python3

import time
import numpy as np


# Creates matrix A
## min = 1, max = 9, shape (5000x5000) and 64-bit int data type
matrix_A = np.random.randint(2, 9, size=(5000, 5000), dtype=np.int64)


# Creates matrix B
## min = 100, max = 127, shape (5000x5000) and 8-bit int data type
matrix_B = np.random.randint(100, 127, size=(5000, 5000), dtype=np.uint8)


# Creates matrix C
## min = 0.33333, max = 0.33333, shape (5000x5000) and 64-bit int data type
matrix_C = np.full((5000, 5000), 0.33333, dtype=np.float64, order='C')


# Creates matrix D
## min = 1001, max = 1100, shape (10,10) and 16-bit int data type
matrix_D = np.linspace(1001, 1100, 100, dtype=np.int16).reshape(10, 10)


# Creates matrix E
## min = 350.0, max = 350.3, shape (10,10) and 32-bit float data type
matrix_E = np.linspace(350.0, 350.3, 4, dtype=np.float32).reshape(2, 2)


