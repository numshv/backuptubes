#STATING INITIAL STATE OF ALL GLOBAL VARIABLES
login_state = 0
global_username = 'nope'
global_id = 0
running_state = True

user_arr = [['001','tes1','tes1','role',200], ['007','tes7','tes7','role',500]]


# Fungsi untuk login
def login(user_arr):
    global login_state
    global global_username
    global global_id
    if login_state == 1:
        print("Anda telah Login dengan username basudara")
    else:
        while True:
            username = str(input('Masukkan username: '))
            password = str(input('Masukkan password: '))
            for i in range (len(user_arr)):
                if username == user_arr[i][1] and password == user_arr[i][2]:
                    print('Logged in successfully!\n')
                    login_state = 1
                    global_id = user_arr[i][0]
                elif username == user_arr[i][1] and password != user_arr[i][2]:
                    print('passwordnya salah bro, ulang yhh\n')
                    login_state = 2
                else:
                    login_state = 0
            if login_state != 2:
                break
        if login_state == 0:
            print("Sorry, you aren't signed up yet. Type 'SIGNUP' to create an account\n")
        else:
            global_username = username

login(user_arr)
print(login_state)
print(global_username)
print(global_id)