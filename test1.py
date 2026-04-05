#Create variables to store a person's name (string), age (integer), height in meters (float), 
# and whether they are a student (boolean). Print all four values in a single print() statement.'''
import datetime


name = "Alice"
age = 30
height = 1.65
is_student = True
print(f"Name:{name} , Age:{age} , Height:{height} , Is Student:{is_student}")

#Task 2: String Formatting Using the variables from Task 1, print a sentence in the following format:
#  Name: <name> | Age: <age> | Height: <height> | Student: <is_student>

print(f"Name: {name} | Age: {age} | Height: {height} | Student: {is_student}")

# Arithmetic Operations Using the age variable, calculate and print:

birth_date = datetime.date(1993, 5, 21)
current_Date = datetime.date.today()
proper_age = current_Date.year - birth_date.year
current_age_in_Months = proper_age * 12
current_age_in_Days = proper_age * 365
age = proper_age// 7 
age_raised_to_power_of_2 = proper_age ** 2
print(f"Current Age in Years: {proper_age}")
print(f"Current Age in Days: {current_age_in_Days}")
print(f"Current Age in Months: {current_age_in_Months}")
print(f"Current Age in Years (Squared): {age_raised_to_power_of_2}")
