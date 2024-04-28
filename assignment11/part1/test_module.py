import numpy as np
import searchUtilsTeam3 as search

search_value = 12
arr1 = np.arange(1,15,1, dtype = 'float64')
arr2 = np.random.choice(arr1, size = len(arr1), replace = False)

print('Sorted Array: {}'.format(arr1))
print('Unsorted Array: {}'.format(arr2))

print('\n')

idx_arr1_linear = search.searchutils.linearsearch(arr1, search_value)
idx_arr2_linear = search.searchutils.linearsearch(arr2, search_value)


print('Index of search value {0} in {1} is: {2}'.format(search_value, arr1, idx_arr1_linear-1))
print('\n')
print('Index of search value {0} in {1} is: {2}'.format(search_value, arr2, idx_arr2_linear-1))
print('\n')

idx_arr1_binary = search.searchutils.binarysearch(arr1, search_value)
idx_arr2_binary = search.searchutils.binarysearch(arr2, search_value)

print('Index of search value {0} in {1} is: {2}'.format(search_value, arr1, idx_arr1_binary-1))
print('\n')
