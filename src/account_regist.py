
# Fungsi untuk login
def login(player_username, login_state, user_arr):
    if login_state == 1:
        print(f"Anda telah Login dengan username {player_username}")
        return 'logged in'
    else:
        while True:
            username = str(input('Masukkan username: '))
            password = str(input('Masukkan password: '))
            for i in range (len(user_arr)):
                if username == user_arr[i][1] and password == user_arr[i][2]:
                    print('Logged in successfully!\n')
                    return user_arr[i] + [1]
                elif username == user_arr[i][1] and password != user_arr[i][2]:
                    print('Password, silahkan ulang.\n')
                    login_state = 2
                    break
                else:
                    login_state = 0
            if login_state != 2:
                break
        if login_state == 0:
            print("Sorry, you aren't signed up yet. Type 'SIGNUP' to create an account\n")
            return 'not_signed_up'


# Fungsi untuk sign up
def sign_up(user_arr, player_id):
    if player_id != 'NaN':
        print('Anda sudah login!')
    
    else:
        while True:
            username = input('Username: ')
            password = input('Password: ')
            cond = True
            
            for i in range (len(user_arr)):
                if user_arr[i][1] == username:
                    print('Username sudah ada yang menggunakan, coba username lain!')
                    cond = False
            
            if cond == True:
                for i in range (len(password)):
                    ord_letter = ord(password[i])
                    if 57<ord_letter<65 or 45<ord_letter<48 or ord_letter< 45 or 90<ord_letter<94 or ord_letter == 96 or ord_letter>122:
                        cond = False
                
                if cond == True:
                    print(f'Anda berhasil membuat akun {username}, silahkan lanjut LOGIN untuk masuk ke dalam akun dan mulai bermain!')
                    return['id', username, password, 'agent', 0]
                
                else:
                    print('Password hanya boleh mengandung huruf, angka, strip (-), dan underscore (_), silahkan ulangi')
        

def logout(player_username, login_state):
    if login_state == 0:
        print("Anda belum Login")
        return 'logged_out_alr'
    else:
        print(f"Anda berhasil logout dari akun {player_username}")
        return['NaN', 'NaN', 'NaN', 'NaN', 0, 0]
