
def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm / 2.54

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_cm(meters):
    return meters * 100

def cm_to_meters(cm):
    return cm / 100

def mm_to_cm(mm):
    return mm / 10

def conversion_calculator():
    print("Conversion options:")
    print("1. Inches to cm")
    print("2. Cm to inches")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Meters to cm")
    print("6. Cm to meters")
    print("7. Mm to cm")
    
    choice = input("Choose a conversion option (1-7): ")
    value = float(input("Enter the value to convert: "))
    
    if choice == '1':
        print(f"{value} inches is {inches_to_cm(value)} cm")
    elif choice == '2':
        print(f"{value} cm is {cm_to_inches(value)} inches")
    elif choice == '3':
        print(f"{value} Celsius is {celsius_to_fahrenheit(value)} Fahrenheit")
    elif choice == '4':
        print(f"{value} Fahrenheit is {fahrenheit_to_celsius(value)} Celsius")
    elif choice == '5':
        print(f"{value} meters is {meters_to_cm(value)} cm")
    elif choice == '6':
        print(f"{value} cm is {cm_to_meters(value)} meters")
    elif choice == '7':
        print(f"{value} mm is {mm_to_cm(value)} cm")
    else:
        print("Invalid choice")

def main():
    print("Choose an option:")
    print("1. Normal calculation")
    print("2. Conversion calculation")
    
    option = input("Enter 1 or 2: ")
    
    if option == '1':
        calculator()
    elif option == '2':
        conversion_calculator()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()