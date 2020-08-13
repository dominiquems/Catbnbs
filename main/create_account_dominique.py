def main():
    print("Welcome to Catbnb! What would you like to do?\n")
    commands()

    action = input("Make your choice here: ").lower()

    if action == 'c':
        pass
    elif action == 'l':
        pass
    elif action == 'e':
        pass
    elif action == 'b':
        pass
    else:
        print("Please choose a valid option")
        main()


def commands():

    print("[C]reate an account")
    print("[L]ogin to your account")
    print("[E]xit Catbnb")
    print("[B]ook a cage\n")


main()
