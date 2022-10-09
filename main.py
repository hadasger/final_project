import string

import pandas as pd
from src.prompts import delete_employee_from_file, prompt_employee_new_file, prompt_employee_age, prompt_employee_id, prompt_employee_name, prompt_employee_phone_number

from src.validations import (validate_age, validate_employee_file, validate_id_number, validate_name,
                             validate_phone_number)

#creating file of employees data
df_employees = pd.read_csv('./employees_data.csv')

#asking the user to type a new employee data

employee_name = prompt_employee_name ()

employee_id = prompt_employee_id (employee_name)

employee_phone_number = prompt_employee_phone_number (employee_name)

employee_age = prompt_employee_age (employee_name)

#add the new employee data to the employee_data file
employee_details = [employee_id, employee_name, employee_phone_number, employee_age]
df_employees.loc[len(df_employees.index)] = employee_details

# print(df_employees)



#asking the user to type a new file of employees

file_of_employees = prompt_employee_new_file()
df_employee_file = pd.read_csv(file_of_employees)


#check how many employees/rows in the file

row_num_emp_file = len(df_employee_file.axes[0])

# Validate employee file
if validate_employee_file(df_employee_file) == True:
    #add the new employees file to the employee_data file
    main_employees_data = pd.concat([df_employees, df_employee_file])
else:
    print('Someting went wrong. We didn\'t add your file to the main data frame')


#delete the employee from the file
main_employees_data = delete_employee_from_file(main_employees_data)

print(main_employees_data)

