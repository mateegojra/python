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
    for f in res:
        print(f[1]+"------"+f[2])
def delFriend(fid):
    q = "DELETE FROM myfriends WHERE f_id = %s"
    v = (fid,)
    handler.execute(q,v)
    mydb.commit()
    show()
def update():
    oname = input("Enter Old Name: ")
    nname = input("Enter New Name: ")
    ncity = input("Enter His/Her City: ")
    q = "UPDATE myfriends SET full_name = %s, city = %s WHERE full_name = %s"
    p = (nname, ncity, oname)
    handler.execute(q,p)
    mydb.commit()
    show()
def mainMenue():
    clear()
    print("******Main Menue******")
    print("1- Add New Record\n2- Show Record\n3- Del a Friend\n4- Update Friend's List")
    what = input("Enter Your Choice: ")
    if what == str('1'):
        AddNew()
        mainMenue()
    elif what == str('2'):
        show()
        mainMenue()
    elif what == str('3'):
        fid = input("Enter Friend's ID to Delete? ")
        delFriend(fid)
        mainMenue()
    elif what == str('4'):
        update()
        mainMenue()
    else:
        print("Invalid Option")
        mainMenue()
mainMenue()
print("***********END************")
