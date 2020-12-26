# first setup MYSQL server and form proper structure either using python or directly using sql query


import mysql.connector

# connecting to database
conn = mysql.connector.connect(host='localhost', database='database_name', user='user_name', password='user_password')
if conn.is_connected():
    print("[+] Connected to db")
else:
    print("[-] OOPS! no connection")

# to use sql query we use cursor
cursor = conn.cursor()


# reading database - READ
print("\n[~] So what we have?")
cursor.execute('select * from emp')  # passing sql query
# # fetch one record data from table
# row=cursor.fetchone()
# while row is not None:
#     print(row)
#     row=cursor.fetchone()

# fetch all record data from table
row = cursor.fetchall()
print("[+] Total number of records: ", cursor.rowcount)
for row in row:
    print(row)


# create/execute sql query - CREATE/EXECUTE
print("\n[~] Adding new employee")
try:
    cursor.execute("insert into emp values(121,'Johana',3000)")
    conn.commit()  # we have to commit the sql queries else no data saved # COMMIT HAPPEN ON CONNECTION
    print("[+] Employee added")
except:
    conn.rollback()  # if try block doesn't execute rollback to previous state
    print("[-] Sorry!")


# delete a record - DELETE
print("\n[~] Deleting an employee!") # this time we do it using a function
def delete(id):
    # connecting to database
    conn = mysql.connector.connect(host='localhost', database='database_name', user='user_name', password='user_password') # when using function better have connection seperately else usless connection time
    if conn.is_connected():
        print("[+] Connected to db")
        cursor=conn.cursor()
        str= "delete from emp where id='%d'"
        Id=(id)
        try:
            cursor.execute(str % Id) # will replace the %d with Id
            conn.commit()
            print("[+] Record deleted")
        except:
            conn.rollback()
            print("[-] Unable to delete")
        finally:
            cursor.close() # close the connection finally no matter the output
            conn.close()
    else:
        print("[-] OOPS! no connection")

empId=int(input("[~] Enter emp ID: ")) # invoking the function
delete(empId)


# update a record - UPDATE
print("\n[~] Updating an employee!") # this time we do it using a function
def update(id):
    # connecting to database
    conn = mysql.connector.connect(host='localhost', database='database_name', user='user_name', password='user_password') # when using function better have connection seperately else usless connection time
    if conn.is_connected():
        print("[+] Connected to db")
        cursor=conn.cursor()
        str= "update emp set sal=10000 where id='%d'"
        Id=(id)
        try:
            cursor.execute(str % Id) # will replace the %d with Id
            conn.commit()
            print("[+] Record updated")
        except:
            conn.rollback()
            print("[-] Unable to update")
        finally:
            cursor.close() # close the connection finally no matter the output
            conn.close()
    else:
        print("[-] OOPS! no connection")

emplId=int(input("[~] Enter emp ID: ")) # invoking the function
update(emplId)


cursor.close()
conn.close()
