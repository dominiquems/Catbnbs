from pymongo import MongoClient

client = MongoClient("mongodb+srv://dominiquems:Domi-2492@cluster0.xxqtl.azure.mongodb.net/catbnb?retryWrites=true&w=majority")

db = client.get_database("catbnb")
records = db.cats


def check_record(entry: dict, db) -> bool:
    if db.count_documents(entry) > 0:
        return True
    return False


def insert_record(entry: dict, db):
    if not check_record(entry, db):
        db.insert_one(entry)
        print("Inserted entry successfully...")
    else:
        print("Could not insert entry because it already exists...")


""""""
def get_info_cat():
    name = input("What is the name? ").strip().lower()
    age = input("What is the age? ").strip()
    gender = input("What is the gender? ").strip().lower()
    color = input("What is the color? ").strip().lower()
    return {"name": name, "age": int(age), "gender": gender, "color": color}


def delete_record(entry: dict):
    if check_record(entry[entry]):
        records.delete_one(entry)
        print("Deleted entry successfully...")
    else:
        print("Could not find entry...")


# def main():
#
#     choice = input("Would you like to [a]dd, [u]pdate or [r]emove a cat? ").lower().strip()
#
#     if choice == 'a':
#         insert_record(get_info_cat())
#     elif choice == 'u':
#         pass
#     elif choice == 'r':
#         delete_record(get_info_cat())
#     else:
#         exit(0)
#
# main()

