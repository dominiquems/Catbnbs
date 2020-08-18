from database import infrastructure_dominique
from cryptography.fernet import Fernet


def create_account(records, entry):
   records.insert_one(entry)

def get_info_owner():
   first_name = input("Insert first name: ")
   last_name = input("Insert last name: ")
   email = input("Insert e-mail address: ")
   region = input("Insert city name: ")
   phone = input("Insert phone number: ")
   password = encrypt_password(input("Insert password: ").encode())
   return {"first_name": first_name, "last_name": last_name, "email": email, "region": region, "phone": phone,
           "password": password}


def encrypt_password(password):
   key = b'WJbMOPcP1U29mRiLEXy5Z-4DaRGrZO1C7orkT_GmLg0='
   cipher_suite = Fernet(key)
   encoded_text = cipher_suite.encrypt(password)
   #decoded_text = cipher_suite.decrypt(encoded_text)
   return encoded_text


def main(choice, db):

   records = db.owners

   if choice == 'c':
      create_account(records, get_info_owner())
