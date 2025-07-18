# weather_advice.py

# Ask the user for the weather condition
weather = input("What's the weather like today? (sunny/rainy/cold) ")

# provide recommendation based on the weather condition
if weather == "sunny":
   print("wear a t-shirt and sun glasses. ")
elif weather == "rainy":
   print("Don't forget your umbrella and a raincoat. ")
elif weather == "cold":
   print("Make sure you wear warm coat and a scarf. ")
else:
   print("Sorry, I don't have recommendation for this weather")       