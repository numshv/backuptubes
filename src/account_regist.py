import os
from src.parser import csv_parser

#STATING INITIAL STATE OF ALL GLOBAL VARIABLES
login_state = False
running_state = True


# Fungsi untuk login
def login():
    global login_state
    if login_state == True:
        print("Anda telah Login dengan username basudara")
    else:
        user_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)),'databases', 'user.csv')
        username = str(input('Masukkan username: '))
        password = str(input('Masukkan password: '))
        file = open(user_path, 'r')
        for line in file:
            item = csv_parser(line)
            if username == item[1] and password == item[2]:
                print('Logged in successfully!')
                login_state = True
                return("")
            elif username == item[1] and password != item[2]:
                print('passwordnya salah bro, ulang yhh')
                login()
        if login_state == False:
            print("Sorry, you aren't signed up yet. Type 'SIGNUP' to create an account") #masih ke double
            return("")

# Fungsi untuk sign up
def sign_up():
    username = str(input('Username: '))
    password = str(input('Password: '))
    user_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)),'databases', 'user.csv')
    file = open(user_path, 'a')
    info = '\n' + 'id' + ',' + username + ',' + password + ',' + 'role' + ',' + 'oc'
    file.write(info)

def logout():
    global login_state
    login_state = False
    print("Anda berhasil logout dari akun basudara")