#Imports
import os
import sys

#menu in a main function that can be called from the command line   
def main():
    print("Orbital Beaver Hacking Framework")
    print("1. Open Redirection Scanner")
    print("2. Robots.txt Scanner")
    print("3. Exit")
    choice = input("Please enter a number: ")
    if choice == "1":
        #call the python file OpenRedirectTest.py
        os.system("python3 OpenRedirectTest.py")
    elif choice == "2":
        #call the python file RobotsTXTScan.py
        os.system("python3 RobotsTXTScan.py")
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")
        main()

main()