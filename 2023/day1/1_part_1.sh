#! /bin/bash

sum=0

for line in $(cat input); do
    echo $line

    # Match the first digit
    [[ ${line} =~ ^[^0-9]*([0-9]).*$ ]]
    first_digit=${BASH_REMATCH[1]}

    # Match the last digit
    [[ ${line} =~ ^.*([0-9])[^0-9]*$ ]]
    last_digit=${BASH_REMATCH[1]}

    # Combine to a two-digit number
    number=${first_digit}${last_digit}

    # Sum it
    sum=$(expr $sum + $number)

    echo $sum
done
