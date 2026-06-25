def day3_solver():
    print("welcome to the Quadratic Equation Solver!")
    print("Please enter the coefficients of the quadratic equation in the form ax^2 + bx + c = 0")
    #1. collect coefficients from user input
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))
    #2. calculate the discriminant
    discriminant = b**2 - 4*a*c
    #3. determine the nature of the roots based on the discriminant
    if discriminant > 0:
        root1= (-b + discriminant**0.5) / (2*a)
        root2= (-b - discriminant**0.5) / (2*a)
        print(f"The equation has two real and distinct roots: {root1} and {root2}.")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"The equation has one real root: {root}.")
    else:
        print("The equation has no real roots.")
    #4. run the function
day3_solver()