#!/usr/bin/env bash

#Convert month name to number. First parameter - month, return this number.
#
#Example:
#
#stdin:Dec
#stdout:12
#
#stdin:Jan
#stdout:01
#
#stdin:APR
#stdout:04
#
#stdin:FeB
#stdout:02

case $(tr '[:upper:]' '[:lower:]' <<< "$1" | head -c 3) in
    "jan") echo "01" ;;
    "feb") echo "02" ;;
    "mar") echo "03" ;;
    "apr") echo "04" ;;
    "may") echo "05" ;;
    "jun") echo "06" ;;
    "jul") echo "07" ;;
    "aug") echo "08" ;;
    "sep") echo "09" ;;
    "oct") echo "10" ;;
    "nov") echo "11" ;;
    "dec") echo "12" ;;
  esac