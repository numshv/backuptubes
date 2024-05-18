import os
from time import sleep

def login(player_username, login_state, user_arr):
    if login_state == 1:
        print(f"Anda telah Login dengan username {player_username}\n")
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

def arrtocsv(arr, path, header_i):
    arr_header = ['user_id,type,quantity', 'type,stock,price', 'id,type,atk,def,hp', 'user_id,monster_id,level', 'monster_id,stock,price', 'user_id,type,quantity', 'id,username,password,role,oc']
    file = open(path, 'w')

    file.write(str(arr_header[header_i]) + '\n')
    for i in range(len(arr)):
        cur_str = ''
        cur_sub = arr[i]
        for j in range(len(cur_sub)):
            if j != len(cur_sub)-1:
                cur_str += str(cur_sub[j]) + ','
            else:
                cur_str += str(cur_sub[j])
        file.write(cur_str+'\n')

def save(item_inventory_arr, item_shop_arr, monster_inventory_arr, monster_shop_arr, monster_arr, potion_inventory_arr, user_arr,player_id, player_oc):
    folder = input('Masukkan nama folder: ')
    print('saving . . . \n')
    sleep(3)
    
    for i in range (len(user_arr)):
        if user_arr[i][0] == player_id:
            user_arr[i][4] = player_oc
    
    data_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)),'databases')
    isExist =  os.path.exists(os.path.join(data_path, folder))
    if isExist == False:
        os.makedirs(os.path.join(data_path, folder))
        print(f'Membuat folder data/{folder}...\n')
    cur_dir = os.path.join(data_path, folder)
    arrtocsv(item_inventory_arr,os.path.join(cur_dir, 'item_inventory.csv'), 0)
    arrtocsv(item_shop_arr, os.path.join(cur_dir, 'item_shop.csv'), 1)
    arrtocsv(monster_inventory_arr, os.path.join(cur_dir, 'monster_inventory.csv'), 3)
    arrtocsv(monster_shop_arr, os.path.join(cur_dir, 'monster_shop.csv'), 4)
    arrtocsv(monster_arr, os.path.join(cur_dir, 'monster.csv'), 2)
    arrtocsv(potion_inventory_arr, os.path.join(cur_dir, 'potion_inventory.csv'), 5)
    arrtocsv(user_arr, os.path.join(cur_dir, 'user.csv'), 6)
    print(f'Berhasil menyimpan data di folder data/{folder}!')


def exited(item_inventory_arr, item_shop_arr, monster_inventory_arr, monster_shop_arr, monster_arr, potion_inventory_arr, user_arr,player_id, player_oc):
    while True:
        save_input = input('Apakah anda mau menyimpan perubahan terlebih dahulu?(y/n): ')
        if save_input != 'y' and save_input != 'n':
            print('Input tidak valid!\n')
        elif save_input == 'y':
            save(item_inventory_arr, item_shop_arr, monster_inventory_arr, monster_shop_arr, monster_arr, potion_inventory_arr, user_arr,player_id, player_oc)
            break
        else:
            break
    print("""
__________                     __________                  
\______   \ ___.__.  ____      \______   \ ___.__.  ____   
 |    |  _/<   |  |_/ __ \      |    |  _/<   |  |_/ __ \  
 |    |   \ \___  |\  ___/      |    |   \ \___  |\  ___/  
 |______  / / ____| \___  >     |______  / / ____| \___  > 
        \/  \/          \/             \/  \/          \/  
                                                            
          """)
    exit(0)

#def save(user_arr, monster_inventory_arr, item_inventory_arr, monster_arr, monster_shop_arr, item_shop_arr):
    