def q3():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if a > b:
        print(f"Output: {a} is the largest number.")
    elif b > a:
        print(f"Output: {b} is the largest number.")
    else:
        print("Output: Both numbers are equal.")

q3()