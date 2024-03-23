# =====================================================================================
# This file defines a system of Finite Element Equations for a simple spring system.
# 
# The purpose of this is to provide a base file that ME5773 students can use to apply
# the concepts of parallelization with Python's multiprocessing module.
#
# Author: Mauricio Aristizabal, PhD
# Last modified: 03/19/2024
#
# =====================================================================================

# =====================================================================================
# Required Libraries
import numpy as np
import scipy as sp # Install scipy using "conda install scipy"
import time
import sys
import multiprocessing as mproc
from multiprocessing import shared_memory, Process, Lock, Pool
# =====================================================================================


def define_global_variables():
  global Kg
  global fg
  global Ne
  global Ndof
  global k_list
  global chunks
  global num_workers
  
  Ndof = 100000
  Ne   = Ndof-1 # number of elements.
  num_workers = 1
  print('Number of Degrees of freedom: {0}'.format(Ndof))
  
  # List of elemental stiffness values.
  #
  # This should be created such that each element 
  # may have a different stiffness value.
  chunks = []
  k_list  = [1]*Ne
  Kg = np.zeros((Ndof,Ndof), dtype = 'int8')
  fg = np.zeros((Ndof,))
  





def assemble(args):
      """
      DESCRIPTION: Assemble an element's system matrix and rhs into a global 
                   system of equations for 1D Finite Element problem.
                   
                   This assembly function only supports linear elastic problems
                   of springs assembled in the form:
                  
              x-^^-x-^^-x-^^-x...x-^^-x-^^-x-^^-x

      
      INPUTS:
          -e: (integer) Element index.
          -Ke: (Float array, Shape: (2,2) ) Elemental stiffness matrix.
          -fe: (Float array, Shape: (2,) )  Elemental force vector.
          -Kg: (Float array, Shape: (Ndof,Ndof) ) Global stiffness matrix.
          -fg: (Float array, Shape: (Ndof,) )     Global force vector.
      
      OUTPUTS:
          Nothing, global inputs are modified.

      """
      shr_name = args[0] 
      elements = args[1]

      
      Ke = np.array([[ 1,-1],
                             [-1, 1]])
     # Ke = k_list[e] * np.array([[ 1,-1],
                             #[-1, 1]])
      fe = np.array([0.0,
                 0.0])
      existing_shm = shared_memory.SharedMemory(name=shr_name)
      np_array = np.frombuffer(existing_shm.buf, dtype=np.int8).reshape(Ndof,Ndof,)

      for e in range(0,len(elements)-1):
          for j in range(2):
              for k in range(2):
                  np_array[elements[e]+j,elements[e]+k] = np_array[elements[e]+j,elements[e]+k] + Ke[j,k]

      del np_array
      existing_shm.close()



def create_shared_block():

    a = np.zeros(shape=(Ndof, Ndof), dtype=np.int8)  # Start with an existing NumPy array

    shm = shared_memory.SharedMemory(create=True, size=a.nbytes)
    # # Now create a NumPy array backed by shared memory
    np_array = np.ndarray(a.shape, dtype=np.int8, buffer=shm.buf)
    np_array[:] = a[:]  # Copy the original data into shared memory
    return shm, np_array


def elasticFEProblem( Ndof, Ne1, Ne2, k_list ):
    """
    DESCRIPTION: This function assembles the global stiffness matrix for a sequence 
                 of spring elements, aranged in the following manner:
                
            x-^^-x-^^-x-^^-x...x-^^-x-^^-x-^^-x

    INPUTS:
        -Ndof: Total number of degrees of freedom.
        -k_list: (List of floats, len: Ne ) Element stiffness values. Ne: Number of elements.
        -Ne1: Starting element to be evaluated.
        -Ne2: Final element to be evaluated.
    
    OUTPUTS:
        -Kg: (Float array, Shape: (Ndof,Ndof) ) Global stiffness matrix.
        -fg: (Float array, Shape: (Ndof,) )     Global force vector.

    """
    # Create the global matrix.


    Ne = len(k_list) # Number of elements.
    Nu = Ne+1        # Number of nodes.
    elements = np.arange(Ne1, Ne2, 1)

    print("creating shared block")
    shr, np_array = create_shared_block()
    chunk_size = int(len(elements)/num_workers)
    chunks = [[shr.name,elements[i*chunk_size:(i+1)*chunk_size]] for i in range(0,num_workers)]
    left_over = elements[num_workers*chunk_size:]
    if len(left_over)!= 0:
        chunks.append([shr.name,left_over])

    if len(sys.argv)>1:

        NProc = int(sys.argv[1])
        print(' Using given NProc = {}'.format(NProc) )

    else:

        NProc = num_workers # Define number of processes.
        print(' Using default configuration. NProc = {}'.format(NProc) )
    st = time.time()
    with Pool(num_workers) as p:

        
        p.map(assemble, chunks)
        p.close()
        p.join()
   
    Kg = np_array.copy()
    shr.close()
    shr.unlink()
    return Kg, fg

# end function


if __name__ == '__main__':
    
    define_global_variables()

    t_start = time.time()
    
    # Total number of degrees of freedom to be generated
    
    
    t_start = time.time()
    
    # Create the global system
    Kg, fg = elasticFEProblem( Ndof, 0, Ne, k_list ) 

    t_end   = time.time()
    
    # print(Kg)

    print('Total time to assemble:',t_end-t_start)

# end if __main__