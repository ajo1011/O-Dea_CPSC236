#!/usr/bin/env python
# coding: utf-8

# # Chapter 2 - How to write your first program

# ## 2.1 Student Registration
# Create a program that allows a student to complete a registration form and displays a completion message that includes the user’s full name and a temporary password.
# 
# ### Console:
# ```powershell
# Registration Form
# 
# First Name: Eric
# Last Name: Idle
# Birth Year: 1934
# 
# Welcome Eric Idle!
# Your registration is complete!
# Your temporary password is: Eric*1934
# ```
# 
# ### Specifications:
# - The user’s full name consists of the user’s first name, a space, and the user’s last name.
# - The temporary password consists of the user’s first name, an asterisk (*), and the user’s birth year.
# - Assume the user will enter valid data.
# 

# In[41]:


print("Registration Form")
print()
first_name = input("First Name: ")
last_name = input("Last Name: ")
birth_year = input("Birth Year: ")


print()
print("Welcome" " " + first_name + " " + last_name + "!")
print("Your registration is complete!")
print("Your temporary password is:" + " " + first_name + "*" + birth_year)


# ## 2.2 - Pay Check Calculator
# Create a program that calculates a user’s weekly gross and take-home pay.
# 
# ### Console
# ```powershell
# Pay Check Calculator
# 
# Hours Worked: 35
# Hourly Pay Rate: 14.50
# 
# Gross Pay: 507.5
# Tax Rate: 18%
# Tax Amount: 91.35
# Take Home Pay: 416.15
# ```
# 
# ### Specifications:
# - The formula for calculating gross pay is:
# `gross pay = hours worked * hourly rate`
# - The formula for calculating tax amount is:
# `tax amount = gross pay * (tax rate / 100)`
# - The formula for calculating take home pay is:
# `take home pay = gross pay – tax amount`
# - The tax rate should be 18%, but the program should store the tax rate in a variable so that you can easily change the tax rate later, just by changing the value that’s stored in the variable.
# - The program should accept decimal entries like 35.5 and 14.25.
# - Assume the user will enter valid data.
# - The program should round the results to a maximum of two decimal places.
# 

# In[15]:


def pay_check_calculator():
    print("Pay Check Calculator\n")
    
    # Get user input for hours worked and hourly pay rate
    hours_worked = float(input("Hours Worked: "))
    hourly_pay_rate = float(input("Hourly Pay Rate: "))
    
    # Tax rate (18%)
    tax_rate = 18
    
    # Calculate gross pay
    gross_pay = round(hours_worked * hourly_pay_rate, 2)
    
    # Calculate tax amount
    tax_amount = round(gross_pay * (tax_rate / 100), 2)
    
    # Calculate take home pay
    take_home_pay = round(gross_pay - tax_amount, 2)
    
    # Display the result
    print("\nGross Pay:", gross_pay)
    print("Tax Rate:", tax_rate, "%")
    print("Tax Amount:", tax_amount)
    print("Take Home Pay:", take_home_pay)

if __name__ == "__main__":
    pay_check_calculator()




# ## 2.3 - Travel Time Calculator
# Create a program that calculates the estimated hours and minutes for a trip.
# 
# ### Console
# ```powershell
# Travel Time Calculator
# 
# Enter Miles: 200
# Enter Miles per Hour: 65
# 
# Estimated Travel Time
# Hours: 3
# Minutes: 5
# ```
# 
# ### Specifications
# - The program should only accept integer entries like 200 and 65.
# - Assume that the user will enter valid data.
# 
# ### Hint
# - Use integers with the integer division and modulus operators to get hours and minutes.

# In[14]:


def travel_time_calculator():
    print("Travel Time Calculator\n")
    
   
    miles = int(input("Enter Miles: "))
    speed = int(input("Enter Miles per Hour: "))
    
    
    hours = miles // speed
    minutes = miles % speed * 60 // speed
    

    print("\nEstimated Travel Time")
    print(f"Hours: {hours}")
    print(f"Minutes: {minutes}")

if __name__ == "__main__":
    travel_time_calculator()

