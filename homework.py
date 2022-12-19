baza = {
    "Roman":"login",
    "klmop123":"password"
}
key = None
table = int(input("""
1.open file database.txt ?
2.create a new file ?
"""))
if table == 1:
    login = input("Enter login: ")
    if login in baza.keys():
        password = input("Enter password: ")
        if password in baza.keys():
            f = open("database.txt", "w")
            f.writelines(input())
        else:
            print("Password is not correct")
    else:
        print("Login is not correct")
elif table == 2:
    if key is None:
        login = input("Enter new login: ")
        password = input("Enter new password: ")
        password2 = input("Enter new password again: ")
        while password != password2:
            password = input("Enter new password: ")
            password2 = input("Enter new password again: ")
        else:
            baza.update({
                login:"login",
                password:"password2"
            })  
            key = login
            with open("newfile.txt", "w") as f:
                print("What do you want to record?")
                f.write(input())
