wold = 'Абракада'
result = []
for i in range(len(wold)):
    letter = wold[i]
    letter = letter.upper() if i % 2 == 0 else letter.lower()
    result.append(letter)
result = '.'.join(result)
print(result)

