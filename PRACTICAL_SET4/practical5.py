import math
n = int(input('enter n: '))
for j in range(2, n+1):
    for i in range(2, int(math.sqrt(j)+1)):
        if j % i == 0:
            break
    else:
        print(j)
