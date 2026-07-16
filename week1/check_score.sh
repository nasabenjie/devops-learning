#!/bin/bash

echo "Enter your score: "
read score


if [ $score -ge 50 ]
then
echo "Congragulations you passed with $score"
else
echo "sorry you failed with $score.You need 50 to pass"
fi
