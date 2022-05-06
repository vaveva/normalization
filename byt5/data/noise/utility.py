#From https://github.com/ufal/multilexnorm2021/blob/master/data/utility.py
import math


def get_random_index(random_float, length):
    return min(int(math.floor(random_float * length)), length - 1)


def get_random_item(array, random_float):
    return array[get_random_index(random_float, len(array))]


def skewed_probability(p):
    return 1.0 - math.sqrt(1.0 - p)
