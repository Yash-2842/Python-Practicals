n = int(input("Enter number: "))
temp = n
rev = 0
while temp != 0:
    rem = temp % 10
    rev = rev * 10 + rem
    temp //= 10
if n == rev:
    print(n, "is palindrome")
else:
    print(n, "is not palindrome")
