def day2_converter():
    print("Welcome to the Unit Converter!")
    print("Please select the type of conversion you would like to perform:")
    print("1. Celsius to Fahrenheit")
    print("2. Radians to Degrees")
    print("3. Millimeters to Inches")
#1. select the conversion type
    choice = input("Enter your conversion option (1/2/3): ")
#2. perform the conversion based on user input
    if choice == "1":
        celsius = float(input("enter the tempeture in celsius:"))
        fahrenheit = (celsius * 9/5)+ 32
        print (f"{celsius} °C is equal to {fahrenheit} °F.")
    elif choice == "2":
        radians = float(input("enter the angle in radians:"))
        degrees = radians * (180/3.141592653589793)
        print (f"{radians} radians is equal to {degrees} degrees")
    elif choice == "3":
        millimeters = float(input("enter the length in millimeters:"))
        inches = millimeters / 25.4
        print (f"{millimeters} millimeters is equal to {inches} inches.")
    else:
        print("❌ Invalid choice. Please run the script again and select 1, 2, or 3.")
#3. run the function
day2_converter()