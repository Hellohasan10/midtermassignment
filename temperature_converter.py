while True:
    celsius = float(input("Enter temperature in Celsius: "))

    # Convert and display the result
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit}°F")

    repeat = input("Would you like to change over another temperature? (yes/no): ")
    if repeat != "yes":
        break