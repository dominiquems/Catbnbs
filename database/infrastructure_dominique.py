from pymongo import MongoClient

client = MongoClient("mongodb+srv://dominiquems:Domi-2492@cluster0.xxqtl.azure.mongodb.net/test.catbnb?retryWrites=true&w=majority")

db = client.get_database("catbnb")
records = db.student_records


def check_record(entry: dict) -> bool:
    if records.count_documents(entry) > 0:
        return True
    return False


def insert_record(entry: dict):
    if not check_record(entry):
        records.insert_one(entry)
        print(f"{entry['name'].capitalize()} is now member of Catbnb!")
    else:
        print(f"{entry['name'].capitalize()} is already member of Catbnb!")


def get_info():
    name = input("What is the name? ").strip().lower()
    age = input("What is the age? ").strip()
    gender = input("What is the gender? ").strip().lower()
    color = input("What is the color? ").strip().lower()
    return {"name": name, "age": int(age), "gender": gender, "color": color}


def delete_record(entry: dict):
    if check_record(entry[entry]):
        records.deleteOne(entry)
        print(f"{entry['name'].capitalize()} is no longer member of Catbnb!")
    else:
        print(f"Cannot find a kiddy named {entry['name'].capitalize()}!")


def main():

    choice = input("Would you like to [a]dd, [u]pdate or [r]emove a cat? ").lower().strip()

    if choice == 'a':
        insert_record(get_info())
    elif choice == 'u':
        pass
    elif choice == 'r':
        delete_record(get_info())
    else:
        exit(0)

main()
