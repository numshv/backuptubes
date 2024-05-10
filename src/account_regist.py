#STATING INITIAL STATE OF ALL GLOBAL VARIABLES
login_state = 0
global_username = 'nope'
global_id = 0
running_state = True

user_arr = [['001','tes1','tes1','role',200], ['007','tes7','tes7','role',500]]


# Fungsi untuk login
def login(global_username):
    global login_state
    if login_state == 1:
        print(f"Anda telah Login dengan username {global_username}")
        return 'logged in'
    else:
        while True:
            username = str(input('Masukkan username: '))
            password = str(input('Masukkan password: '))
            for i in range (len(user_arr)):
                if username == user_arr[i][1] and password == user_arr[i][2]:
                    print('Logged in successfully!\n')
                    login_state = 1
                    global_id = user_arr[i][0]
                    return user_arr[i]
                    break
                elif username == user_arr[i][1] and password != user_arr[i][2]:
                    print('passwordnya salah bro, ulang yhh\n')
                    login_state = 2
                    break
                else:
                    login_state = 0
            if login_state != 2:
                break
        if login_state == 0:
            print("Sorry, you aren't signed up yet. Type 'SIGNUP' to create an account\n")


# Fungsi untuk sign up
def sign_up():
    global user_arr
    username = str(input('Username: '))
    password = str(input('Password: '))
    info = ['id', username, password, 'role', 100]
    user_arr.append(info)

def logout(global_username, global_id):
    global login_state
    if login_state == 0:
        print("Anda belum Login")
    else:
        login_state = False
        print(f"Anda berhasil logout dari akun {global_username}")
