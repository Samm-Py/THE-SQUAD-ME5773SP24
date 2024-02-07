#!/bin/bash



Var1=NameReceived_$1.txt
temp=1
for i in $(eval echo {1..$1})
do
	temp=$((temp*i))
	echo $i! = $temp
done
echo
