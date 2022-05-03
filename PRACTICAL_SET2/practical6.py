degree = input("Enter Your Degree (BE/ME): ").upper()
experience = int(input("Enter Your Experiencce: "))
if degree == "BE":
    if experience < 5:
        salary = 30000
    else:
        salary = 40000
elif degree == "ME":
    if experience < 5:
        salary = 50000
    else:
        salary = 60000
print(f"Your Salary is: {salary}")
