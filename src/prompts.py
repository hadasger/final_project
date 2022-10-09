

from pickletools import int4
from .validations import (validate_age, validate_id_number, validate_name,
                             validate_phone_number)
def prompt_employee_name ():
    print('Enter an employee\'s name:')
    #check if the user entered a valid name
    while True:
        emp_name = input()
        if validate_name(emp_name) == True:
            return emp_name
        else:
            print ('Enter a valid employee\'s name:')


def prompt_employee_id (emp_name):
    print(f'Enter {emp_name}\'s ID number:')
    #check if the user entered a valid ID number
    while True:
        emp_id = input()
        if validate_id_number(emp_id) == True:
            return emp_id
        elif len(emp_id) != 9:
            print('Enter a 9 digits employee\'s ID mumber:')
        else:
            print ('Enter a valid employee\'s ID number:')


def prompt_employee_phone_number (emp_name):
    print(f'Enter {emp_name}\'s phone number (digits only):')
    #check if the user entered a valid phonenumber
    while True:
        emp_phone_number = input()
        if validate_phone_number(emp_phone_number) == True:
            return emp_phone_number
        elif len(emp_phone_number)==10:
            print('Enter a 10 digits employee\'s phone mumber:')
        else:
            print ('Enter a valid employee\'s phone number:')


def prompt_employee_age (emp_name):
    print(f'Enter {emp_name}\'s age:')
    #check if the user entered a valid age
    while True:
        emp_age = input()
        if emp_age.isnumeric():
            emp_age = int(emp_age)
            if validate_age(emp_age) == True:
                return emp_age
            else:
                print('Enter a valid employee\'s age between 21 to 67:')
        else:
            print ('Enter a valid employee\'s age:')


def prompt_employee_new_file():
    print('Enter a file of employees data name:')
    file_of_emp = input()
    return file_of_emp

def delete_employee_from_file (df_employees):
    print('Enter an employee\'s ID number to delete:')
    #check if the user entered a valid ID number
    while True:
        emp_id = input()
        if validate_id_number(emp_id) == True:
            #check if the id number exist in dataframe
            if (df_employees['ID'].eq(int(emp_id))).any() == True:
                return df_employees.drop(df_employees.loc[df_employees['ID']== int(emp_id)].index)         
            else:
                print('The ID number doesn\'t exist')
        elif len(emp_id) != 9:
            print('Enter a 9 digits employee\'s ID mumber:')
        else:
            print ('Enter a valid employee\'s ID number:')