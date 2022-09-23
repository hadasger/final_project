
#functions to check validation of input employees data

def validate_name(emp_name: str):
    return emp_name.isalpha()

def validate_id_number(emp_id: str):
    return (emp_id.isnumeric) and (len(emp_id) == 9)

def validate_phone_number(emp_phone_number: str):
    return (emp_phone_number.isnumeric) and (len(emp_phone_number) == 10)

def validate_age(emp_age: int):
    return (isinstance(emp_age, int)) and (emp_age >= 21) and (emp_age <= 67)