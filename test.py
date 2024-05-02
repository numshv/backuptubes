from sys import exit
from time import sleep as wait

#STATING INITIAL STATE OF ALL GLOBAL VARIABLES
login_state = False
running_state = True


# Kayak fungsi split untuk baca isi csv
def csv_parser(line):
    s=[]
    j=0
    for i in range (len(line)):
        if ','== line [i]:
            s.append(line[j:i])
            j=i+1
    s.append (line[j:])
    return s

# Fungsi saat first time di play

def intro():
    print("""
 __      __         .__                                         __                               __                                      
/  \    /  \  ____  |  |    ____   ____    _____    ____      _/  |_  ____      ______    ____  |  | __  ____    _____    ____    ____   
\   \/\/   /_/ __ \ |  |  _/ ___\ /  _ \  /     \ _/ __ \     \   __\/  _ \     \____ \  /  _ \ |  |/ /_/ __ \  /     \  /  _ \  /    \  
 \        / \  ___/ |  |__\  \___(  <_> )|  Y Y  \\  ___/      |  | (  <_> )    |  |_> >(  <_> )|    < \  ___/ |  Y Y  \(  <_> )|   |  \ 
  \__/\  /   \___  >|____/ \___  >\____/ |__|_|  / \___  >     |__|  \____/     |   __/  \____/ |__|_ \ \___  >|__|_|  / \____/ |___|  / 
       \/        \/            \/              \/      \/                       |__|                 \/     \/       \/              \/  
""")

# Fungsi untuk milih metode masuk, mau login or sign in
def select_method():
    select = int(input("""Ayo masuk mas mba!
[1] LOGIN (jika sudah memiliki akun)
[2] SIGN UP (bila belum memiliki akun)
[3] EXIT (Enggak jadi main TT)
"""))
    if select == 1:
        login()
    elif select == 2:
        sign_up()
    else:
        print('Input tidak valid')
        select_method()

# Fungsi untuk login
def login():
    global login_state
    email = str(input('Masukkan username: '))
    password = str(input('Masukkan password: '))
    file = open('accounts.csv', 'r')
    for line in file:
        item = csv_parser(line)
        if email == item[0] and password == item[1]:
            print('Logged in successfully!')
            login_state = True
            return("")
        elif email == item[0] and password != item[1]:
            print('passwordnya salah bro, ulang yhh')
            login()
    print("Sorry, you aren't signed up yet.")

# Fungsi untuk sign up
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

def main():
    intro()
    if login_state == False:
        select_method()
    else:
        operation = input(">> ")
        if operation == "LOGIN":
            print("Anda telah Login dengan username")

main()
        
        