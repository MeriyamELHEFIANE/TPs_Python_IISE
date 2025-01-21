class NegativeAgeError(Exception):
    pass
def set_age(age):
    if age<0:
        raise NegativeAgeError("L'age ne peut pas etre negatif")
    else:
        print(f"Age defini a : {age}")
try:
    set_age(10)
    
except NegativeAgeError as e:
    print(e)