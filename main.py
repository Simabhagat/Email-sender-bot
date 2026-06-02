from Errors import Data_Validation
import mailer, Templates
import getpass, sys
import utils



     

def main():
    
        try:
            
            print("-----------admin side-----------")
            
            from_mail = input("Enter admin email:")
            utils.validate_email(from_mail)
            password = getpass.getpass("Enter admin password: ")
            
            print("-----------Client side-----------")
            
            to_mail = input("Enter your email address: ")
            utils.validate_email(to_mail)
            """_______________________send_OTP___________________"""
            
            result = mailer.send_OTP(from_mail, password, to_mail)
            if not result:
                print("Failed to send OTP")
            else:
                OTP_from_server, valid_for = result
            """_____________verify_OTP___________________"""
            
            result = utils.verify_otp(OTP_from_server, valid_for)
            if result:
                print("OTP verification successful")
                sys.exit()
            else: 
                choice = input("Do you wish to resend OTP?(Y/N) ").casefold()
                utils.validate_choice(choice)
                if choice == "y" or choice == "Yes":
                    mailer.send_OTP(from_mail, password, to_mail)
                else:
                    sys.quit()
                
        except Data_Validation as e:
            print(e)
        
        except Exception as e:
            print(e)
    
if __name__ == "__main__":
    main()