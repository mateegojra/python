import mysql.connector
import os

clear = lambda: os.system('cls')

mydb = mysql.connector.connect(host= "localhost", user="root", password="", database="python_practice")

handler = mydb.cursor()

#handler.execute("CREATE TABLE myFriends(f_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, full_name VARCHAR(30), city VARCHAR(20), added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)")

def AddNew():
    n = input("Enter Friend's Name: ")
    c = input("Enter City: ")
    q = "INSERT INTO myfriends(full_name, city) VALUES(%s, %s)"
    v = (n,c)
    handler.execute(q,v)
    mydb.commit()
def show():
    q = "SELECT * FROM myfriends"
    handler.execute(q)
    res = handler.fetchall()
    print(res)
def mainMenue():
    clear()
    print("******Main Menue******")
    print("1- Add New Record\n2- Show Record")
    what = input("Enter Your Choice: ")
    if what == str('1'):
        AddNew()
        mainMenue()
    elif what == str('2'):
        show()
        mainMenue()
    else:
        print("Invalid Option")
        mainMenue()
mainMenue()
print("***********END************")
