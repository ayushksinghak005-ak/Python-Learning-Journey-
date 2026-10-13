bikes = ["splendor", "pulsar", "bullet"]

# 2. बाइकों की फिक्स कीमतें (Tuple)
# splendor = index 0, pulsar = index 1, bullet = index 2
bike_prices = (80000, 150000, 220000)

print("---  हमारे डिजिटल बाइक शोरूम में आपका स्वागत है ---")
print("हमारे पास ये बाइक उपलब्ध हैं:", bikes)

# 3. यूजर से इनपुट लिया (Input)
user_choice = input("\nआपको कौन सी बाइक पसंद है? (नाम लिखें): ")

# 4. फैसले लेने का लॉजिक (if-elif-else) और टुपल इंडेक्स का उपयोग
if user_choice.lower() == "splendor":
    print(f"Splendor की कीमत ₹{bike_prices[0]} है।")

elif user_choice.lower() == "pulsar":
    print(f"Pulsar की कीमत ₹{bike_prices[1]} है।")

elif user_choice.lower() == "bullet":
    print(f"Bullet की कीमत ₹{bike_prices[2]} है।")

else:
    print("Yeh bike hamare paas nahi hai!")
