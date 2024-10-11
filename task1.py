import sqlite3
import re
con=sqlite3.connect("UserDetails.db")
cursor=con.cursor()
cursor.execute('''

CREATE TABLE IF NOT EXISTS users(id INTEGER primary key autoincrement,first_name varchar(50) not null,last_name varchar(50) not null,
phone_number varchar(20) not null, email varchar(30) not null, address varchar(40) not null)''')
def validate_user_details(first_name,last_name,phone_number,email,address):
    if not first_name or not last_name or not address:
        return False,"First Name Last Name and address cannot be empty"
    if not phone_number.isdigit() or len(phone_number)!=10:
        return False,"Phone number must be 10 digit numberic value."
    email_regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex,email):
        return False,"Invalid email format."
    return True,"Validation Successful"

def add_user(first_name,last_name,phone_number,email,address):
    valid,message=validate_user_details(first_name,last_name,phone_number,email,address)
    if valid:
        cursor.execute('''
        INSERT INTO users(first_name,last_name,phone_number,email,address)
        VALUES(?,?,?,?,?)
        ''',(first_name,last_name,phone_number,email,address))
        con.commit()
        return "User Added Successfully"
    else:
        return message
def view_users():
    cursor.execute('''
    SELECT * FROM users
    ''')
    users=cursor.fetchall()
    return users
def update_users(user_id,first_name,last_name,phone_number,email,address):
    valid,message=validate_user_details(first_name,last_name,phone_number,email,address)
    if valid:
        cursor.execute('''
        UPDATE users SET first_name=?,last_name=?,phone_number=?,email=?,address=?
        WHERE id=?
        ''',(first_name,last_name,phone_number,email,address,user_id))
        con.commit()
        return "User updated successfully."
    else:
        return message
def delete_user(user_id):
    cursor.execute("DELETE FROM userrs WHERE id=?",(user_id))
    con.commit();
    return "User Deleted SuccessFully"
def menu():
    while True:
        print("\nUser Management Application")
        print("1.Add User")
        print("2.View User")
        print("3.Update User")
        print("4.Delete User")
        print("5.Exit")
        choice=input("Enter Your Choice:")
        if choice=='1' :
            first_name=input("Enter First Name:")
            last_name=input("Enter Last Name")
            phone_number=input("Enter the Phone Number")
            email=input("Enter email")
            address=input("Enter address")
            print(add_user(first_name,last_name,phone_number,email,address))
        elif choice=='2':
            users=view_users()
            for user in users:
                print(user)
        elif choice=='3':
            user_id=int(input("Enter User Id to update"))
            first_name=input("Enter new First name")
            lsst_name=input("Enter new last name")
            phone_number=input("Enter new phone number")
            email=input("enter new email")
            address=input("Enter new address")
        elif choice=='4':
            user_id=input("Enter the user id to be deleted")
            print(delete_user(user_id))
        elif choice=='5':
            break;
        else:
            print("invalid choice !Please try again")
menu()
con.close()


