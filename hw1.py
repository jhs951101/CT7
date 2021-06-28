str1 = "yesterday all my troubles seemed so far away"
print(str1)

numOfMoum = 0
numOfJaum = 0

for i in range(0, len(str1), 1):

    if str1[i] != ' ':
        if str1[i] in 'aeiou':
            numOfMoum += 1
        else:
            numOfJaum += 1

print('모음의 개수 :', numOfMoum)
print('자음의 개수 :', numOfJaum)
