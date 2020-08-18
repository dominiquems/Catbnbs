from Catbnbs.database import owner_emile
from pymongo import MongoClient
import time

def main():
    client = MongoClient(
        "mongodb+srv://dominiquems:Domi-2492@cluster0.xxqtl.azure.mongodb.net/catbnb?retryWrites=true&w=majority")
    db = client.get_database('catbnb')

    indicator = True
    while indicator:
        print("Welcome to Catbnb, what would you like to do? ")
        print("[C]reate an owner account ")
        print("[L]ogin to your account ")
        print("[E]xit ")
        choice = input("Specifty your choice: \n").strip().lower()

        if choice == "c" or choice == "l" or choice == "e":
            indicator = False
            if choice == "c":
                owner_emile.main_owner(choice, db)
            elif choice == "l":
                pass

        else:
            print("No valid input, please try again. ")
            indicator = True
            time.sleep(2)

main()