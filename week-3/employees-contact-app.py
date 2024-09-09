# TDI Data Science Track
# Week 3: Employee Contact Book Application
# Due Date: August 24, 2024
# Instructions
'''Data Storage:    empID(string or number), 
                    first_name(string), 
                    last_name(string), 
                    phone_number(integer)
                    email(string), 
                    address(string)
   Input Validation: empID, phone_number, and email are unique for every record
                    first_name and last_name must contain only alphabets
                    email must meet standard email structure
                    adress can contain special characters, numbers and alphabets
'''

import re                       # regular expression for email verification
import time                     # time module to delay prompting
import pandas as pd             # pandas to view records as a table

# create an empty list to store employees record as dictionary
contact_book = []

# create a function for print delay
def delay_print (message, delay=1.5):
    print(message)
    time.sleep(delay)

def emp_data():
    # record employee id
    empID = input("What is your employees ID?: ")
    time.sleep(1.5)

    # record first name
    while True:
        first_name = input("What is your first name?: ").title()
        if first_name.isalpha(): # ensure record contains only alphabets
            delay_print("Your first name has been recorded.")
            break # break out of loop if condition is met
        else:
            delay_print("Your first name should only contain alphabetical characters.")

    # record last name
    while True:
        last_name = input("What is your last name?: ").title()
        if last_name.isalpha(): #ensure record contains only aphabets
            delay_print('Your last name has been recorded.')
            break
        else:
            delay_print("Your last name should only contain alphabetical characters.")

    # record phone number
    while True:
        try:
            phone_number = int(input("Enter your phone no: "))
            break #break the loop if input is valid
        except ValueError:
            delay_print('Please enter a valid phone no.')
    delay_print('Your phone number has been recorded.')

    # record email
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'     # standard regex structure for email
    while True:
        email = input("Enter your email: ").lower()
        if (re.fullmatch(regex, email)):
            delay_print("Your email has been recorded.")
            break
        else:
            delay_print("Please enter a valid email.")
 
    # record address
    address = input("Enter your address: ").title()
    delay_print('Your address has been recorded.')
    time.sleep(1.5)
    delay_print("Confirming data validity..")
    time.sleep(2)

    # confirming data validity
    duplicate = False
    for record in contact_book:
        if record['Employee ID'] == empID:
            delay_print(f"Employee ID {empID} is already in the database.")
            duplicate = True
        if record['Phone No'] == phone_number:
            delay_print(f"Phone Number {phone_number} is already in the database.")
            duplicate = True
        if record['Email'] == email:
            delay_print(f"Email {email} exists in database.")
            duplicate = True

    if not duplicate:
        # update contact_book
        contact_book.append({'Employee ID' : empID, 
                             'First Name': first_name, 
                             'Last Name': last_name, 
                             'Phone No': phone_number, 
                             'Email': email, 
                             'Address': address})
        delay_print("Your records has been submitted successfully.")
        # convert contact_book(list of dictionary) to a dataframe to get a tabular view
        df_contact = pd.DataFrame(contact_book)
        # set employees ID as index
        df_contact.set_index('Employee ID', inplace =  True)
        delay_print(df_contact)
        
    else:
        print("Records cannot be uploaded to avoid duplicate data.")

while True:
    emp_data()
    add_data = input("Would you like to add a new employee data? - 'yes' or 'no': ").lower()
    if add_data == 'no':
        delay_print("Thank you for using our contact book application. Bye!")
        break