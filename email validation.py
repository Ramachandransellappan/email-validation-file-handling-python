import os
# EMAIL VALIDATION
import re
def register():
    valid_mail = 'a'
    valid_pass = 'a'
    cou = 1
    count = 1
    while cou==1:
        pattern="^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        mail=input("Enter the User ID:")

        if re.search(pattern,mail):
            valid_mail=mail
            r = open('userdetials.txt', 'r')
            userdetails = r.readline()
            if (userdetails.find(mail) == False):
                print("User name exits.. Login:")
                login()
            # print("Mail ID is Valid")
            break
        else:
            print("Mail ID is not valid")

    #PASSWORD VALIDATION

    while count>=1:
        p = input("Enter your password:")
        x = True
        while x:
            if (len(p)<6 or len(p)>12):
                break
            elif not re.search("[a-z]",p):
                break
            elif not re.search("[0-9]",p):
                break
            elif not re.search("[A-Z]",p):
                break
            elif not re.search("[$#@]",p):
                break
            elif re.search("\s",p):
                break
            else:
                valid_pass=p
                x=False
                count=0
                break

        if x:
            print("Not a Valid Password! Re-enter")
            count+=1

    user1=valid_mail,valid_pass
    f=open("userdetials.txt","a")
    f.write(valid_mail + "," + valid_pass + '\n')
    f.close()
    print("Registration Successful !\n --Login--")
    login()

def login():
    name=input("Enter user name:")
    r=open('userdetials.txt','r')
    password = str(input("\nPassword: "))
    userdetails = r.readlines()
    length = len(userdetails)
    r.close()
    with open('userdetials.txt') as fp:
        contents = fp.read()
        status = 0
        if name in contents:
            if password in contents:
                print("\nWelcome Back, " + name)
                print("\nLogout press 1")
                option = int(input("Option : "))
                if option == 1:
                    print("\nSuccessfully logged out...")
                    menu()
            else:
                print("\nPassword entered is wrong")
                print("\n1. For forgot password\n 2.For re-entering password\n")
                res = int(input("Please enter the option : "))
                if res == 1:
                    Forget_password()
                elif res == 2:
                    login()
        else:
            print("\nName not found. Please do registration first.")
    
def Forget_password():
    Username = str(input("Enter your username:"))

    if not len(Username ) < 1:

        if True:
            db = open("userdetials.txt", "r")
            d = []
            f = []
            for i in db:
                a, b = i.split(",")
                b = b.strip()
                c = a, b
                d.append(a)
                f.append(b)
            data = dict(zip(d, f))

            if Username in d:
                print("your password is: ",f[d.index(Username)])
            else:
                print("Username not exist please register")
                register()


        else:
            pass


def menu():
    print("\nWelcome\n 1.Registration\n 2.Login\n 3.Exit\n")
    opt=int(input("Please enter the option : "))
    if opt==1:
        register()
        menu()
    elif opt==2:
        login()
        menu()
    elif opt==3:
        print("Thank You\n")
    else:
        print("\nPlease select the options displayed in the menu\n")
        menu()

menu()





