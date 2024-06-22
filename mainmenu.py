import mainmenu
import airport
import passanger
import flight
import employee
import ticket
import graphicalreport
import os
os.system('cls')
while True:   
    print("........................................................................................")
    print(".................****** WELCOME TO AIRLINES MANAGEMENT SYSTEM ******....................")    
    print("........................................................................................")
    
    print("1: AIRPORT DETAILS")
    print("2: FLIGHT INFO")
    print("3: PASSENGER INFO")
    print("4: TICKET")
    print("5: EMPLOYEE DETAILS")
    print("6: GRAPHICAL REPORT")
    print("7: EXIT")   print("........................................................................................")
    choice=int(input("ENTER THR REQUIRED CHOICE: "))
    if choice==1:
        airport.ARP_MENU()
    elif choice==2:
        flight.FLG_MENU()
    elif choice==3:
        passanger.PASS_MENU()
    elif choice==4:
        ticket.TICT_MENU()
    elif choice==5:
        employee.EMP_MENU()
    elif choice==6:
        graphicalreport.GRAPH_MENU()
    elif choice==7:
        quit()
    else:
        print("ERROR:This choice is not available, enter the required choice")
        conti=input("Press any other key")
