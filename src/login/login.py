from datetime import datetime


def login():
    print("please enter your username")
    user_nm = input("Enter here: ")
    pssd_wr = (input("enter the password"))+'\n'
    try:
        usernm = user_nm+" task.txt"
        f_ = open(usernm, 'r')

        k = f_.readlines(0)[0]
        f_.close()

        if pssd_wr == k:
            print("1--to view your data \n2--To add task \n3--Update\
                task status \n4--View task status")
            a = input()

            if a == '1':
                view_data(user_nm)
            elif a == '2':
                task_information(user_nm)
            elif a == '3':
                task_update(user_nm)
            elif a == '4':
                task_update_viewer(user_nm)
            else:
                print("wrong input")

        else:
            print("SIR YOUR PASSWORD OR USERNAME IS WRONG , Plz enter Again")
            login()
    except Exception as e:
        print(e)
        login()

def view_data(username):
    ff = open(username, 'r')
    print(ff.read())
    ff.close()

def task_information(username):
    print("Sir enter n.o of task you want to ADD")
    j = int(input())
    f1 = open(username, 'a')
    for i in range(1, j+1):
        task = input("enter the task")
        target = input("enter the target")
        pp = "TASK "+str(i)+" :"
        qq = "TARGET "+str(i)+" :"

        f1.write(pp)
        f1.write(task)
        f1.write('\n')
        f1.write(qq)
        f1.write(target)
        f1.write('\n')

        print("Do u want to stop press space bar otherwise enter")
        s = input()
        if s == ' ':
            break
    f1.close

def task_update(username):
    username = username+" TASK.txt"
    print("Please enter the tasks which are completed ")
     
    task_completed = input()
    print("Enter task which are still not started by you")
     
    task_not_started = input()
    print("Enter task which you are doing")
     
    task_ongoing = input()
    fw = open(username, 'a')
    DT = str(datetime.datetime.now())
     
    fw.write(DT)
    fw.write("\n")
    fw.write("COMPLETED TASK \n")
    fw.write(task_completed)
    fw.write("\n")
    fw.write("ONGOING TASK \n")
    fw.write(task_ongoing)
    fw.write("\n")
    fw.write("NOT YET STARTED\n")
    fw.write(task_not_started)
    fw.write("\n")

def task_update_viewer(username):
    ussnm = username+" TASK.txt"
    o = open(ussnm, 'r')
    print(o.read())
    o.close()