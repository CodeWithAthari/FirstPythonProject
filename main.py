import datetime
import os
import sys


# set = {"Athar","Rizwan","Athar"}


def table():
    print("-------------- Code With Athar Developed This Table Maker Tool")
    table = int(input("Enter Table: "))
    max = int(input("Enter Max Table Number: "))
    i = 0
    while i < max:
        i += 1
        tub = table * i
        print(str(table) + " x " + str(i) + " =" + str(tub))




def age():
    print("------------------ This tool is developed by Code With Athar ------------------")
    enter = input("Press Enter to Continue")
    if enter == "":
        x = datetime.datetime.now()
        x = int(x.strftime('%Y%m%d'))
        year = str(x)
        year = year[0:4]
        month = str(x)
        month = month[4:6]
        date = str(x)
        date = date[6:]

        final = year + month + date
        final = int(final)

        userage = input("Enter Your Age e.g 2005/10/29 :")
        userage = userage.replace("/", "")
        userage = int(userage)
        result = final - userage
        result = str(result)
        print("You are " + result[0:2] + " years old.")

    else:
        print("You Pressed Wrong Key")
        enter = input("Press Enter to Re Run the Program")
        os.execl(sys.executable, sys.executable, *sys.argv)


print("---------CODE WITH ATHAR SPECIAL TOOLS")
print("Select Tools: \n 1. Age Calculator \n 2. Table Generator")
type = int(input("Enter Tool: "))
if type == 1:
    age()
elif type == 2:
    table()
else:
    print("You Entered the Wrong Value")



