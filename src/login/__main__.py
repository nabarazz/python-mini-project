
from login import login
from sign_up import signup


if __name__ == '__main__':
    print("WELCOME TO ANURAG`S TASK MANAGER")
    print("sir are you new to this software")
    a = int(input("Type 1 if new otherwise press 0 ::"))
     
    if a == 1:
        signup()
    elif a == 0:
        login()
    else:
        print("You have provided wrong input !")
