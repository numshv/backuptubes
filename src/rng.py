import os
import time

def generate_seed():
    pid = os.getpid()
    timestamp = int(time.time_ns())  # Use nanoseconds
    constant = 0xDEADBEEF  # Random constant chosen by me muehehehehe
    seed = pid ^ timestamp ^ constant
    return seed

def linear_congruential_generator(seed, a=1664525, c=1013904223, m=2**32):
    while True:
        seed = (a * seed + c) % m
        yield seed

def RNG(min_num, max_num):
    seed = generate_seed()
    lcg = linear_congruential_generator(seed)
    next(lcg)  # Discard the first number to avoid getting the same number on each call
    scaled = min_num + next(lcg) % (max_num - min_num + 1)
    return scaled

