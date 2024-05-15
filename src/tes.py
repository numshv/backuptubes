import os
def csv_parser(line):
    s=[]
    j=0
    for i in range (len(line)):
        if ','== line [i]:
            s.append(line[j:i])
            j=i+1
    s.append (line[j:])
    return s

def csvtoarr(main_path, file):
    path = os.path.join(main_path, file)
    user_file = open(path, 'r')

    arr = []
    for line in user_file:
        inp_arr = csv_parser(line.replace('\n', ''))
        arr.append(inp_arr)
    arr.pop(0)
    return arr


def load():
    import argparse
    import os
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="display a folder of the databases",
                        type=str)
    args = parser.parse_args()
    
    if args != 'data':
        print("Folder doesn't exits")
    
    else:
        all_files = []
        main_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)), args.folder)
        for filename in os.listdir(args.folder):
            cur_csv = csvtoarr(main_path, filename)
            all_files.append(cur_csv)
        return all_files, 


load()