a, b, c = int(input("Enter Number: ")), int(input("Enter Number: ")), int(input("Enter Number: "))

maximum = 0
if a > b:
    if a > c:
        maximum = a
    else:
        maximum = c
else:
    if b > c:
        maximum = b
    else:
        maximum = c
print(f"{maximum} is maximum")
