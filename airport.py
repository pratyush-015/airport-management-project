import mysql.connector as sqltor
import mainmenu
import airport
import os
def ARP_MENU():

    while True:
        print("..................................................................")
        print("............WELCOME TO AIRLINES MANAGEMENT SYSTEM.................")        
        print("..................................................................")
        print(".................******* AIRPORT INFO ********....................")
        print("..................................................................")
        
        print("1: ADD AIRPORT DETAILS")
        print("2: SHOW AIRPORT DETAILS")
        print("3: SEARCH FOR AIRPORT")
        print("4: DELETION OF RECORDS")
        print("5: UPDATE AIRPORT DETAILS")
        print("6: RETURN TO MAIN MENU")
        choice=int(input("ENTER THE REQUIRED CHOICE: "))
        if choice==1:
            airport.INSERT_ARP_DETAILS()
        elif choice==2:
            airport.SHOW_ARP_DETAILS()
        elif choice==3:
            airport.SEARCH_ARP_DETAILS()
        elif choice==4:
            airport.DELETE_ARP_DETAILS()
        elif choice==5:
            airport.EDIT_ARP_DETAILS()
        elif choice==6:
            return
        else:
            print("ERROR: This choice is not available, please enter the required choice")
            conti=input("Press any other key")
def INSERT_ARP_DETAILS():  

    mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database ='airline')
    conti= 'press any key to return to main menu'
    cursor=mycon.cursor()
    AIRPORT_ID= int(input("Enter AIRPORT_ID: "))
    AIRPORT_NAME=input("Enter AIRPORT_NAME: ")
    AIRLINE_NAME=input("Enter AIRLINE_NAME: ")
    STATE=input("Enter STATE: ")
    COUNTRY_NAME=input("Enter the COUNTRY_NAME: ")    
    THREE_DIGIT_CODE= int(input("Enter three digit code: "))
    input1=(AIRPORT_ID, AIRPORT_NAME, AIRLINE_NAME, STATE, COUNTRY_NAME,THREE_DIGIT_CODE)
    qry= 'insert into airport values(%s,%s,%s,%s,%s,%s)'
    cursor.execute(qry,input1)
    mycon.commit()
    mycon.close()
    cursor.close()
    print('Record is saved in airport table')

def SHOW_ARP_DETAILS():

    mycon=sqltor.connect(host='Localhost', user='root', passwd= 'pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    cursor.execute('select* from airport')
    data=cursor.fetchall()
    for row in data:
      print(row)

def SEARCH_ARP_DETAILS():

   mycon=sqltor.connect(host='localhost', user='root',passwd= 'pratyush', port='3306', database='airline')
   cursor=mycon.cursor()
   ac=int(input("Enter AIRPORT_ID: "))
   St= "select * from airport where airport_id=%s"%(ac)
   cursor.execute(St)
   data=cursor.fetchall()
   print(data)

def DELETE_ARP_DETAILS():

    mycon=sqltor.connect(host='localhost', user='root',passwd= 'pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input("Enter AIRPORT_ID: "))
    st="delete from airport where AIRPORT_ID=%s"%(ac)
    cursor.execute(st)
    mycon.commit()
    print("Data deleted successfully.")

def EDIT_ARP_DETAILS():

    mycon=sqltor.connect(host='localhost', user='root',passwd= 'pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    print("1: Edit AIRPORT_ID")
    print("2: Edit AIRPORT_NAME")
    print("3: Edit STATE")
    print("4: Edit COUNTRY_NAME")
    print("5: Return")
    print("................................................................")

    choice=int(input("Enter your choice: "))

    if choice==1:
       airport.edit_AIRPORT_ID()
    elif choice==2:
       airport.edit_AIRPORT_NAME()
    elif choice==3:
       airport.edit_STATE()
    elif choice==4:
       airport.edit_COUNTRY_NAME()    
    elif  choice==5:
        return
    else:
       print('ERROR: INVALID CHOICE TRY AGAIN')
       conti='Press any key to return to main menu'

def edit_AIRPORT_ID(): 

    mycon=sqltor.connect(host='localhost', user='root',passwd= 'pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter old AIRPORT_ID: '))
    nm=input('Enter correct AIRPORT_ID: ')
    st="update airport set  AIRPORT_ID= '%s' where AIRPORT_ID= '%s'"%(nm,ac)    
    cursor.execute(st)
    mycon.commit()
    print('Data Updated Successfully')

def edit_AIRPORT_NAME():
   mycon=sqltor.connect(host='localhost', user='root',passwd= 'pratyush', port='3306', database='airline')
   cursor=mycon.cursor()
   ac=int(input('Enter AIRPORT_ID: '))
   nm=str(input('Enter correct AIRPORT_NAME: '))
   st="update airport set AIRPORT_NAME= '%s' where AIRPORT_ID= '%s'"%(nm,ac)
   cursor.execute(st)
   mycon.commit()
   print('Data Updated Successfully')

def edit_STATE():

   mycon=sqltor.connect(host='localhost', user='root',passwd= 'pratyush', port='3306', database='airline')
   cursor=mycon.cursor()
   ac=int(input('Enter AIRPORT_ID: '))
   nm=input('Enter correct STATE: ')
   st="update airport set STATE= '%s' where AIRPORT_ID= '%s'"%(nm,ac)
   cursor.execute(st)
   mycon.commit()
   print('Data Updated Successfully')

def edit_COUNTRY_NAME():
    
    mycon=sqltor.connect(host='localhost', user='root',passwd= 'pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter AIRPORT_ID: '))
    nm=input('Enter correct COUNTRY_NAME: ')
    st="update airport set country_name= '%s' where AIRPORT_ID= '%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated Successfully')
