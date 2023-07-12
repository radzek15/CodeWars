#!/usr/bin/env bash

#Debugging sayHello function
#
#The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!
#
#Example output:
#
#Hello, Mr. Spock

say_hello(){
  local arg="$1"
  echo "Hello, $arg"
}
say_hello "$1"