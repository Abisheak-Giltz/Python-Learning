# Weather Clothing Advisor

tempInput = float(input("Hey! What's the weather today? : "))

if tempInput <= 10 :
    print(f"{tempInput}°C is too cold! Wear a some warm clothing and eat some warm foods.")
elif tempInput > 10 and tempInput < 25 :
    print(f"{tempInput}°C is mildy cool! A light Jacket will be enough to go around.")
else :
    print(f"{tempInput}°C is a bit hot to go outside swtich-on the AC and stay inside.")

    
