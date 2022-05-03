n = int(input("Enter n: "))
num = n
reverse = 0
while n != 0:
    rem = n % 10
    reverse = reverse*10 + rem
    n //= 10
print(f"Reverse of {num} is {reverse}")