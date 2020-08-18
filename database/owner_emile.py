from cryptography.fernet import Fernet
from Catbnbs.database import infrastructure_emile

def get_info_owner():
    first_name = input("Please enter your first name \n:")
    # last_name =  input("Please enter your last name \n:")
    # email = input("Please enter your email \n:")
    # region = input("Please enter city \n:")
    # phone = input("Please enter phone number \n:")
    password_temp = input("Enter password \n:")
    password_enc = encrypt_password(password_temp.encode())
    return {"first_name" : first_name, "password" : password_enc}

    #return {"first_name" : first_name, "last_name" : last_name, "email" : email,
     #       "region" : region, "phone" : phone, "password" : password_enc}


def encrypt_password(password):
    key = b'WJbMOPcP1U29mRiLEXy5Z-4DaRGrZO1C7orkT_GmLg0='
    cipher_suite = Fernet(key)
    encoded_text = cipher_suite.encrypt(password)
    return encoded_text


def main_owner(choice, db):
    records = db.owners
    if choice == "c":
        infrastructure_emile.insert_record(get_info_owner(), records)

    else:
        pass