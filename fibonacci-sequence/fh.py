lst = [1,1]
i = int(input('long of sequnce: '))
if i == 1:
    print('[1]')
    exit()
if i == 2:
    print(lst)
    exit()

if i >2:
    for a in range(i-2):
        lst.append(lst[-1]+lst[-2])

len = len(lst)
print(lst)
for b in range(0,len+1):
    i = b
    if i%2==0:
        print(' '*(len-i+1), end='')
        for a in range(0, i):
            print(lst[a], end='')
            print(' ', end='')
        print(' '*(len-i))

    else:
        print(' '*(len-i), end='')
        for a in range(0,i):
            print(' ', end='')
            print(lst[a], end='')
        print(' '*(len-i))
