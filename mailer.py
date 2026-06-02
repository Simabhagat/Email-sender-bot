import smtplib
import utils
import Templates

HOST = "smtp.gmail.com"
PORT = 587

def send_mail(from_mail, password, to_mail, email_body):
    try:
        smtp = smtplib.SMTP(HOST, PORT)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(from_mail, password)
        smtp.sendmail(from_mail, to_mail, email_body)
        return True
    except Exception as e:
        print("Backend Error: ", e)
        return False
    finally:
        smtp.quit()
    
def send_OTP(from_mail, password, to_mail):
    OTP_from_server, valid_for = utils.generate_OTP(5) 
            
    
    name = to_mail.split("@").pop() #["test", "mail.com"]
    email_body = Templates.render_otp_email(name, OTP_from_server)
    result = send_mail(from_mail, password, to_mail, email_body)
    if result:
        print("An OTP has been sent to your email!")
        return OTP_from_server, valid_for
    else:
        print("Email sending failed!")
        return None
