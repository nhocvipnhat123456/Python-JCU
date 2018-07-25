"""
This program will help the customer to compute the price of a movie ticket.
Name: Nguyen Hoang Nhan
Date started: 17/11/2014
Date last modified: 1/12/2014
Pseudocode:

import random
function MainMenu
    display Menu
function Instruction
    display description
function Quit
    display thankyou
function main
    while True
        display MainMenu
        get choice
        if choice=i or choice=I
            display Instruction
        elif choice=a or choice=A
            while True
                get movie name
                get price of the movie
                if movie name==" "
                    display error
                else
                    break
        elif choice=l or choice=L
            get file name
        elif choice=c or choice=C
            open movie file
            read file
            while True
                get value
                display error
                if value>0
                    break
            close file
            while True
                get number of adults and children
                if number<0
                    display error
                else
                    break
            random number from 1 to 9
            if random number=1
                display congratulation
            while True
                get value offpeak or peak
                if value!= o or value!=p
                    display error
                else
                    break
            calculate the price
        elif choice=s or choice=S
            get file name
        elif choice=q or choice=Q
            display Quit
            break
        else
            display error
"""
            

import random

def MainMenu():
    print("Menu:")
    print("(I)nstructions")
    print("(L)oad Movies")
    print("(S)ave Movies")
    print("(A)dd Movie")
    print("(C)ompute Prices")
    print("(Q)uit")
def Instructions():
    print("This program allows you to calculate total costs based on choice of movie, number of adults and children and whether off-peak or peak viewing.")
    print("You can load movies from a file, add new ones and save the file for next time.")      
def Quit():
    print("Thank you for buying with CP1200, enjoy your movie")
def main():
    NoProduct= []
    while True:
        MainMenu()
        x=input("Your selection is: ")
        if x=="i" or x=="I":
            Instructions()
        elif x=="L" or x=="l":
            Load_File=input("Enter file name: ")
            NoProduct.append(Load_File)
        elif x=="A" or x=="a":
            while True:
                s=input("Enter movie name: ")
                float(input("Enter movie price: $"))
                if s==" ":
                    print("Product name cannot be blank")
                else:
                    break
        elif x=="C" or x=="c" :
            if NoProduct:
                Movie_File=open('movie.txt','r')
                read=Movie_File.read()
                print(read)
                while True:
                    num=int(input("Which movie would you like?"))
                    if num >= 5 or num <= 0:
                        print("Number must be <=4")
                    else:
                        Movie_File.close()
                        break                
                while True:
                    y=int(input("Please enter the number of adults: "))
                    z=int(input("Please enter the number of children: "))
                    if y<0 or z<0:
                        print("Error, please enter number >=0")
                    else:
                        break
                discountChance=random.randint(1, 9)#inclusive so 1 to 9 is ten
                discountFactor=1;
                if discountChance==1 :
                    discountFactor=0.5                   
                    print("You are entitled to 50% discount for adults")
                cost1=float(7.50*y*discountFactor+(7.50*z)/2)
                cost1peak=float(10.00*y*discountFactor+(10.00*z)/2)
                cost2=float(9.00*y*discountFactor+(9.00*z)/2)
                cost2peak=float(12.00*y*discountFactor+(12.00*z)/2)
                cost3=float(11.25*y*discountFactor+(11.25*z)/2)
                cost3peak=float(15.00*y*discountFactor+(15.00*z)/2)
                cost4=float(4.50*y*discountFactor+(4.50*z)/2)
                cost4peak=float(6.00*y*discountFactor+(6.00*z)/2)
                while True:
                    v=input("Would you like (O)ff Peak or (P)eak?: ")
                    if v=="o" or v=="O" and num==1:
                        print("The total costs is", "$" + format(cost1, '.2f'), "for the movie for", y ,"adults and", z ,"children. Enjoy your movie!")
                        break
                    elif v=="o" or v=="O" and num==2:
                        print("The total costs is", "$" + format(cost2, '.2f'), "for the movie for", y ,"adults and", z ,"children. Enjoy your movie!")
                        break
                    elif v=="o" or v=="O" and num==3:
                        print("The total costs is", "$" + format(cost3, '.2f'), "for the movie for", y ,"adults and", z ,"children. Enjoy your movie!")
                        break
                    elif v=="o" or v=="O" and num==4:
                        print("The total costs is", "$" + format(cost4, '.2f'), "for the movie for", y ,"adults and", z ,"children. Enjoy your movie!")
                        break
                    elif v=="p" or v=="P" and num==1:
                        print("The total costs is", "$" + format(cost1peak, '.2f'), "for the movie for", y ,"adults and", z ,"children. Enjoy your movie!")
                        break
                    elif v=="p" or v=="P" and num==2:
                        print("The total costs is", "$" + format(cost2peak, '.2f'), "for the movie for", y ,"adults and", z ,"children. Enjoy your movie!")
                        break
                    elif v=="p" or v=="P" and num==3:
                        print("The total costs is", "$" + format(cost3peak, '.2f'), "for the movie for", y ,"adults and", z ,"children. Enjoy your movie!")
                        break
                    elif v=="p" or v=="P" and num==4:
                        print("The total costs is", "$" + format(cost4peak, '.2f'), "for the movie for", y ,"adults and", z ,"children. Enjoy your movie!")
                        break
                    else:
                        print("Error. Please enter o or p")  
            else:
                print("No products.")
        elif x=="S" or x=="s":
            while True:
                savefile=input("Enter file name: ")
                if savefile =="" or savefile==" ":
                    print("File name can not be blank.")
                else:
                    break
            Save_File=open(savefile,'w')
            Save_File.close()
        elif x=="Q" or x=="q":
            Quit()
            break
        else:
            print("Invalid menu choice.")
main()
