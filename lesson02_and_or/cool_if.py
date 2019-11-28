# строука
s = ''
print('#КЛассика  ////////////////////////')
if len(s) != 0:
    print('Трока не ПУстая')
else:
    print('Empty string')
print(r'#Удобный питон способ     ////////////////////////')
if s:
    print('Трока не ПУстаяяяя')
else:
    print('Empty stringggggg')

print(r'#Аналогично со списками и словарями   ////////////////////////')
l = [1, 2, 3, 4, 78]
d = {1: 'a'}
if len(l) != 0:
    print('лист не ПУстая')
else:
    print('Empty list')
print('DICTIONARY')
if len(d) != 0:
    print('dict не ПУстая')
else:
    print('Empty dict')
print(r'list по другому\\//////////////////////////')
if l:
    print('лист не ПУстая')
else:
    print('Empty list')
print(r'лист и dict по другому\\//////////////////////////')
if d and l:
    print('лист не ПУстая и dict не ПУстые')
else:
    print('Empty dict и лист ')
