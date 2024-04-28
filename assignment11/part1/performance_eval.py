import numpy as np
import searchUtilsTeam3 as search
import time

arr1 = np.linspace(-10,10,10**7)
search_value = arr1[-2]


st = time.time()
idx_arr1_linear = search.searchutils.linearsearch(arr1, search_value)
et = time.time()

tt = et - st
print('CPU time fortran linear search: {}'.format(tt))

st = time.time()
idx_arr1_linear = search.searchutils.binarysearch(arr1, search_value)
et = time.time()

tt = et - st
print('CPU time fortran binary search: {}'.format(tt))


st = time.time()
idx_arr1_search_sorted = np.searchsorted(arr1, search_value)
et = time.time()

tt = et - st
print('CPU time np.searchsorted(): {}'.format(tt))

st = time.time()
idx_arr1_linear = np.where(arr1 == search_value)
et = time.time()

tt = et - st
print('CPU time np.where() {}'.format(tt))

