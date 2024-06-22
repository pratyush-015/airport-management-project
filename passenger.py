import mysql.connector as sqltor
import mainmenu
import passanger
import airport
def PASS_MENU():
    while True:        
        print("..................................................................")
        print("............WELCOME TO AIRLINES MANAGEMENT SYSTEM.................")        
        print("..................................................................")
        print("................. ******PASSENGER INFO****** .....................")        
        print("..................................................................")

        print("1: ADD PASSENGER DETAILS")
        print("2: SHOW PASSENGER DETAILS")
        print("3: SEARCH")
        print("4: DELETION")
        print("5: UPDATE PASSENGER DETAILS")
        print("6: RETURN TO MAIN MENU")
        choice=int(input("ENTER THE REQUIRED CHOICE: "))
        if choice==1:
            passanger.INSERT_PASS_DETAILS()        
        elif choice==2:
            passanger.SHOW_PASS_DETAILS()        
        elif choice==3:            
            passanger.SEARCH_PASS_DETAILS()        
        elif choice==4:            
            passanger.DELETE_PASS_DETAILS()        
        elif choice==5:            
            passanger.EDIT_PASS_DETAILS()
        elif choice==6:
            return
        else:
            print("ERROR:This choice is not available, enter the required choice")
            conti=input("Press any other key")
def INSERT_PASS_DETAILS():    mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    PASSENGER_ID= int(input("Enter passenger ID: "))
    PASSPORT_NO=input("Enter passport No: ")
    PASSENGER_NAME=input("Enter passenger name: ")
    GENDER=input("Enter gender: ")
    FLIGHT_CODE=(input("Enter flight code: "))
    AGE=int(input("Enter age: "))
    PHONE_NUMBER=int( input("Enter phone number: "))
    EMAIL_ID= input(" Enter email ID: ")
    input1=(PASSENGER_ID, PASSPORT_NO, PASSENGER_NAME, GENDER, FLIGHT_CODE,AGE,PHONE_NUMBER,EMAIL_ID)
    qry= 'insert into passenger values(%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(qry,input1)
    mycon.commit()
    mycon.close()
    cursor.close()
    print('Record is saved in passenger table')

def SHOW_PASS_DETAILS():    mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    cursor.execute('select* from passenger')
    data=cursor.fetchall()
    for row in data:
        print(row)

def SEARCH_PASS_DETAILS():
mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    ac=int(input("Enter passenger ID: "))
    st="select * from passenger where PASSENGER_ID='%s'"%(ac)
    cursor.execute(st)
    data=cursor.fetchall()
    print(data)

def DELETE_PASS_DETAILS():   mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
   cursor=mycon.cursor()
   ac=int(input("Enter passenger ID: "))
   st="delete from passenger where PASSENGER_ID='%s'"%(ac)
   cursor.execute(st)
   mycon.commit()
   print("Data deleted successfully")
   
def EDIT_PASS_DETAILS():
   mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush',port='3306',database='airline')
   cursor=mycon.cursor()
   print("1: Edit PASSENGER ID")
   print("2: Edit PASSPORT NO")
   print("3: Edit PASSENGER NAME")
   print("4: Edit GENDER")
   print("5: Edit FLIGHT CODE")
   print("6: Edit AGE")
   print("7: Edit PHONE NUMBER")
   print("8: Edit EMAIL ID")
   print("9: Return")   print("................................................................")
   choice=int(input("Enter required choice: "))
   if choice==1:
       passanger.edit_PASSENGER_ID()
   elif choice==2:
       passanger.edit_PASSPORT_NO()
   elif choice==3:
        passanger.edit_PASSENGER_NAME()
   elif choice==4:
        passanger.edit_GENDER()
   elif  choice==5:
        passanger.edit_FLIGHT_CODE()
   elif  choice==6:
        passanger.edit_AGE()
   elif choice==7:
       passanger.edit_PHONE_NUMBER()
   elif choice==8:
       passanger.edit_EMAIL_ID()
   elif choice==9:
       return
   else:
     print('ERROR: INVALID CHOICE TRY AGAIN')
     conti='Press any key to return to main menu'
def edit_PASSENGER_ID(): 
mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter PASSENGER ID: '))
    nm=input('Enter correct PASSENGER ID: ')
    st="update PASSENGER set PASSENGER_ID='%s' where PASSENGER_ID='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated successfully'       
def edit_PASSPORT_NO(): 
    mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter PASSANGER ID: '))
    nm=input('Enter PASSPORT NO: ')
    st="update PASSENGER set PASSPORT_NO='%s' where PASSENGER_ID='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated successfully')
      def edit_PASSENGER_NAME(): 
    mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter PASSENGER ID: '))
    nm=input('Enter correct PASSENGER NAME: ')
    st="update PASSENGER set PASSENGER_NAME='%s' where PASSENGER_ID='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated successfully')
def edit_GENDER(): 
    mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter PASSENGER ID: '))
    nm=input('Enter correct GENDER: ')
    st="update PASSENGER set GENDER='%s' where PASSENGER_ID='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated successfully')    
def edit_FLIGHT_CODE(): 
    mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter PASSENGER ID: '))
    nm=input('Enter correct Flight code: ')
    st="update PASSENGER set FLIGHT_CODE='%s' where PASSENGER_ID='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print('Data Updated successfully')
def edit_AGE(): 
    mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter PASSENGER ID: '))
    nm=input('Enter correct AGE: ')
    st="update PASSENGER set AGE='%s' where PASSENGER_ID='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated successfully')
def edit_PHONE_NUMBER():
    mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter PASSENGER_ID: '))
    nm=input('Enter correct PHONE NUMBER: ')
    st="update PASSENGER set PHONE_NUMBER='%s' where PASSENGER_ID='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated successfully')
def edit_EMAIL_ID(): 
    mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter PASSENGER ID: '))
    nm=input('Enter correct destination: ')
    st="update PASSENGER set EMAIL_ID='%s' where PASSENGER_ID='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated successfully')
