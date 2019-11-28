import copy
# копия срезом:
a = [1, 2, 23, [4, 34]]
b = copy.deepcopy(a)
b[3][0] = 300
print(f'----> copy.deepcopy(a) + влож список {a}')
print(f'----> copy.deepcopy(a)  + влож список {b} ')
