print("----------------------------------")
print(" Welcome to Python Pizza Delivery ")
print("----------------------------------")

#  Get pizza size
size = input("Enter pizza size (small/large): ").lower()

if size == "small":
    base_price = 8
elif size == "large":
    base_price = 12
else:
    print("Invalid pizza size selected.")
    exit()

# Get number of toppings
try:
    toppings = int(input("Enter number of additional toppings: "))
    if toppings < 0:
        print("Toppings cannot be negative.")
        exit()
except ValueError:
    print("Please enter a valid number for toppings.")
    exit()

topping_cost = toppings * 1

#  Get delivery distance
try:
    miles = float(input("Enter delivery distance in miles: "))
    if miles < 0:
        print("Distance cannot be negative.")
        exit()
except ValueError:
    print("Please enter a valid distance.")
    exit()

# Delivery fee calculation
if miles <= 5:
    delivery_fee = 2
else:
    delivery_fee = 2 + (miles - 5) * 1

# Calculate total
total_cost = base_price + topping_cost + delivery_fee

# Display result
print("\n------ Order Summary ------")
print(f"Pizza Size: {size.capitalize()}")
print(f"Base Price: ${base_price}")
print(f"Toppings Cost: ${topping_cost}")
print(f"Delivery Fee: ${delivery_fee}")
print("---------------------------")
print(f"Total Cost: ${total_cost}")