#!/bin/bash

echo "Enter your name: "
read name

echo "Enter your age: "
read age

echo "Hello $name"

if [ $age -ge 18 ]
then
echo "You're an adult"
else
echo "You're not an adult"
fi
