import os
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
    # Mau tambahin tulisan buat akses help sama cerita awal

# Fungsi untuk navigasi command
def help():
    pass

# Fungsi untuk login
def login():
    global login_state
    user_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'databases', 'user.csv')
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
    user_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'databases', 'user.csv')
    file = open(user_path, 'a')
    info = '\n' + 'id' + ',' + username + ',' + password + ',' + 'role' + ',' + 'oc'
    file.write(info)
    #print('Do you want to log in? [Yes/No]')       LIHAT INI BRO
    #start_over = str(input()).lower()
    #file.close()
    #if 'y' in start_over:
    #    login()
    #else:
    #    print('See you next time!')
    #    wait(2)
    #    exit(0)

def logout():
    global login_state
    login_state = False
    print("Anda berhasil logout dari akun basudara")

def exited():
    global running_state
    print("""
__________                     __________                  
\______   \ ___.__.  ____      \______   \ ___.__.  ____   
 |    |  _/<   |  |_/ __ \      |    |  _/<   |  |_/ __ \  
 |    |   \ \___  |\  ___/      |    |   \ \___  |\  ___/  
 |______  / / ____| \___  >     |______  / / ____| \___  > 
        \/  \/          \/             \/  \/          \/  
                                                            
          """)
    running_state == False
    exit(0)

def main():
    intro()
    while running_state == True:
        operation = input(">> ")
        if operation == "LOGIN":
            if login_state == True:
                print("Anda telah Login dengan username basudara")
            else:
                login()
            
        elif operation == "SIGNUP":
            sign_up()
        
        elif operation == "LOGOUT":
            logout()
        
        elif operation == "EXIT":
            exited()

main()