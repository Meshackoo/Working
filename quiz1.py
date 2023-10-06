import datetime

def calculate_age(year_of_birth):
    current_date = datetime.date.today()
    birth_date = datetime.date(year_of_birth, 1, 1)  # Assuming January 1st as the birth date
    
    # Calculate the age in years
    age_in_years = current_date.year - birth_date.year
    
    # Calculate the age in months and adjust if the current month is before the birth month
    age_in_months = current_date.month - birth_date.month
    if current_date.month < birth_date.month:
        age_in_years -= 1
        age_in_months = 12 - birth_date.month + current_date.month
    
    # Calculate the age in days and adjust if the current day is before the birth day
    age_in_days = current_date.day - birth_date.day
    if current_date.day < birth_date.day:
        age_in_months -= 1
        if current_date.month == 1:
            age_in_years -= 1
            age_in_months = 11
        else:
            month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            age_in_days = month_lengths[current_date.month-2] - birth_date.day + current_date.day

    return age_in_years, age_in_months, age_in_days

# Usage example
year_of_birth = int(input("Enter the year of birth: "))
age_in_years, age_in_months, age_in_days = calculate_age(year_of_birth)

print("Age: {} years, {} months, {} days".format(age_in_years, age_in_months, age_in_days))