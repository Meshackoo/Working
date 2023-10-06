def calculate_bmi(height, weight):
    # Calculate the BMI
    bmi = weight / (height ** 2)

    # Determine the weight status based on BMI
    if bmi < 18.5:
        weight_status = "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        weight_status = "Normal weight"
    else:
        weight_status = "Overweight"

    return bmi, weight_status

# Usage example
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi, weight_status = calculate_bmi(height, weight)
print("Your BMI is:", bmi)
print("Weight Status:", weight_status)