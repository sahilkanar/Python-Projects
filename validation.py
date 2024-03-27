import re
from colorama import Fore,Back,Style



def email_validation(student_email):

    pattern = "^[\\w\\.]+[@]\\w+[.]\\w{2,5}$"

    result = re.match(pattern,student_email)
    if result:
        print(Fore.GREEN+"Email Validated Successfully")
        print(Style.RESET_ALL)
        return True
    else:
        print(Fore.RED+"Invalid Email")
        print(Style.RESET_ALL)
        return False


def phone_no_validation(phone_no):
    pattern = "[7-9]{1}[\\d]{9}$"

    result = re.match(pattern,phone_no)
    if result:
        print(Fore.GREEN+"Phone Number Validated Successfully")
        print(Style.RESET_ALL)
        return True
    else:
        print(Fore.RED+"Invalid Phone Number")
        print(Style.RESET_ALL)
        return False


def password_validation(student_password):
    if len(student_password) < 8:
        print(Fore.RED+"Password too short")
        print(Style.RESET_ALL)
        return False
    else:
        print(Fore.GREEN+"Valid Password")
        print(Style.RESET_ALL)
        return True


