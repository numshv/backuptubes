import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("folder", help="display a folder of the databases",
                    type=str)
args = parser.parse_args()

def csvtoarr(file):
    path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)),'databases', file)
    user_file = open(path, 'r')

    arr = []
    for line in user_file:
        inp_arr = csv_parser(line.replace('\n', ''))
        arr.append(inp_arr)
    arr.pop(0)
    return arr

def process_file(filename):
    with open(filename, 'r') as file_input:
        pass  # do something here . . .

def process_directory(directory_name):
    for filename in os.listdir(directory_name):
        process_file(os.path.join(directory_name, filename))

process_directory(args.inputdir)