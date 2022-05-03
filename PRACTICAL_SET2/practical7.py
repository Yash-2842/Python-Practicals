char = input("Enter Character: ")
if char.isalpha():
    print(f"{char} is alphabet.")
elif char.isdigit():
    print(f"{char} is number.")
else:
    print(f"{char} is special symbol.")
