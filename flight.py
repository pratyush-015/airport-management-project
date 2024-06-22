import mainmenu
import flight
import mysql.connector as sqltor
def FLG_MENU():
    while True:        
        print("..................................................................")
        print("............WELCOME TO AIRLINES MANAGEMENT SYSTEM.................")
        print("..................................................................")
        print("................. ******FLIGHT MANAGEMENT****** ..................")
        print("..................................................................")

        print('1:Add Flight  Details')
        print('2:Show Flight  Details')
        print('3:Search Flight Details')
        print('4:Delete Flight Details ')
        print('5:Edit FLight Info Details')
        print('6:Return')
        print('---------------------------------------------------')

        choice=int(input('Enter the required choice: '))
        
        if choice==1:
            flight.insert_flight_details()
        elif choice==2:
            flight.show_flight_details()
        elif choice==3:
            flight.search_flight_details()
        elif choice==4:
            flight.delete_flight_details()
        elif choice==5:
            flight.edit_flight_details()
        elif choice==6:
            return
        else:
            print('ERROR:INVALID CHOICE TRY AGAIN')
            conti='Press any key to return to main menu'
def insert_flight_details():    mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    Flight_id=int(input('Enter Flight ID: '))
    Flight_code=input('Enter Flight code: ')
    Destination=input('Enter desired destination: ')
    Arrival=input('Enter arrival time: ')
    Departure =input('Enter departure time: ')
    Status=input('Enter status time: ') 
    Duration=input('Enter duration time: ') 
    Flight_type=input('Enter Flight type: ')
input1=(Flight_id,Flight_code,Destination,Arrival,Departure ,Status, Duration, Flight_type)
    qry='insert into flight values(%s,%s,%s,%s,%s,%s, %s, %s)'
    cursor.execute(qry,input1)
    mycon.commit()
    mycon.close()
    cursor.close()
    print('Record has been Saved in flight table.')
def show_flight_details():    mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    cursor.execute('select * from flight')
    data=cursor.fetchall()
    for row in data:
        print(row)
def search_flight_details():    mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter Flight ID: '))
    st="select * from flight where flight_id='%s'"%(ac)
    cursor.execute(st)
    data=cursor.fetchall()
    print(data)
def delete_flight_details():    mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter Flight ID: '))
    st="delete from flight where Flight_id='%s'"%(ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Deleted Successfully')
def edit_flight_details():
mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    print('1:Edit destination')
    print('2:Edit arrival time')
    print('3:Edit departure time')
    print('4:Return')
    print('----------------------------------------------')
    choice=int(input('Enter your Choice: '))
    if choice==1:
        flight.edit_destination()
    elif choice==2:
        flight.edit_arrival_time()
    elif choice==3:
        flight.edit_departure_time()
    elif choice==4:
        return
    else:
        print('ERROR:INVALID CHOICE TRY AGAIN')
        conti='Press any key to return to main menu'
    def edit_destination():
    mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter Flight ID: '))
    nm=input('Enter correct destination: ')
    st="update flight set destination= '%s' where flight_id= '%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated Successfully')
def edit_arrival_time():
mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter Flight ID: '))
    nm=int(input('Enter correct arrival time: '))
    st="update flight set arrival_time= '%s' where flight_id= '%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated Successfully')
def edit_departure_time():
mycon=sqltor.connect(host='localhost',user='root',passwd='pratyush',port='3306',database='airline')
    cursor=mycon.cursor()
    ac=int(input('Enter Flight_ID: '))
    nm=input('Enter correct departure time: ')
    st="update flight_set departure_time ='%s' where flight_id='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data Updated Successfully')
