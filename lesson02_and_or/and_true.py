import math

# есть список чисел
numbers = [2, 3, 5, 6, 7, 6543, 44, 22]
n = []

for number in numbers:
    if number > 0:
        sqrt = math.sqrt(number)
        if sqrt < 2:
            n.append(number)
print(n)

numbers = [2, 3, 5, 6, 7, 6543, 44, 22]
n = []
for number in numbers:
    if number:
        sqrt = math.sqrt(number)
        if sqrt < 2:
            n.append(number)
print(n)
print('теперь по другому с and иили or\///////////////////////////')
numbers = [2, 3, 5, 6, 7, 6543, 44, 22]
n = []
for number in numbers:
    sqrt = math.sqrt(number)
    if number > 0 and sqrt < 2:
        n.append(number)
print(n)
print('через генератор....\/////////////////////')
result =[number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)