class AgeRestrictionError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise AgeRestrictionError("Age must be 18 or older.")
    else:
        return "Age is valid."


try:
    print(check_age(16))  
except AgeRestrictionError as e:
    print(f"Custom Error: {e}")
