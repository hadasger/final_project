import pandas as pd

#creating file of employees data
df_employees = pd.read_csv('./employees_data.csv')
df_employees.head()

#asking the user to type a new employee data
print('Enter an employee\'s name:')
emp_name = input()

print(f'Enter {emp_name}\'s ID number:')
emp_id = input()

print(f'Enter {emp_name}\'s phone number:')
emp_phone_number = input()

print(f'Enter {emp_name}\'s age:')
emp_age = input()

#add the new employee data to the employee_data file
employee_details = [emp_id, emp_name, emp_phone_number, emp_age]
df_employees.loc[len(df_employees.index)] = employee_details


