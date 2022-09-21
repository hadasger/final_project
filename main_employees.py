import string
import pandas as pd

#creating file of employees data
df_employees = pd.read_csv('./employees_data.csv')
df_employees.head()
# print(df_employees)



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
