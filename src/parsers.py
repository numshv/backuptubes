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

def csvtoarr(file):
    path = path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)),'databases', file)
    user_file = open(path, 'r')

    arr = []
    for line in user_file:
        inp_arr = csv_parser(line.replace('\n', ''))
        arr.append(inp_arr)
    return arr
