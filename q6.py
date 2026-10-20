def fmt(n):
    return int(n) if float(n).is_integer() else n

def q6():
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ").strip()
    b = float(input("Enter second number: "))
    if op == "+":
        print(f"Output: Result: {fmt(a + b)}")
    elif op == "-":
        print(f"Output: Result: {fmt(a - b)}")
    elif op == "*":
        print(f"Output: Result: {fmt(a * b)}")
    elif op == "/":
        if b == 0:
            print("Output: Error: Division by zero is not allowed.")
        else:
            print(f"Output: Result: {fmt(a / b)}")
    else:
        print("Output: Error: Invalid operator!")

q6()