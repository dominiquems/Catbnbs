from pymongo import MongoClient

client = MongoClient("mongodb+srv://dominiquems:Domi-2492@cluster0.xxqtl.azure.mongodb.net/test?retryWrites=true&w=majority")

db = client.get_database('catbnb')

records = db.student_records

# insert record


def insert_record(entry):
    if not check_record(entry):
        records.insert_one(entry)
        print(f"{entry['name'].capitalize()} has been succesfully added to Catbnb!")
    else:
        print(f"{entry['name'].capitalize()} is already in the database! \n")


def check_record(entry: dict):
    if records.count_documents(entry) > 0:
        return True
    return False


def get_info():
    name = input("What is the name of the cat? \n").strip().lower()
    age = input("What is the age of the cat? \n").strip()
    gender = input("Is the gender [m] or [f]? \n").strip().lower()
    color = input("What is the color of the cat? \n ").strip().lower()
    return {"name" : name, "age" : int(age), "gender" : gender, "color" : color}

def delete_record(entry: dict):
    if not check_record(entry):
        print(f"{entry['name'].capitalize()} is not found in the database.")
        print(entry)
    else:
        records.delete_one(entry)
        print(f"{entry['name'].capitalize()} has been succesfully removed from Catbnb!")

def main():
    choice = input("Do you want to [A]dd, [R]emove or [U]pdate you cat? \n").lower().strip()
    if choice == "a":
        insert_record(get_info())
    elif choice == "r":
        delete_record(get_info())
    elif choice == "p":
        pass
    elif choice == "u":
        pass
    else:
        exit(0)


main()

