! Description: Function that finds the location (idx) of a value x
! in an array using the linear search algorithm.
!
! Find idx such that arr(idx) == x
!

MODULE searchutils
use omp_lib

CONTAINS
FUNCTION linearSearch(arr, n, x) RESULT(idx)
 IMPLICIT NONE
 REAL(8) :: arr(n) ! Array to search
 INTEGER :: n ! Number of elements in array.
 REAL(8) :: x ! Value to search for in array.
 INTEGER :: idx ! Result of the search. [arr(idx) == x]
 INTEGER :: size_of_array
 INTEGER :: counter
 idx = -1
 
 size_of_array = SIZE(arr)


 !$OMP PARALLEL DO PRIVATE(counter)
 DO counter = 1, size_of_array, 1
  IF (arr(counter) == x) THEN
     idx = counter
  END IF
 END DO
 !$OMP END PARALLEL DO




END FUNCTION linearSearch
! Description: Function that finds the location (idx) of a value x
! in a sorted array using the binary search algorithm.
!
! Find idx such that arr(idx) == x
!
FUNCTION binarySearch(arr, n, x) RESULT(idx)
 IMPLICIT NONE
 REAL(8) :: arr(n) ! Array to search
 INTEGER :: n ! Number of elements in array.
 REAL(8) :: x ! Value to search for in array.
 INTEGER :: idx ! Result of the search. [arr(idx) == x]

 INTEGER :: l
 INTEGER :: r
 INTEGER :: m



 l = 1
 r = SIZE(arr)
 DO WHILE (l <= r)
  idx = -1
  m = l + (r - l)/2
  IF (arr(m) == x) THEN
     idx = m
     EXIT
  END IF

  IF (arr(m) < x) THEN
      l = m + 1
  ELSE 
      r = m - 1
  END IF
 END DO

! Your implementation here.
END FUNCTION binarySearch

END MODULE searchutils

