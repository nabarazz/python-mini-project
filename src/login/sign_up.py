
# ossd means password and ussnm means username
from login import login


def user_information(ussnm, pssd):
    name = input("enter your name: ")
    address = input("your address")
    age = input("your age ")

    ussnm_ = ussnm+" task.txt"
    f = open(ussnm_, 'a')
    f.write(pssd)
    f.write("\nName: ")
    f.write(name)
    f.write('\n')
    f.write("Address :")
 
    f.write(address)
    f.write('\n')
    f.write("Age :")
    f.write(age)
    f.write('\n')
    f.close()

def signup():
    print("please enter the username by which you\ wanna access your account")
    username = input("please enter here: ")
    password = input("enter a password: ")
    user_information(username, password)
    print("sir, please proceed towards log in")
    login()