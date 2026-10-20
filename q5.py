def q5():
    marks = float(input("Enter marks: "))
    if marks < 0 or marks > 100:
        print("Output: Invalid marks! Please enter marks between 0 and 100.")
    elif marks >= 90:
        print("Output: Grade: A")
    elif marks >= 75:
        print("Output: Grade: B")
    elif marks >= 60:
        print("Output: Grade: C")
    elif marks >= 40:
        print("Output: Grade: D")
    else:
        print("Output: Grade: F")

q5()