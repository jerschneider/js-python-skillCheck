import random
print(" ")
print("#####################################################")
print("Welcome to a management program for Tom Nook's Stores")
print("        2020 {jerschne} for Nook Industries")
print("#####################################################")
print(" ")
name = input(" Hello! Please enter your name. >>> ")
print(" ")
print("Now select one of the following options:")
print("[A]: Income Tax Calculator")
print("[B]: Create an Employee Account")
print("[C]: Exit this progream")
print(" ")
start = input("Please input in A, B or C >>> ")
while True:
    if start == 'A':
        print("#####################")
        print("Income Tax Calculator")
        print("#####################")
        print(" ")
        print("Welcome!")
        print(" ")
        income = input("Please enter your predicted income for the year >>> ")
        while True:
            if income is int or float:
                taxPredicted = float(income) * .04
                print("[", name, "]", "You should expect to pay this much in taxes >>> $", taxPredicted)
                print(" ")
                exit = input("To exit this program please press the C key >>> ")
                if exit == 'C':
                    print("Exiting Program!")
                    break
            else:
                print("Please enter a number!")
                income

    if start == 'B':
        print("################################################")
        print("Employee Account Creation (ie Usernmae/Password)")
        print("################################################")
        print(" ")
        print("Welcome!")
        print(" ")
        print("To begin: please input the first and last name of the employee.")
        print(" ")
        first = input("first name >>> ")
        last = input("last name >>> ")
        username = first[0] + first[1] + first [2] + last[0] + last[1] + last[2] + last[3]
        print("the username for ", first, last, " is >>> ", username)
        passBank = ["oranges", "apples", "macintosh", "blueberries", "cashews", "bagels", "mushrooms", "oracles"]
        password = random.choice(passBank) + str(random.randint(10,100))
        print("and their password is >>> ", password)

        exit = input("To exit this program please press the C key >>> ")
        if exit == 'C':
            print("Exiting Program!")
            break

    if start == 'C':
        print("Exiting Program!")
        break
    else:
        start = input("Invalid Input! :( >> ")
##            start = input("input invalid: Please enter either A or B or C [capital letters!]>>> ")
