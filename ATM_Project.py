

import os


def startUp(fname):
    d = dict()
    if os.path.exists(fname):
        file = open(fname, "r")
        for line in file:
            pin, first_name, last_name, balance = line.split(',')
            balance = float(balance)
            d[pin] = [first_name, last_name, balance]
        return d
    else:
        print('cannot get to the file')
        return None


def verifyPin(dict):

    # Attempt 1
    pin = input('Please enter your pin: ')

    # Attempt 2 - 3
    for i in range(2):

        # if the pin does exist in dictionary
        if pin in dict:

            # then return the pin and users first name
            return [pin, dict[pin][0]]
        else:
            pin = input('Invalid pin, try again: ')

    return [None, 'Please call customer support at 800-000-000']


def displayMenu(first_name):
    print(first_name)
    print('1. Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Quit')

    choice = input('Enter your choice: ')
    return choice


def verifyMenuChoice(first_name):
    non_nume = 'Invalid choice non-numeric characters not allowed, try again'
    while(True):
        try:
            choice = int(displayMenu(first_name))
            if choice < 1 or choice > 4:
                print('Valid choices are 1, 2, 3, 4 try again')

            # Checking to see if choice is a value between 1 - 4
            for i in range(1, 5):
                if choice == i:
                    return choice
        except ValueError:
            print(non_nume)


def verifyAmount():
    while(True):
        try:
            amount = float(input("Enter the amount: "))
            if amount < 0:
                print('Negative amount. Please try again')
            else:
                return amount
        except ValueError:
            print('Invalid amount. Use digits only.')


def deposit(pin, dict):
    amount = verifyAmount()

    # updating users balance
    dict[pin][2] += amount
    return


def withdraw(pin, dict):
    amount = verifyAmount()
    while amount > dict[pin][2]:
        print('Insufficient funds to complete the transaction')
        amount = verifyAmount()
    dict[pin][2] -= amount
    return


def balance(pin, dict):
    return dict[pin][2]


def quit(pin, dict):
    while(True):
        answer = (input('Do you wish to leave the transaction y/n: ')).lower()
        if answer == 'y':
            return [dict[pin][0], dict[pin][1]]
        elif answer == 'n':
            return [None, None]
        else:
            print('enter y to quit or n otherwise')


def main():
    dict = startUp('accounts.csv')
    if dict is None:
        return
    pin, value = verifyPin(dict)
    if pin is None:
        msg = value
        print(msg)
        return 'Good bye'
    name = value

    while True:
        print()
        choice = verifyMenuChoice(name)
        if choice == 2:
            deposit(pin, dict)
        elif choice == 3:
            withdraw(pin, dict)
        elif choice == 1:
            b = balance(pin, dict)
            msg = 'Your current balance is ${:,.2f}'
            print(msg.format(b))
        elif choice == 4:
            fname, lname = quit(pin, dict)
            if fname is None and lname is None:
                pass
            else:
                str = '\n{} {}, thank you for using the ABC Banking System'
                print(str.format(fname, lname))
                break
    return 'Goodbye'


main()
