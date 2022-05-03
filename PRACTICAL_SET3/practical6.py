import math
n = int(input("Enter Number: "))
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        print(f"{n} is not prime.")
        break
else:
    print(f"{n} is prime.")