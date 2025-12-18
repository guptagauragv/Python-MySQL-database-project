def alter():
            print("Press 1 to Add a new column in an existing table ")
            print("Press 2 to Delete a item of a table")
            print("Press 3 to change data type of a column")
            s=int(input("Enter your choice:-"))
            if s==1:
                tble=input("Enter Table name:")
                field=input("Enter column Name:")
                typ=input("Enter datatype:")
                bye=input("Enter space of letters to inserted(in no.):")
                print("Press 0 for none")
                print("Press 1 to apply (primary key) ")
                print("Press 2 to apply (Not null) ")
                print("Press 3 to apply (default) ")
                print("Press 4 to apply (unique)")
                con=int(input("Choose constraints to be applied in column:"))
                if con==0:
                    const=''
                if con==1:
                    const="primary key"
                if con==2:
                    const="Not null"
                if con==3:
                    cs=input("Enter Defaultvalue:")
                    const="default" "'"+cs+"'"
                if con==4:
                    const="Unique"
                chain=const
                q=field+' '+typ+'('+bye+') '+chain
                query='alter table '+tble+' '+'add'+' '+q
                cursor.execute(query)
            if s==2:
                print("Press 1 to Delete column-")
                print("Press 2 to remove a constraint from  table-")
                at=int(input("Enter your choice:-"))
                if at==1:
                    tble=input("Enter Table name:")
                    field=input("Enter column Name you want to delete:")
                    query='alter table '+tble+' '+'drop'+' '+field
                    cursor.execute(query)
                if at==2:
                    print("Press 1 to remove (primary key) ")
                    print("Press 2 to remove (Not null) ")
                    print("Press 3 to remove (default) ")
                    print("Press 4 to remove (unique)")
                    con=int(input("Choose constraints to be remove from column:"))                    
                    if con==1:
                        const='alter table '+tble+' '+'drop'+' '+"primary key"
                        cursor.execute(const)
                    if con==2:
                        const='alter table '+tble+' '+'drop'+' '+"not null"
                        cursor.execute(const)
                    if con==3:
                        const='alter table '+tble+' '+'drop'+' '+"default"
                        cursor.execute(const)
                    if con==4:
                        const='alter table '+tble+' '+'drop'+' '+"unique"
                        cursor.execute(const)

def present():    
      tble=input("Enter Table name to be presented:")
      print("press 0 to present all data in table")
      print("press 1 to filter the table ")
      print("press 2 to Alter the table ")
      print("press 3 to update the table ")
      print("press 4 to feed data to table")
      print("press 5 to describe the table ")
      fd=int(input("enter your choice:"))
      if fd==0:
          cursor.execute("select * from "+tble)
          x=cursor.fetchall()
          for i in x:
              print(i)
      if fd==5:
          cursor.execute("desc "+tble)
          x=cursor.fetchall()  
          for i in x:
              print(i)
      if fd==1:
          fi=input("Enter fields separated with commas(,): ")
          zd=fi.strip()
          query="select "+zd+" from "+tble
          cursor.execute(query)
          x=cursor.fetchall()  
          for i in x:
              print(i)          
      if fd==2:
          alter()
    
def table():
    print("Press 1 to show all tables ")
    print("Press 2 to create table")
    n=int(input("Enter your choice:-"))
    if n==1:
        cursor.execute("show tables")
        rcord=cursor.fetchall()
        for i in rcord:
            print(i)
        print(" Press 1 to delete Table")
        print(" Press 2 to present table")
        z=int(input("Enter your choice:-"))
        if z==1:
            tble=input("Enter Table name you want to delete:")
            cursor.execute("drop table "+tble)
        if z==2:
            present()        
    if n==2:
        t=input(" Name the table to be created:")
        x=int(input("No. of fields in table:"))
        l=list()
        q=''
        for i in range(1,x+1):
            field=input("Enter column Name:")
            typ=input("Enter datatype:")
            bye=input("Enter space of letters to inserted(in no.):")
            print("Press 0 for none")
            print("Press 1 to apply (primary key) ")
            print("Press 2 to apply (Not null) ")
            print("Press 3 to apply (default) ")
            print("Press  4 to apply (unique)")
            con=int(input("Choose constraints to be applied in column:"))
            if con==0:
                const=''
            if con==1:
                const="primary key"
            if con==2:
                const="Not null"
            if con==3:
                cs=input("Enter Defaultvalue:")
                const="default" "'"+cs+"'"
            if con==4:
                const="Unique"
            chain=const
            q=q+field+' '+typ+'('+bye+') '+chain
            if i!=x:
                q=q+','
        state="create table "+t+'('+q+')'
        cursor.execute(state)
            
def database():
    print("Press (X) to Close the program ")
    print("Press 1 to show database")
    print("Press 2 to use database")
    print("Press 3 to create database")
    print("Press 4 to delete database")
    n=input("Enter your choice:-")
    if n=='1':
        cursor.execute("show databases")
        rcord=cursor.fetchall()
        for i in rcord:
            print(i)
    if n=='2':
        name=input("Enter name of database you want to use:-")
        cursor.execute("use "+name)
        while True:
            
            table()
            print("Press X to close the program")
            print("Press C to Stay on table")
            print("Press D to Go to Databases")
            n=input("Enter your choice:")
            if n=="c":
                            continue
            elif n=="d":
                      
                      break       
            elif n=="x":
                return 0
                break
               
    if n=='3':
        name=input("Enter name of database you want to create:-")
        cursor.execute("create database "+name)
        print("databases created")    
    if n=='4':
        name=input("Enter name of database you want to delete-")
        cursor.execute("drop database "+name)
        print("databases deleted")
        
    if n=='x':
        return 0
    

import mysql.connector as mysql
#local=input("Enter Host Name:-")
#root=input("Enter User Name:-")
#pwd=input("Enter password:-")
mydb=mysql.connect(host="localhost",user="root",passwd="expert")
cursor=mydb.cursor()
if mydb.is_connected:
    print("connection succesfull")
    

while True :
        x=database()
        if x==0:
            break
mydb.commit()
print("The end")







        
