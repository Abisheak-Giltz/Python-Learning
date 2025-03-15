"""
if input is in celsius
if celsius change to farnaheit


if input is in farenheit
if farenheit change to celsius
"""



temp = input("Only degree : ")
degree = input("Celsius/Fahrenheit : ")

fahrenheit = (int(temp) * 9/5) + 32

celsius = (int(temp) - 32) * 5/9

if degree == "Celsius" :
    print(celsius,"C")
elif degree == "Fahrenheit" :
    print(fahrenheit, "F")


