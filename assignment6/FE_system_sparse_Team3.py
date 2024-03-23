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
import scipy.sparse as sps

# =====================================================================================


def define_global_variables():
  global Kg
  global fg
  global Ne
  global Ndof
  global k_list
  global chunks
  global num_workers
  
  Ndof = 500000
  Ne   = Ndof-1 # number of elements.
  num_workers = 1

  
  # List of elemental stiffness values.
  #
  # This should be created such that each element 
  # may have a different stiffness value.
  chunks = []
  k_list  = [1]*Ne
  Kg = sps.lil_matrix((Ndof,Ndof))
  fg = np.zeros((Ndof,))
  
  
  
def assemble(e):
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
    Kg_temp = sps.lil_matrix((Ndof,Ndof))
    

    for e in e:
        Ke = k_list[e] * np.array([[ 1,-1],
                                   [-1, 1]])
    
        fe = np.array([0.0,
                       0.0])

        for i in range(2):
            for j in range(2):

                Kg_temp[e+i,e+j] = Kg_temp[e+i,e+j] + Ke[i,j]
            # end for 
        # end for
    
    Kg_temp = Kg_temp.tocsr()
    return Kg_temp, fg
# end function





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
    define_global_variables()
    elements = np.arange(Ne1, Ne2, 1)

    chunk_size = int(len(elements)/num_workers)
    chunks = [elements[i*chunk_size:(i+1)*chunk_size] for i in range(0,num_workers-1)]
    left_over = elements[(num_workers-1)*chunk_size:]
    if len(left_over)!= 0:
        chunks.append(left_over)
    if len(sys.argv)>1:

        NProc = int(sys.argv[1])
        print(' Using given NProc = {}'.format(NProc) )

    else:

        NProc = num_workers # Define number of processes.
        print(' Using default configuration. NProc = {}'.format(NProc) )

    # end if 

    
    p = mproc.Pool( processes = NProc ) # Number of processes created
    pool_res= p.map(assemble, chunks)
    Kg = sum([pool_res[i][0] for i in range(0,len(pool_res))])
    fg = sum([pool_res[i][1] for i in range(0,len(pool_res))])
    # fg = sum(pool_res[1])
    # for e in range( Ne1, Ne2):
        
    #     # Assemble the elemental values into the global components.
    #     assemble(e,Kg,fg)
        
    # # end for

    return Kg, pool_res

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