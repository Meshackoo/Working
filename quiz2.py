def calculate_tip(total_bill, tip_percentage, num_people):
    # Calculate the tip amount
    tip_amount = (total_bill * tip_percentage) / 100
      
    # Calculate the total amount including the tip
    total_amount = total_bill + tip_amount
    
    # Calculate the amount each person should pay
    amount_per_person = total_amount / num_people

    return round(amount_per_person, 2)

# Usage example
total_bill = float(input("Enter the total bill amount: "))
tip_percentage = int(input("Enter the tip percentage (10, 12, or 15): "))
num_people = int(input("Enter the number of people splitting the bill: "))

amount_per_person = calculate_tip(total_bill, tip_percentage, num_people)
print("Each person should pay: $", amount_per_person)