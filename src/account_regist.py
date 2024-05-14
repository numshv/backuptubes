
# Fungsi untuk login
def login(player_username, login_state, user_arr):
    if login_state == 1:
        print(f"Anda telah Login dengan username {player_username}")
        return 'logged in'
    else:
        print('\n=============== LOGIN ===============\n')
        while True:
            username = str(input('Masukkan username: '))
            password = str(input('Masukkan password: '))
            for i in range (len(user_arr)):
                if username == user_arr[i][1] and password == user_arr[i][2]:
                    print(f'\nSelamat datang agent {username}, Anda berhasil login ke akun anda.\n')
                    return user_arr[i] + [1]
                elif username == user_arr[i][1] and password != user_arr[i][2]:
                    print('Password salah, silahkan ulang.\n')
                    login_state = 2
                    break
                else:
                    login_state = 0
            if login_state != 2:
                break
        if login_state == 0:
            print("Wah sepertinya kamu belum memiliki akun, ketik 'SIGNUP' untuk membuat akun baru!\n")
            return 'not_signed_up'


# Fungsi untuk sign up
def sign_up(user_arr, player_id, monster_arr):
    if player_id != 'NaN':
        print('Anda sudah login!')
    
    else:
        print('\n=============== REGISTER ===============\n')
        print('Username yang dimasukkan harus unik')
        print('Password hanya dapat mengandung huruf, angka, strip(-), dan underscore(_)\n')
        while True:
            username = input('Username: ')
            password = input('Password: ')
            cond = True
            
            for i in range (len(user_arr)):
                if user_arr[i][1] == username:
                    print('Username sudah ada yang menggunakan, coba username lain!\n')
                    cond = False
            
            if cond == True:
                for i in range (len(password)):
                    ord_letter = ord(password[i])
                    if 57<ord_letter<65 or 45<ord_letter<48 or ord_letter< 45 or 90<ord_letter<94 or ord_letter == 96 or ord_letter>122:
                        cond = False
                
                if cond == True:
                    print('\nSilahkan pilih salah satu monster sebagai monster awalmu.')
                    for i in range (len(monster_arr)):
                        print(f'{i+1}. {monster_arr[i][1]}')
                    while True:
                        print('\n')
                        monster_pick = int(input('>>> Pilih monster nomor?: '))
                        if monster_pick <= len(monster_arr):
                            break
                        else:
                            print('Input tidak valid!')
                    picked_monster = monster_arr[monster_pick-1][0]
                    add_user_arr = [len(user_arr)+1, username, password, 'agent', 0]
                    add_mons_inv_arr = [len(user_arr)+1, picked_monster, 1]
                    print(f'Anda berhasil membuat akun {username}, silahkan lanjut LOGIN untuk masuk ke dalam akun dan mulai bermain!\n')
                    return {'user': add_user_arr, 'mons_inv': add_mons_inv_arr}
                
                else:
                    print('Password hanya boleh mengandung huruf, angka, strip (-), dan underscore (_), silahkan ulangi\n')
        

def logout(player_username, login_state):
    if login_state == 0:
        print("Anda belum Login\n")
        return 'logged_out_alr'
    else:
        print(f"Anda berhasil logout dari akun {player_username}\n")
        return['NaN', 'NaN', 'NaN', 'NaN', 0, 0]
