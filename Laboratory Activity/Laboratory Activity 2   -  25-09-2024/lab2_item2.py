total_amount = float(input("Enter the total purchase amount: "))

print(f"Initial Purchase Amount: {total_amount:.2f}")

if total_amount > 5000:
    discount_percentage = 0.10
else:
    discount_percentage = 0.05

discount_amount = total_amount * discount_percentage

print(f"Discount: {discount_amount:.2f}")

final_amount = total_amount - discount_amount

print(f"Final Price: {final_amount:.2f}")

while True:
    response = input("Do you want to try again? (yes/no): ")
    if response == 'yes':
        total_amount = float(input("Enter the total purchase amount: "))
        print(f"Initial Purchase Amount: {total_amount:.2f}")
        if total_amount > 5000:
            discount_percentage = 0.10
        else:
            discount_percentage = 0.05
        discount_amount = total_amount * discount_percentage
        print(f"Discount: {discount_amount:.2f}")
        final_amount = total_amount - discount_amount
        print(f"Final Price: {final_amount:.2f}")
    elif response == 'no':
        print("Thank you!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")