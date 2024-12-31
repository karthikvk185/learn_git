def calculator():
    try:
        conversion_type = input("Choose conversion type (1: Celsius to Fahrenheit, 2: cm to meter, 3: mm to cm, 4: feet to inches, 5: None): ")
        
        if conversion_type == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius} Celsius is {fahrenheit} Fahrenheit")
            return
        elif conversion_type == '2':
            cm = float(input("Enter length in cm: "))
            meters = cm / 100
            print(f"{cm} cm is {meters} meters")
            return
        elif conversion_type == '3':
            mm = float(input("Enter length in mm: "))
            cm = mm / 10
            print(f"{mm} mm is {cm} cm")
            return
        elif conversion_type == '4':
            feet = float(input("Enter length in feet: "))
            inches = feet * 12
            print(f"{feet} feet is {inches} inches")
            return
        elif conversion_type == '5':
            pass
        else:
            print("Invalid option")
            return
        expression = input("Enter a mathematical expression: ")
        result = eval(expression)
        print(f"The result is: {result}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    calculator()


