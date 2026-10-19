def calculator():
    print("Simple Calculator")
    print("Select Operation:")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")

    operation = input("Select an option 1,2,3,4: ")

    if operation not in ["1", "2", "3", "4"]:
        print("Invalid operation selected.")
        return

    var1 = float(input("Enter 1st number: "))
    var2 = float(input("Enter 2nd number: "))

    if operation == "1":
        print(f"Output: {var1} + {var2} = {var1 + var2}")

    elif operation == "2":
        print(f"Output: {var1} - {var2} = {var1 - var2}")

    elif operation == "3":
        print(f"Output: {var1} * {var2} = {var1 * var2}")

    elif operation == "4":
        if var2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"Output: {var1} / {var2} = {var1 / var2}")


calculator()
