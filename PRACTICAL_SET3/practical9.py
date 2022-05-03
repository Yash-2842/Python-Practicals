n = int(input("Enter Number: "))
temp = n
len = len(str(n))
sum = 0
while n != 0:
    rem = n % 10
    sum += rem**len
    n //= 10
if temp == sum:
    print(f"{temp} is Armstrong number")
else:
    print(f"{temp} is not Armstrong number")