import string
import pandas as pd

#creating file of employees data
df_employees = pd.read_csv('./employees_data.csv')
df_employees.head()



#functions to check validation of input employees data

def validate_name(emp_name: str):
    return emp_name.isalpha()

def validate_id_number(emp_id: str):
    return (emp_id.isnumeric) and (len(emp_id) == 9)

def validate_phone_number(emp_phone_number: str):
    return (emp_phone_number.isnumeric) and (len(emp_phone_number) == 10)

def validate_age(emp_age: int):
    return (isinstance(emp_age, int)) and (emp_age >= 21) and (emp_age <= 67)
      



#asking the user to type a new employee data

print('Enter an employee\'s name:')
#check if the user entered a valid name
while True:
    emp_name = input()
    if validate_name(emp_name) == True:
        break
    else:
        print ('Enter a valid employee\'s name:')
        

print(f'Enter {emp_name}\'s ID number:')
#check if the user entered a valid ID number
while True:
    emp_id = input()
    if validate_id_number(emp_id) == True:
            break
    elif len(emp_id) != 9:
            print('Enter a 9 digits employee\'s ID mumber:')
    else:
        print ('Enter a valid employee\'s ID number:')


print(f'Enter {emp_name}\'s phone number (digits only):')
#check if the user entered a valid phonenumber
while True:
    emp_phone_number = input()
    if validate_phone_number(emp_phone_number) == True:
        break
    elif len(emp_phone_number)==10:
        print('Enter a 10 digits employee\'s phone mumber:')
    else:
        print ('Enter a valid employee\'s phone number:')

print(f'Enter {emp_name}\'s age:')
#check if the user entered a valid age
while True:
    emp_age = input()
    if emp_age.isnumeric():
        emp_age = int(emp_age)
        if validate_age(emp_age) == True:
            break
        else:
            print('Enter a valid employee\'s age between 21 to 67:')
    else:
        print ('Enter a valid employee\'s age:')

#add the new employee data to the employee_data file
employee_details = [emp_id, emp_name, emp_phone_number, emp_age]
df_employees.loc[len(df_employees.index)] = employee_details

#asking the user to type a new file of employees

print('Enter a file of employees data name:')
file_of_employees = input()

#check how many employees/rows in the file



