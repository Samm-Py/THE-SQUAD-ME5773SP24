#!/bin/bash


Var1=NameReceived_$1.txt
Var2=1


echo The K-Fibonacci series for K = $1 is:

 
arr=()

for i in $(eval echo {1..$1})
do
arr+=(1)
done


for ((j=0; j<10; j++))
do	
	idx2=${#arr[*]}
	idx1=$(($idx2-$1))
	temp=0
	for((i=$idx1 ; i < $idx2 ; i++))
	do
		temp=$(($temp+${arr[$i]}))
	done
	arr+=($temp)
done
echo ${arr[@]}

