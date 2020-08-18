from database import owner_dominique
from pymongo import MongoClient
import time


def is_valid_choice(choice: str):
    if choice == 'c' or choice == 'l' or choice == 'e':
        return True
    else:
        return False


def main():
    client = MongoClient("mongodb+srv://dominiquems:Domi-2492@cluster0.xxqtl.azure.mongodb.net/catbnb?retryWrites=true&w=majority")
    db = client.get_database("catbnb")

    print("Welcome to the Catbnb!")

    running = True
    while running:

        print("[C]reate a new account")
        print("[L]ogin to your account")
        print("[E]exit")
        choice = input("Specify your choice: ").strip().lower()

        if is_valid_choice(choice):
            if choice == 'c':
                owner_dominique.main(choice, db)
                running = False
        else:
            print("Please choose a valid option...\n")
            time.sleep(1.5)

main()
