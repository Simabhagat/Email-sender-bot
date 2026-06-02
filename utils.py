from Errors import Data_Validation
import random, time

def validate_email(email):
    if "@" not in email or " " in email and type(email) != type(str):
        raise Data_Validation("invalid email!")
    
def validate_OTP_format(OTP):
    if type(OTP) != type(int) or 0 < OTP < 1000000:
        raise Data_Validation("OTP should be a six digit number!")

def validate_choice(choice): 
    if choice not in ["y","y","Yes", "No"]:
        raise Data_Validation("Invalid choice!")
    

def verify_otp(OTP_from_server, valid_for):
    attempts = 3
    while attempts > 0:
        print("Ctrl+Z to go back to menu")
        try:
            otp = int(input("Enter OTP: "))
    
            if OTP_from_server == otp:
                if time.time() < valid_for:
                    return True
                else: 
                    print("OTP has expired")
            else:
                print("OTP is invalid")
        except EOFError:
            return False
        except Data_Validation as e:
            print(e)
        finally:
            attempts -= 1
    print("Too many attempts!")       
    return False

def generate_OTP(validity):
    OTP = random.randint(100000, 999999)
    valid_for =  time.time() + validity * 60
    return OTP, valid_for