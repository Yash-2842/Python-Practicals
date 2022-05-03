n = int(input("Enter n: "))
for i in range(1,n):
    if i % 2 == 0 and i % 6 != 0:
        print(i)