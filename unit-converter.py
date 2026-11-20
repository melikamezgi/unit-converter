print("Welcome to Unit Converter!")

while True:
    print("\n1. Temperature")
    print("2. Weight")
    print("3. Length")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "4":
        print("Goodbye!")
        break

    if choice == "1":
        print("\n1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")

        option = input("Choose an option: ")

        if option == "1":
            celsius = float(input("Enter Celsius: "))
            result = (celsius * 9 / 5) + 32
            print("Fahrenheit:", result)

        elif option == "2":
            fahrenheit = float(input("Enter Fahrenheit: "))
            result = (fahrenheit - 32) * 5 / 9
            print("Celsius:", result)

        else:
            print("Wrong option!")

    elif choice == "2":
        print("\n1. Kilogram to Gram")
        print("2. Gram to Kilogram")

        option = input("Choose an option: ")

        if option == "1":
            kilogram = float(input("Enter Kilogram: "))
            result = kilogram * 1000
            print("Gram:", result)

        elif option == "2":
            gram = float(input("Enter Gram: "))
            result = gram / 1000
            print("Kilogram:", result)

        else:
            print("Wrong option!")

    elif choice == "3":
        print("\n1. Meter to Centimeter")
        print("2. Centimeter to Meter")

        option = input("Choose an option: ")

        if option == "1":
            meter = float(input("Enter Meter: "))
            result = meter * 100
            print("Centimeter:", result)

        elif option == "2":
            centimeter = float(input("Enter Centimeter: "))
            result = centimeter / 100
            print("Meter:", result)

        else:
            print("Wrong option!")

    else:
        print("Wrong choice! Try again.")
