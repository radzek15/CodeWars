#!/usr/bin/env bash

#You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.
#
#Find max(abs(length(x) − length(y)))
#
#If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).
#Example:
#
#a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
#a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
#mxdiflg(a1, a2) --> 13
#
#Bash note:
#
#    input : 2 strings with substrings separated by ,
#    output: number as a string

#!/bin/bash
accum () {
  min() {
    echo $1 | awk -F, '{ for( i=1; i<=NF; i++ ) {print length($i)}}' | sort -n | head -1
  }
  max (){
    echo $1 | awk -F, '{ for( i=1; i<=NF; i++ ) {print length($i)}}' | sort -nr | head -1
  }
    min1=$(min $1)
    max1=$(max $1)
    min2=$(min $2)
    max2=$(max $2)
    if [ -z "$1" ] || [ -z "$2" ]; then
      echo "-1";
    else
      echo $(($((max1-min2)) > $((max2-min1)) ? $((max1-min2)) : $((max2-min1))))
    fi
}
accum "$1" "$2"