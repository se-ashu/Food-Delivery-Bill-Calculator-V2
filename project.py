print("Welcome to Food Delivery Bill Calculator!")

total_bill = 0

while True:
    print("\nMenu:")
    print("1. Burger - ₹120")
    print("2. Pizza - ₹250")
    print("3. Sandwich - ₹100")
    print("4. Pasta - ₹180")
    print("5. Exit and Calculate Bill")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        qty = int(input("Enter quantity: "))
        total_bill += 120 * qty
    elif choice == 2:
        qty = int(input("Enter quantity: "))
        total_bill += 250 * qty
    elif choice == 3:
        qty = int(input("Enter quantity: "))
        total_bill += 100 * qty
    elif choice == 4:
        qty = int(input("Enter quantity: "))
        total_bill += 180 * qty
    elif choice == 5:
        break
    else:
        print("Invalid choice! Please select from the menu.")


if total_bill > 500:
    delivery_charge = 0
    print("\nYou got FREE delivery!")
else:
    delivery_charge = 50
    print("\nDelivery charge ₹50 added.")

final_bill = total_bill + delivery_charge


if final_bill > 1000:
    discount = final_bill * 0.1   
    print("You got a 10% discount!")
else:
    discount = 0

final_bill -= discount

print("\n------------------------------")
print(f"Total Food Bill : ₹{total_bill}")
print(f"Delivery Charge : ₹{delivery_charge}")
print(f"Discount        : ₹{discount:.2f}")
print("------------------------------")
print(f"Final Amount to Pay: ₹{final_bill:.2f}")
print("------------------------------")
print("Thank you for ordering with us!")

    
    