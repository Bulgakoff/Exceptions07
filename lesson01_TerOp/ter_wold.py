wold = 'слово'
result = []
for i in range(len(wold)):
    if i % 2 == 0:
        letter = wold[i].upper()
    else:
        letter = wold[i].lower()
    result.append(letter)
result = '/'.join(result)
print(result)

is_wo = True
wold_up = 'СлОвО' if is_wo else wold
print(wold_up)



