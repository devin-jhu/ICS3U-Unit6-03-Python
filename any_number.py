#!/usr/bin/env python3

# Created by Devin Jhu
# Created on May 2022
# The largest number finder


import random


def smallest(number_array):
    # this function finds the largest number in the array

    smallest_number = number_array[0]

    for counter in number_array:
        if counter < smallest_number:
            smallest_number = counter

    return smallest_number


def main():
    # this function gets 10 random numbers

    number_array = []

    print("The smallest random number finder")

    # process
    for counter in range(0, 10):
        random_number = random.randint(0, 100)
        number_array.append(random_number)
        print("Random number: {}".format(random_number))

    smallest_number = smallest(number_array)

    # output
    print("The smallest number is {0}.".format(smallest_number))

    print("\nDone.")


if __name__ == "__main__":
    main()
