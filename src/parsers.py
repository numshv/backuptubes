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

def csv_parser(line):
    s=[]
    j=0
    for i in range (len(line)):
        if ','== line [i]:
            s.append(line[j:i])
            j=i+1
    s.append (line[j:])
    return s

def csvtoarr(file):
    path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)),'databases', file)
    user_file = open(path, 'r')

    arr = []
    for line in user_file:
        inp_arr = csv_parser(line.replace('\n', ''))
        arr.append(inp_arr)
    arr.pop(0)
    return arr

def load():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="display a folder of the databases",
                        type=str)
    args = parser.parse_args()
    print(args.folder)

def appendcsv(arr, file):
    csvtoarred = csvtoarr(file)
    path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)),'databases', file)
    if len(arr)>len(csvtoarred):
        with open(path, mode='a', newline='') as file:
            for i in range(len(csvtoarred), len(arr)):
                row_str = ','.join(map(str, arr[i]))
                file.write('\n' + row_str)


def save(user_arr, monster_inventory_arr, item_inventory_arr, monster_arr, monster_shop_arr, item_shop_arr):
    appendcsv(user_arr, 'user.csv')
    appendcsv(monster_inventory_arr, 'monster_inventory.csv')
    appendcsv(item_inventory_arr, 'item_inventory.csv')
    appendcsv(monster_arr, 'monster.csv')
    appendcsv(monster_shop_arr, 'monster_shop.csv')
    appendcsv(item_shop_arr, 'item_shop.csv')
    print('Semua perubahan telah berhasil tersimpan!\n')
    time.sleep(2)