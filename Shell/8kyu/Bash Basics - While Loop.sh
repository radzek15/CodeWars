#!/usr/bin/env bash

#Create a simple while loop in bash that prints the numbers 1-20 to stdout.
#
#It should look like (stdout):
#
#Count: 1
#Count: 2
#...
#Count: 20


countToTwenty() {
  number=1
  while [ $number -le 20 ]; do
    echo "Count: $number"
    number=$((number+1))
  done
}

countToTwenty