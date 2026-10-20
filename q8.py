def fmt(n):
    return int(n) if float(n).is_integer() else n

def q8():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    if a == b == c:
        print("Output: All three numbers are equal.")
    elif a >= b and a >= c:
        print(f"Output: {fmt(a)} is the greatest number.")
    elif b >= a and b >= c:
        print(f"Output: {fmt(b)} is the greatest number.")
    else:
        print(f"Output: {fmt(c)} is the greatest number.")

q8()