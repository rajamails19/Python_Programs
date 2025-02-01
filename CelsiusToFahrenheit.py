def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

temp = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()

if unit == "C":
    print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")
elif unit == "F":
    print(f"{temp}°F = {fahrenheit_to_celsius(temp)}°C")
else:
    print("Invalid unit")
