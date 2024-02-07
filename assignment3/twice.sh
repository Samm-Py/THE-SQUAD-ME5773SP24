#!/bin/bash

var1=NameReceived_$1.txt


sleep $((2*$1))

echo Terminated a task that takes $((2*$1)) seconds.
