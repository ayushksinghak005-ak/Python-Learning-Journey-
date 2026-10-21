bikes = ["splendor", "pulsar", "bullet"]
bike_prices = (80000, 150000, 220000)
print("---  hamare digital shoroom me aapka swagat hai---")
print("hamare paas ye bike hai:", bikes)
user_choice = input("\n aapako kon si bike pasand hai? (naam likhe): ")
if user_choice.lower() == "splendor":
    print(f"Splendor ki kimat ₹{bike_prices[0]} hai।")
elif user_choice.lower() == "pulsar":
    print(f"Pulsar ki kimat ₹{bike_prices[1]} hai।")
elif user_choice.lower() == "bullet":
    print(f"Bullet ki kimat ₹{bike_prices[2]} hai।")

else:
    print("Yeh bike hamare paas nahi hai!")
