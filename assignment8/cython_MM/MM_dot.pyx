# cython: wraparound=False
# cython: boundscheck=False
# cython: profile=True
# cython: initializedcheck=False
import cython
cimport cython
import  numpy as np
cimport numpy as np
from cython.parallel import prange


@cython.boundscheck(False)
@cython.nonecheck(False)
@cython.wraparound(False)

def mat_mul(np.ndarray[np.float64_t, ndim=2] A, np.ndarray[np.float64_t, ndim=2] B):
   
   cdef int s1 = A.shape[0]
   cdef int s2 = B.shape[1]
   cdef double [:,:] res = np.empty((s1, s2))
   cdef double temp = 0
   
   res = np.dot(A,B)
   
   
   return res


