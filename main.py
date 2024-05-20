import argparse
import os
from time import sleep


def main(folder):
    from src.account_regist import login, register, logout, save, exited
    from src.texts import intro
    from src.parsers import csvtoarr, RNG
    from src.laboratory import lab
    from src.battle import battle
    from src.help import help
    from src.shop import shop
    from src.arena import arena
    from src.inventory import inventory
    from src.monstermanagement import monster_management
    from src.shopmanagement import shop_management
    import os
    
    user_arr = csvtoarr(folder, 'user.csv')
    monster_inventory_arr = csvtoarr(folder, 'monster_inventory.csv')
    item_inventory_arr = csvtoarr(folder, 'potion_inventory.csv')
    monster_arr = csvtoarr(folder, 'monster.csv')
    monster_shop_arr = csvtoarr(folder, 'monster_shop.csv')
    item_shop_arr = csvtoarr(folder, 'item_shop.csv')
    
    #STATING INITIAL STATE OF ALL GLOBAL VARIABLES
    running_state = True
    player_username = 'NaN'
    player_id = 'NaN'
    player_oc = 0
    player_role = 'NaN'
    login_state = 0
    
    os.system("cls")
    intro()
    while running_state == True:
        operation = input(">> ")
        if operation == "LOGIN": #checked
            user_info = login(player_username, login_state, user_arr)
            if user_info != 'logged in' and user_info != 'not_signed_up':
                player_username = user_info[1]
                player_id = user_info[0]
                player_oc = user_info[4]
                player_role = user_info[3]
                login_state = user_info[5]
            
        elif operation == "REGISTER": #checked
            new_player = register(user_arr, player_id, monster_arr)
            if login_state == 0:
                user_arr.append(new_player['user'])
                monster_inventory_arr.append(new_player['mons_inv'])
                item_inventory_arr.append([new_player['user'][0], 'strength', 0])
                item_inventory_arr.append([new_player['user'][0], 'resilience', 0])
                item_inventory_arr.append([new_player['user'][0], 'healing', 0])
        
        elif operation == "SHOP_MANAGE": #checked
            shop_management(login_state, player_role, monster_shop_arr, item_shop_arr, monster_arr)
        
        elif operation == "LAB": #checked
            after_lab_state = lab(monster_arr, monster_inventory_arr, player_oc, player_id)
            if login_state == 1:
                player_oc = after_lab_state[0]
                monster_inventory_arr = after_lab_state[1]
        
        elif operation == "BATTLE":
            if login_state == 1:
                oc_reward = battle(monster_arr, monster_inventory_arr, player_id, item_inventory_arr, player_oc,player_role)
                player_oc = int(oc_reward)
                print('Anda telah kembali di halaman utama OWCA, ketik "HELP" Kalau lupa command!\n')
            else:
                print('Anda belum login!\n')
        
        
        elif operation == "ARENA":
            if login_state == 1:
                oc_reward_arena = arena(monster_inventory_arr, player_id, monster_arr, item_inventory_arr)
                player_oc = str(int(player_oc) + oc_reward_arena)
            else:
                print('Anda belum login!\n')
        
        elif operation == "LOGOUT":#checked
            logout_info = logout(player_username, login_state)
            if logout_info != 'logged_out_alr':
                player_username = logout_info[1]
                player_id = logout_info[0]
                player_oc = logout_info[4]
                player_role = logout_info[3]
                login_state = logout_info[5]
        
        elif operation == "INVENTORY":
            inventory(player_id, monster_inventory_arr, item_inventory_arr, player_oc, monster_arr, player_role)
        
        elif operation == "EXIT": #checked
            exited(item_inventory_arr, item_shop_arr, monster_inventory_arr, monster_shop_arr, monster_arr, item_inventory_arr, user_arr, player_id, player_oc)
        
        elif operation == 'RNG':
            print(RNG(0, 2))
        
        elif operation == "CEK":
            print(user_arr)
            print(monster_inventory_arr)
            print(monster_arr)
            print(item_inventory_arr)
            print(player_role)
            print(player_id, type(player_id))
            print(player_username)
            print(item_shop_arr)
            print(monster_shop_arr)

        elif operation == "HELP": #checked
            help(login_state, player_role)

        elif operation == "SHOP":
            shop(monster_inventory_arr, item_inventory_arr, monster_shop_arr, item_shop_arr, monster_arr, player_oc)

        elif operation == "MONSTER_MANAGE": #checked
            monster_management(monster_arr, player_role)
        
        elif operation == "SAVE": #checked
            save(item_inventory_arr, item_shop_arr, monster_inventory_arr, monster_shop_arr, monster_arr, item_inventory_arr, user_arr, player_id,player_oc)
        
        else: #checked
            print("Command tidak valid! Lupa command? ketik HELP untuk mengetahui list command\n")

def checker(folder):
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'databases')
    isExist =  os.path.exists(os.path.join(data_path, folder))
    if isExist == False:
        raise argparse.ArgumentTypeError('Folder tidak ditemukan')
    return folder

def load():
    parser = argparse.ArgumentParser(description='Mengakses folder database')
    parser.add_argument('folder', type=checker)
    
    prs = parser.parse_args()
    folder = prs.folder
    print("Selamat datang di OWCA")
    sleep(3)
    main(folder)

load()