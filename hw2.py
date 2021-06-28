numOfLine = int( input('출력 줄수 입력 : ') )

for a in range(0, numOfLine, 1):
    for x in range(numOfLine-1-a, 0, -1):
        print(' ', end='')

    for x in range(0, 2*a+1, 1):
        print('*', end='')

    print('')
