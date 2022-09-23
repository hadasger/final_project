import string

import pandas as pd
from src.prompts import prompt_employee_age, prompt_employee_id, prompt_employee_name, prompt_employee_phone_number

from src.validations import (validate_age, validate_id_number, validate_name,
                             validate_phone_number)

#creating file of employees data
df_employees = pd.read_csv('./employees_data.csv')

#asking the user to type a new employee data

emp_name = prompt_employee_name ()

emp_id = prompt_employee_id (emp_name)

emp_phone_number = prompt_employee_phone_number (emp_name)

emp_age = prompt_employee_age (emp_name)

#add the new employee data to the employee_data file
employee_details = [emp_id, emp_name, emp_phone_number, emp_age]
df_employees.loc[len(df_employees.index)] = employee_details

# print(df_employees)



#asking the user to type a new file of employees

print('Enter a file of employees data name:')
file_of_emp = input()
df_emp_file = pd.read_csv(file_of_emp)
df_emp_file.head()
# print(df_emp_file)

#check how many employees/rows in the file

row_num_emp_file = len(df_emp_file.axes[0])

#check validation of input employees file
valid_rows = 0
for row in range(row_num_emp_file):
    if validate_id_number(str(df_emp_file.loc[row]['ID'])) == True:
            if validate_name(df_emp_file.loc[row]['Name']) == True:
                    if validate_phone_number(str(df_emp_file.loc[row]['Phone'])) == True:
                            if validate_age(int(df_emp_file.loc[row]['Age'])) == True: 
                                valid_rows +=1
                            else:
                                print('The age column in row number:', row, 'isn\'t valid')
                                break
                    else:
                        print('The phone number column in row number:', row, 'isn\'t valid')
                        break
            else:
                print('The name column in row number:', row, 'isn\'t valid')
                break
    else:
        print ('The ID column in row number:', row, 'isn\'t valid')
        break
    

#add the new employees file to the employee_data file
if valid_rows == row_num_emp_file:
    main_employees_data = pd.concat([df_employees, df_emp_file])
else:
    print('Someting went wrong. We didn\'t add your file to the main data frame')

print(main_employees_data)
