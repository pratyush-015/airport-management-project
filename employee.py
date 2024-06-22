import mysql.connector as sqltor
import mainmenu
import employee
def EMP_MENU():

    while True:      
        print("..................................................................")
        print("............WELCOME TO AIRLINES MANAGEMENT SYSTEM.................")     
        print("..................................................................")
        print("................. ******EMPLOYEE DETAILS****** ...................")  
        print("..................................................................")

        print("1: ADD EMPLOYEE_DETAILS")
        print("2: SHOW EMPLOYEE DETAILS")
        print("3: SEARCH EMPLOYEE")
        print("4: DELETE DETAILS")
        print("5: UPDATE DETAILS")
        print("6: RETURN")

        choice=int(input("ENTER THE REQUIRED CHOICE: "))
        
        if choice==1:
          employee.EMP_DETAILS()
        elif choice==2:
          employee.SHOW_EMP_DETAILS()
        elif choice==3:
          employee.SEARCH_EMP_DETAILS()
        elif choice==4:
          employee.DELETE_EMP_DETAILS()
        elif choice==5:
          employee.EDIT_EMP_DETAILS()
        elif choice==6:
          return        
        else:
          print("ERROR:This choice is not available, enter the required choice")
          conti=input("Press any other key")

def EMP_DETAILS():

  mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database ='airline')
  conti= 'press any key to return to main menu'
  cursor=mycon.cursor()
  EMPLOYEE_ID= int(input("Enter Airport ID: "))
  EMPLOYEE_NAME=input("Enter Employee Name: ")
  ADDRESS=input("Enter Address: ")
  GENDER= input("Enter GENDER")
  AGE=int(input("Enter age: "))
  PHONE_NUMBER=int(input("Enter phone number: "))
  OB_TYPE=input("Enter job type: ")
  SHIFT=input ("Enter shift: ")
  SALARY=int(input("Enter salary: "))
  input1=(EMPLOYEE_ID,EMPLOYEE_NAME,ADDRESS,GENDER,AGE,PHONE_NUMBER,JOB_TYPE,SHIFT,SALARY)
  qry= 'insert into airport values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
  cursor.execute(qry,input1)
  mycon.commit()
  mycon.close()
  cursor.close()
  print('Record is saved in employee table')

def SHOW_EMP_DETAILS():

  mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
  cursor=mycon.cursor()
  cursor.execute('select* from EMPLOYEE')
  data=cursor.fetchall()
  for row in data:
    print(row)

def SEARCH_EMP_DETAILS():

  mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
  cursor=mycon.cursor()
  ac=int(input("Enter EMPLOYEE ID: "))
  st= "select * from EMPLOYEE where EMPLOYEE_ID='%s'"%(ac)
  cursor.execute(st)
  data=cursor.fetchall()
  print(data)

def DELETE_EMP_DETAILS():
   mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
   cursor=mycon.cursor()
   ac=int(input("Enter EMPLOYEE ID: "))
   st="delete from EMPLOYEE_ID where EMPLOYEE_ID='%s'"%(ac)
   cursor.execute(st)
   mycon.commit()
   print("Data deleted successfully")
def EDIT_EMP_DETAILS():
   mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
   cursor=mycon.cursor()
   print("1: Edit EMPLOYEE_ID")
   print("2: Edit EMPLOYEE_NAME")
   print("3: Edit ADDRRSS")
   print("4: Edit GENDER")
   print("5: Edit AGE")
   print("6: Edit PHONE_NUMBER")
   print("7: Edit JOBTYPE")
   print("8: Edit SHIFT ")
   print("9: Edit SALARY")
   print("10: Return")  
   print("................................................................")
   choice=int(input("ENTER THE REQUIRED CHOICE: "))
   if choice==1:
      employee.edit_EMPLOYEE_ID()
   elif choice==2:
      employee.edit_edit_EMPLOYEE_NAME()
   elif choice==3:
      employee.edit_ADDRESS()
   elif choice==4:
      employee.edit_GENDER()
   elif  choice==5:
      employee.edit_AGE()
   elif  choice==6:
      employee.edit.PHONE_NUMBER()
   elif choice==7:
      employee.edit.JOB_TYPR()
   elif choice==8:
      employee.edit.SHIFT()
   elif choice==9:
      employee.edit.SALARY
   elif choice==10:
      return
   else:
      print('ERROR: INVALID CHOICE TRY AGAIN')
      conti='Press any key to return to main menu'

   def edit_EMPLOYEE_ID(): 

    mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter EMPLOYEE ID: '))
    nm=input('Enter correct EMPLOYEE ID: ')
    st="update EMPLOYEE set EMPLOYEE_ID='%s' where EMPLOYEE_ID='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated Successfully')

def edit_EMPLOYEE_NAME():
  
    mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter EMPLOYEE ID: '))
    nm=input('Enter correct EMPLOYEE NAME: ')
    st="update EMPLOYEE set EMPLOYEE_NAME='%s' where EMPLOYEE_ID='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated successfully')
def edit_GENDER(): 
    mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter EMPLOYEE ID: '))
    nm=input('Enter correct GENDER: ')
    st="update EMPLOYEE set GENDER='%s' where EMPLOYEE_ID='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated successfully')
def edit_JOB_TYPE(): 
    mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter EMPLOYEE ID: '))
    nm=input('Enter correct JOB TYPE: ')
    st="update EMPLOYEE set JOB_TYPE='%s' where EMPLOYEE_ID='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print('Data Updated successfully')
def edit_AGE(): 
    mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter EMPLOYEE ID: '))
    nm=input('Enter correct AGE: ')
    st="update EMPLOYEE set AGE='%s' where EMPLOYEE_ID='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated successfully')    
def edit_PHONE_NUMBER():
    mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter EMPLOYEE ID: '))
    nm=input('Enter correct PHONE NUMBER: ')
    st="update EMPLOYEE set PHONE_NUMBER='%s' where EMPLOYEE_ID='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated successfully')    
def edit_SALARY(): 
    mycon=sqltor.connect(host='localhost', user='root',passwd='pratyush', port='3306', database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter EMPLOYEE_ID: '))
    nm=int(input('Enter correct SALARY: '))
    st="update EMPLOYEE set SALARY='%s' where SALARY='%s'" %(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated successfully')
