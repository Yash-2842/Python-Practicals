n = int(input("Enter number of element in fibonacci series: "))
fibo1,fibo2,temp = 0,1,0
print(fibo1)
for i in range(n-1):
    print(fibo2)
    temp = fibo2
    fibo2 = fibo1 + fibo2
    fibo1 = temp
