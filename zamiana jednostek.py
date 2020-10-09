# Miles to Kilometers
# Celsius Celsius = (var1 - 32) * 5/9
# Gallons to liters Gallons = 3.6
# Pounds to kilograms Pounds = 0.45
# Inches to centimeters Inches = 2.54


def intro():
    print("Welcome! This program will convert measures for you.")
    main()


def main():
    print("Select operation:")
    print("1.Miles to Kilometers")
    print("2.Fahrenheit to Celsius")
    print("3.Gallons to liters")
    print("4.Pounds to kilograms")
    print("5.Inches to centimeters")

    choice = input("Enter your choice by number: ")

    if choice == '1':
        convertmk()
    elif choice == '2':
        convercf()
    elif choice == '3':
        convertgl()
    elif choice == '4':
        convertpk()
    elif choice == '5':
        convertic()
    else:
        print("Error")
        main()


def convertmk():
    input_m = float(input("Miles: "))
    m_conv = 1.6 * input_m
    print("Kilometers: %f\n" % m_conv)
    res()


def convercf():
    input_f = float(input("Fahrenheit: "))
    f_conv = (input_f - 32) * 5 / 9
    print("Celcius: %.2f\n" % f_conv)
    res()


def convertgl():
    input_g = float(input("Gallons: "))
    g_conv = input_g * 3.6
    print("Liters: %.2f\n" % g_conv)
    res()


def convertpk():
    input_p = float(input("Pounds: "))
    p_conv = input_p * 0.45
    print("Kilograms: %.2f\n" % p_conv)
    res()


def convertic():
    input_cm = float(input("Inches: "))
    inches_conv = input_cm * 2.54
    print("Centimeters: %.2f\n" % inches_conv)
    res()


def res():
    restart = str(input("Do you wish to make another conversion? [y]Yes or [n]no: "))
    if restart == 'y':
        main()
    elif restart == 'n':
        end()
    else:
        print("I didn't quite understand that answer. Terminating.")
        main()


def end():
    print("This program will close.")
    exit()


intro()
