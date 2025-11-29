def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9


while True:
    print("\nUNIT CONVERT ")
   
    print("1. Kilograms → Pounds")
    print("2. Pounds → Kilograms")
    print("3. Celsius → Fahrenheit")
    print("4. Fahrenheit → Celsius")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("exit bye bye")
        break

    if choice in ['1','2','3','4','5']:
        value = float(input("Enter value to convert: "))

        if choice == '1':
            print(f"{value} kg = {kg_to_pounds(value)} pounds")
        elif choice == '2':
            print(f"{value} pounds = {pounds_to_kg(value)} kg")
        elif choice == '3':
            print(f"{value}°C = {c_to_f(value)}°F")
        elif choice == '4':
            print(f"{value}°F = {f_to_c(value)}°C")

    else:
        print("Invalid choice! Please select between 1–5.")
