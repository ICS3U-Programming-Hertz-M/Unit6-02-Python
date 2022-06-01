#!/usr/bin/env python3

# Created by: hertz
# Created on: May 31, 2022.
# this program Generates random numbers and displays the max value to the user.
import random
import constants


def find_max_value(random_num):
    max_value = random_num[0]

    # determines the range and return the max value
    for counter in range(len(random_num)):
        if max_value < random_num[counter]:
            max_value = random_num[counter]
    return max_value


def main():
    # initialize counter and creat a list
    counter = 0
    random_list = []

    # display random number to the user
    for counter in range(constants.MAX_ARRAY_SIZE):
        random_list.append(random.randint(constants.MIN_N, constants.MAX_N))

        print("{} is added to the list at position {}"
              .format(random_list[counter], counter))

    # call functiondisplay the max value
    maximum = find_max_value(random_list)
    print("")
    # display the max to the user
    print("{} is the max value".format(maximum))


if __name__ == "__main__":
    main()
