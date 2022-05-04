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
    print(lst)