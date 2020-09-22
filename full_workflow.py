#!/usr/bin/env python
import pickle
import json
import numpy as np
import time
import matplotlib.pyplot as plt

# # Expand dictionary
# 
# All functions necessary to expand the factor dictionary. Forgive the repetitiveness / lack of brevity.

# In[2]:


def stringify(num):
    l = [0]*10

    if type(num) == int:
        s = str(num)
        for c in s:
            l[int(c)] += 1
    if type(num) == list:
        for c in num:
            l[c] += 1

    return ','.join([str(i) for i in l[2:]])

def expand_dict(d, beg, end):
    """There are two cubes that need to be expanded: 2^x, 3^y, 7^z and 3^x, 5^y, and 7^z"""
    # seven added shapes to a cube: 2, 3, 7
    
    # expanded_cube:
    for t in range(beg, end):
        tp = 2**t
        for th in range(beg, end):
            thp = 3**th
            for s in range(beg, end):
                sp = 7**s
                num = tp*thp*sp
                if '0' not in str(num):
                    string = stringify(num)
                    d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]
    
    # dim-longs
    # 7
    for t in range(beg, end):
        tp = 2**t
        for th in range(beg, end):
            thp = 3**th
            for s in range(0, beg):
                sp = 7**s
                num = tp*thp*sp
                if '0' not in str(num):
                    string = stringify(num)
                    d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]
    
    # 2
    for t in range(0, beg):
        tp = 2**t
        for th in range(beg, end):
            thp = 3**th
            for s in range(beg, end):
                sp = 7**s
                num = tp*thp*sp
                if '0' not in str(num):
                    string = stringify(num)
                    d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]
    
    # 3             
    for t in range(beg, end):
        tp = 2**t
        for th in range(0, beg):
            thp = 3**th
            for s in range(beg, end):
                sp = 7**s
                num = tp*thp*sp
                if '0' not in str(num):
                    string = stringify(num)
                    d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]
    
    #faces
    # 2
    for t in range(beg, end):
        tp = 2**t
        for th in range(0, beg):
            thp = 3**th
            for s in range(0, beg):
                sp = 7**s
                num = tp*thp*sp
                if '0' not in str(num):
                    string = stringify(num)
                    d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]
                    
    # 3
    for t in range(0, beg):
        tp = 2**t
        for th in range(beg, end):
            thp = 3**th
            for s in range(0, beg):
                sp = 7**s
                num = tp*thp*sp
                if '0' not in str(num):
                    string = stringify(num)
                    d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]
    # 7
    for t in range(0, beg):
        tp = 2**t
        for th in range(0, beg):
            thp = 3**th
            for s in range(beg, end):
                sp = 7**s
                num = tp*thp*sp
                if '0' not in str(num):
                    string = stringify(num)
                    d[string] = d.get(string, []) + [[num, (t, th, 0, s)]]
     
# --------------------------------------------------------------------------------------------------- #
# cube: 5, 3, 7
#     print('fives')
    beg_p = 1 if beg == 0 else beg
    
    # expanded_cube:
    for t in range(beg_p, end):
        tp = 5**t
        for th in range(beg, end):
            thp = 3**th
            for s in range(beg, end):
                sp = 7**s
                num = tp*thp*sp
                if '0' not in str(num):
                    string = stringify(num)
                    d[string] = d.get(string, []) + [[num, (0, th, t, s)]]
    
    # dim-longs
    # 7
    for t in range(beg_p, end):
        tp = 5**t
        for th in range(beg, end):
            thp = 3**th
            for s in range(0, beg):
                sp = 7**s
                num = tp*thp*sp
                if '0' not in str(num):
                    string = stringify(num)
                    d[string] = d.get(string, []) + [[num, (0, th, t, s)]]
    
    # 2
    for t in range(1, beg):
        tp = 5**t
        for th in range(beg, end):
            thp = 3**th
            for s in range(beg, end):
                sp = 7**s
                num = tp*thp*sp
                if '0' not in str(num):
                    string = stringify(num)
                    d[string] = d.get(string, []) + [[num, (0, th, t, s)]]
    
    # 3             
    for t in range(beg_p, end):
        tp = 5**t
        for th in range(0, beg):
            thp = 3**th
            for s in range(beg, end):
                sp = 7**s
                num = tp*thp*sp
                if '0' not in str(num):
                    string = stringify(num)
                    d[string] = d.get(string, []) + [[num, (0, th, t, s)]]
    
    #faces
    # 2
    for t in range(beg_p, end):
        tp = 5**t
        for th in range(0, beg):
            thp = 3**th
            for s in range(0, beg):
                sp = 7**s
                num = tp*thp*sp
                if '0' not in str(num):
                    string = stringify(num)
                    d[string] = d.get(string, []) + [[num, (0, th, t, s)]]
                    
    # 3
    for t in range(1, beg):
        tp = 5**t
        for th in range(beg, end):
            thp = 3**th
            for s in range(0, beg):
                sp = 7**s
                num = tp*thp*sp
                if '0' not in str(num):
                    string = stringify(num)
                    d[string] = d.get(string, []) + [[num, (0, th, t, s)]]
    # 7
    for t in range(1, beg):
        tp = 5**t
        for th in range(0, beg):
            thp = 3**th
            for s in range(beg, end):
                sp = 7**s
                num = tp*thp*sp
                if '0' not in str(num):
                    string = stringify(num)
                    d[string] = d.get(string, []) + [[num, (0, th, t, s)]]

    with open(f'dict_f{end}.pickle', 'wb') as f:
        pickle.dump(d, f)
    
    return d


# # Use dictionary
# 
# Use the dictionary to search upward in the tree to find longest branch.

def prime_factor(n):
    '''given n, return prime factorization under 10 (2, 3, 5, 7)'''
    l = []
    primes = [2, 3, 5, 7]
    for p in primes:
        while (n % p == 0) and (n != 1):
            n /= p
            l.append(p)
    return l if n == 1 else []

def combo_clusters(l):
    def replace_factors(l, f, s, e, n):
        new_l = list(l)
        for _ in range(f*2):
            new_l.pop(new_l.index(2))
        for _ in range(f):
            new_l.append(4)

        for _ in range(s):
            new_l.pop(new_l.index(3))
            new_l.pop(new_l.index(2))
        for _ in range(s):
            new_l.append(6)

        for _ in range(e*3):
            new_l.pop(new_l.index(2))
        for _ in range(e):
            new_l.append(8)

        for _ in range(n*2):
            new_l.pop(new_l.index(3))
        for _ in range(n):
            new_l.append(9)

        return new_l

    # nines
    number_of_threes = len([i for i in l if i == 3])
    nines = range(0, number_of_threes // 2 + 1)

    # fours and eights
    number_of_twos = len([i for i in l if i == 2])
    fours = range(0, number_of_twos // 2 + 1)
    eights = range(0, number_of_twos // 3 + 1)

    # sixes
    sixes = range(0, (number_of_twos + number_of_threes) // 2 + 1)

    combos = []
    for f in fours:
        for s in sixes:
            for e in eights:
                for n in nines:
                    # if ((f*2 + e*3) <= number_of_twos and 
                    # (s*2 + f*2 + e*3 + n*2 <= number_of_threes + number_of_twos)):
                    try:
                        new_l = replace_factors(l, f, s, e, n)
                        combos.append(new_l)
                    except:
                        pass

    return combos

def search_higher_node(n, d):
    l = prime_factor(n)
    combos = combo_clusters(l)
    higher_nodes = []
    for c in combos:
        as_string = stringify(c)
        if as_string in d:
            higher_nodes += d[as_string]
    return higher_nodes

def make_tree(seed, d):
    def recursive_tree(l, d, tree):
        if len(l) != 0:
            for n in l:
                new_l = search_higher_node(n, d)
                if n in new_l:
                    new_l.pop(new_l.index(n))
                tree[n] = new_l
                recursive_tree(new_l, d, tree)

    tree = {}
    recursive_tree([seed], d, tree)
    return tree

def tree_height(tree): 
    def recursive_height(root, tree, li, count=0):
        children = tree[root]
        for child in children:
            try:
                if len(tree[child]) != 0:
                    li.append(count)
                    recursive_height(child, tree, li, count=count+1)
            except:
                print(child)

    li = []
    root = min(tree.keys()) # yikes this is scary
    recursive_height(root, tree, li)
    try:
        return max(li)
    except:
        return None


# # Use functions
beg = 475
end = 476
old = f'dict_f{beg}.pickle'

with open(old, 'rb') as f:
    d_o = pickle.load(f)
tic = time.time()
d_n = expand_dict(d_o, beg, end)

l = []
d_f = {}
for k, v in d_n.items():
    d_f[k] = [x[0] for x in v]

for i in range(1, 100):
    tree = make_tree(i, d_f)
    h = tree_height(tree)
    if not h is None:
        l.append([i, h])
m = np.array(l)
plt.scatter(x=m[:, 0], y=m[:, 1])
plt.show()

