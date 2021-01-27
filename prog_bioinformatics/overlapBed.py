#!/usr/bin/env python3
# rohan : submission week 12. recursive binary search tree
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i1", help="file1")
parser.add_argument("-i2", help="file2")
parser.add_argument("-m", help="overlap perc")
parser.add_argument("-j", help="join output", action='store_true')
parser.add_argument('-o',help="output file name")
args = parser.parse_args()

def get_base(file: str):
    with open(file,'r') as fh:
        file2 = fh.readlines()
    a = dict()
    val,z = 0,0
    for x, y in enumerate(file2):
        x1 = y.rstrip().split('\t')
        if x1[0] not in a:
            a[x1[0]] = [[int(x1[1]), int(x1[2]), x1[0] + '_' + str(x-val)]]
            temp = val
        else:
            a[x1[0]].append([int(x1[1]), int(x1[2]), x1[0] + '_' + str(x-temp)])
            val = x+1
    return a

def check_two(x, y):
    if check_one(x[0], y) and check_one(x[1], y):
        return 1
    return 0

def make_tree(data: list):
    pos = int(round(len(data) / 2))
    x,y,z = data[:pos],data[pos+1:],data[pos]
    if len(x) > 1:
        x = make_tree(x)
    elif len(x) == 1:
        x = [x[0],[-1,-1,-1,[]],[-1,-1,-1,[]],[]]
    else:
        x = [-1,-1,-1,[]]

    if len(y) > 1:
        y = make_tree(y)
    elif len(y) == 1:
        y = [y[0],[-1,-1,-1,[]],[-1,-1,-1,[]],[]]
    else:
        y = [-1,-1,-1,[]]
    return [z, x, y, []]

def check_one(x, y):
    if x>=int(y[0]) and x<=int(y[1]):
        return 1
    return 0

def span(y, z):
    if (check_one(y[0],z) or check_one(y[1],z) or check_one(z[0],y) or check_one(z[1],y)):
        return 1
    return 0

def insert_data(tree, pos, val, start, end):
    if tree[0] != -1:
        x = (start, tree[0])
        y = (tree[0], end)
        if check_two(x, pos):
            tree[1][-1].append(val)
        elif span(x, pos):
            insert_data(tree[1], pos, val, x[0], x[1])

        if check_two(y, pos):
            tree[2][-1].append(val)
        elif span(y, pos):
            insert_data(tree[2], pos, val, y[0], y[1])

def get_data(tree, data, start, end):
    for val in data:
        insert_data(tree, [val[0], val[1]], val[-1], start, end)

def remove_null(tree):
    v = len(tree[-1])
    if tree[1] == -1 and tree[2] == -1:
        if v == 0:
            return 1
        else:
            return 0
    else:
        if remove_null(tree[1]) == 1:
            tree[1] = -1

        if remove_null(tree[2]) == 1:
            tree[2] = -1

        if tree[1] == -1 and tree[2] == -1:
            if v == 0:
                return 1
            else:
                return 0

def get_tree(file: list):
    #
    start = file[0][0]-1
    end = file[-1][0] + 1
    c = []
    for pos in file:
        c.extend([pos[0], pos[1]])
    c = list(set(c))
    c.sort()
    tree = make_tree(c)
    get_data(tree, file, start, end)
    remove_null(tree)
    return tree,start,end

def find_overlap(tree, zone, start, end):
    value = []
    #global resu
    a = (start, tree[0])
    b = (tree[0], end)
    if span(a, zone):
        value.extend(tree[-1])
        if tree[1] != -1:
            g = find_overlap(tree[1], zone, a[0], a[1])
            #if g:
            value.extend(g)
            #    if value:
            #        resu = min([int(x.split('_')[1]) for x in value])
            #        return 1

    if span(b, zone):
        value.extend(tree[-1])
        if tree[2] != -1:
            p = find_overlap(tree[2], zone, b[0], b[1])
            #if p and not isinstance(p, int):
            value.extend(p)
    return list(set(value))

def get_map(x,y,tree,start,end,file,perc):
    #global resu
    #resu = 0
    try:
        resu = find_overlap(tree,[x, y],start,end)
    except:
        pass
    z = []
    if resu:
        resu = [int(x.split('_')[1]) for x in resu]
        for r in resu:
            q = file[r]
            if (min(y, q[1]) - max(x, q[0]))/(y-x) >= perc:
                z.append([q[0],q[1]])
        #else:
    return z

def overlap_files(file1: str, data_dict: dict, output: str, perc, flag):
    with open(file1, 'r') as fh:
        plant = dict()
        result = []
        for line in fh:
            part = line.rstrip().split()
            if part[0] not in plant:
                plant[part[0]],s,e = get_tree(data_dict[part[0]])
            res = get_map(int(part[1]), int(part[2]), plant[part[0]], s, e, data_dict[part[0]],perc)
            if res:
                for rb in res:
                    if not flag:
                        result.append(part[0]+'\t'+str(rb[0])+'\t'+str(rb[1])+'\n')
                    else:
                        result.append(part[0]+'\t'+str(rb[0])+'\t'+str(rb[1])+'\t'+part[0]+'\t'+part[1]+'\t'+part[2]+'\n')
    with open(output,'w') as fw:
        fw.writelines(result)

if __name__ == '__main__':
    data = get_base(args.i2)
    overlap_files(args.i1, data, args.o, int(args.m)/100, args.j)
