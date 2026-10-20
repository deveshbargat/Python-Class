def q7():
    year = int(input("Enter year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"Output: {year} is a Leap Year.")
    else:
        print(f"Output: {year} is not a Leap Year.")

q7()