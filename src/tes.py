
import argparse
import os
 
# function to convert the input and 
# check the range

def checker(folder):
    data_path = os.path.join(os.path.abspath(__file__), 'databases')
    isExist =  os.path.exists(os.path.join(data_path, folder))
    if isExist == False:
        raise argparse.ArgumentTypeError('Folder tidak ditemukan')

 
 
parser = argparse.ArgumentParser(
    description='Processing integers in range 5 to 15')
 
# passing the function for 'type' parameter
parser.add_argument('<folder>', type=checker)
 
res = parser.parse_args()
print("Sukses")