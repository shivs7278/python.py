import os.path

def checkExistence():
    if os.path.exists("info.txt"):
        pass
    else:
        file = open("info.txt", 'w')
        file.close()

def appendNew():
    file = open("info.txt", 'a')

    print()
    print()

    userName = input("Please enter the user name: ")
    password = input("Please enter the password here: ")
    website = input("Please enter the website address here: ")

    print()
    print()

    usrnm = "UserName: " + userName + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close()

def readPasswords():
    file = open('info.txt', 'r')
    content = file.read()
    file.close()
    print(content)

def main():
    checkExistence()
    while True:
        print("1. Add new password")
        print("2. View passwords")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            appendNew()
        elif choice == "2":
            readPasswords()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()