
#functions to check validation of input employees data

def validate_name(emp_name: str):
    return emp_name.isalpha()

def validate_id_number(emp_id: str):
    return (emp_id.isnumeric) and (len(emp_id) == 9)

def validate_phone_number(emp_phone_number: str):
    return (emp_phone_number.isnumeric) and (len(emp_phone_number) == 10)

def validate_age(emp_age: int):
    return (isinstance(emp_age, int)) and (emp_age >= 21) and (emp_age <= 67)


# Check validation of input file of employees data

def validate_employee_file(df_emp_file): 
    
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
                                print('Age in row #', row, 'isn\'t valid')
                    else:
                        print('Phone number in row #', row, 'isn\'t valid')
            else:
                print('Name in row #', row, 'isn\'t valid')
        else:
            print ('ID in row #', row, 'isn\'t valid')
    
    return valid_rows == row_num_emp_file
