import mainmenu
import ticket
import mysql.connector as sqltor
def TICT_MENU():
    while True:
        print("..................................................................")
        print("............WELCOME TO AIRLINES MANAGEMENT SYSTEM.................")        
        print("..................................................................")
        print("................. ******TICKET MANAGEMENT****** ..................")     
        print("..................................................................")
        
        print("1: ADD TICKET DETAILS")
        print("2: SHOW TICKET DETAILS")
        print("3: SEARCH TICKET")
        print("4: DELETION")
        print("5: UPDATE TICKET DETAILS")
        print("6: RETURN TO MAIN MENU")     
        choice=int(input("ENTER THE REQUIRED CHOICE: "))
        if choice==1:
            ticket.TICT_DETAILS()
        elif choice==2:
            ticket.SHOW_TICT_DETAILS()
        elif choice==3:
            ticket.SEARCH_TICT_DETAILS()
        elif choice==4:
            ticket.DELETE_TICT_DETAILS()
        elif choice==5:
            ticket.EDIT_TICT_DETAILS()
        elif choice==6:
            return
        else:
            print("ERROR:This choice is not available, enter the required choice")        conti=input("Press any other key") 
def TICT_DETAILS():    mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    ticket_no=int(input('Enter Ticket No: '))
    passport_no=int(input('Enter Passport number: '))
    flight_code=input('Enter Flight code: ')
    destination=input('Enter Destination: ')
    date_of_booking=input('Enter date of booking: ')
    date_of_travel=input('Enter the date of travel: ')
    seat_no=input('Enter the seat No: ')
    cl=input('Enter class: ')
    price_in_rupees=int(input('Enter price in rupees: '))
input1=(ticket_no,passport_no,flight_code,destination,date_of_booking,date_of_travel,seat_no,cl,price_in_rupees)
    qry='insert ticket values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(qry,input1)
    mycon.commit()
    mycon.close()
    cursor.close()
    print('Record has been Saved in ticket table')
def SHOW_TICT_DETAILS():
mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    cursor.execute('select * from TICKET')
    data=cursor.fetchall()
    for row in data:
        print(row)
def SEARCH_TICT_DETAILS():
mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter Ticket_no: '))
    st="select * from TICKET where ticket_no='%s'"%(ac)
    cursor.execute(st)
    data=cursor.fetchall()
    print(data)
def DELETE_TICT_DETAILS():
mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter Ticket_no: '))
    st="delete from ticket where ticket_no='%s'"%(ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Deleted Successfully')
def EDIT_TICT_DETAILS():
mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    print('1:Edit DESTINATION')
    print('2:Edit SEAT NO')
    print('3:Edit CLASS')
    print('4:Edit PRICE')
    print('5: Return')
    print('----------------------------------------------')
    choice=int(input('ENTER REQUIRED CHOICE: '))
    if choice==1:
        ticket.edit_destination()
    elif choice==2:
        ticket.edit_seat_no()
    elif choice==3:
        ticket.edit_class()
    elif choice==4:
        ticket.edit_price_in_rupees()
    elif choice==5:
        return
    else:
        print('ERROR:INVALID CHOICE TRY AGAIN')
        conti='Press any key to return to main menu’       
def edit_destination():
    mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter Ticket No: '))
    nm=input('Enter correct Destination: ')
    st="update ticket set destination='%s' where ticket_no='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated Successfully')
def edit_seat_no(): mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter Ticket No: '))
    nm=int(input('Enter correct Seat No: '))
    st="update ticket set seat_no='%s' where ticket_no='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated Successfully')
def edit_cl():
mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter Ticket No: '))
    nm=input('Enter correct Class: ')
    st="update ticket set cl='%s' where ticket_no='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated Successfully')
    
def edit_price_in_rupees():
    mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter Ticket No: '))
    nm=input('Enter corrected Price: ')
    st="update ticket set price_in_rupees='%s' where ticket_no='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated Successfully')
