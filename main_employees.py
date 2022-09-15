import pandas as pd

#creating file of employees data
df_employees = pd.read_csv('./employees_data.csv')
df_employees.head()

#asking the user to type a new employee data

print('Enter an employee\'s name:')
#check if the user entered a valid name
while True:
    emp_name = input()
    if emp_name.isalpha():
        break
    else:
        print ('Enter a valid employee\'s name:')
        

print(f'Enter {emp_name}\'s ID number:')
#check if the user entered a valid ID number
while True:
    emp_id = input()
    if emp_id.isnumeric():
        if len(emp_id)==9:
            break
        else:
            print('Enter a 9 digits employee\'s ID mumber:')
    else:
        print ('Enter a valid employee\'s ID number:')


print(f'Enter {emp_name}\'s phone number (digits only):')
#check if the user entered a valid phonenumber
while True:
    emp_phone_number = input()
    if emp_phone_number.isnumeric():
        if len(emp_phone_number)==10:
            break
        else:
            print('Enter a 10 digits employee\'s phone mumber:')
    else:
        print ('Enter a valid employee\'s phone number:')

print(f'Enter {emp_name}\'s age:')
#check if the user entered a valid age
while True:
    emp_age = input()
    if emp_age.isnumeric():
        emp_age = int(emp_age)
        if (emp_age >= 21) and (emp_age <= 67):
            break
        else:
            print('Enter a valid employee\'s age between 21 to 67:')
    else:
        print ('Enter a valid employee\'s age:')

#add the new employee data to the employee_data file
employee_details = [emp_id, emp_name, emp_phone_number, emp_age]
df_employees.loc[len(df_employees.index)] = employee_details


