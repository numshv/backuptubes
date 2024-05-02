from sys import exit
from time import sleep as wait

def select_method():
    select = int(input("""Chosse what you want to do:
[1] LOGIN
[2] SIGN UP
"""))
    if select == 1:
        login()
    elif select == 2:
        sign_up()
    else:
        print('Choose a valid operation')

def login():
    email = str(input('Email: '))
    password = str(input('Password: '))
    file = open('accounts.csv', 'r')
    for line in file:
        item = line.split(',')
        if email == item[0] and password == item[1]:
            print('Logged in successfully!')
            exit(0)
    print("Sorry, you aren't signed up yet.")

def sign_up():
    email = str(input('Email: '))
    password = str(input('Password: '))
    file = open('accounts.csv', 'a')
    info = '\n' + email + ',' + password
    file.write(info)
    print('Do you want to log in? [Yes/No]')
    start_over = str(input()).lower()
    file.close()
    if 'y' in start_over:
        login()
    else:
        print('See you next time!')
        wait(2)
        exit(0)


select_method()
