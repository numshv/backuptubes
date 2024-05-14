

def main():
    
    from src.account_regist import login, sign_up, logout
    from src.texts import intro, exited
    from src.parsers import csvtoarr, save
    from src.laboratory import lab
    from src.battle import battle
    from src.help import help
    from src.shop import shop
    from src.arena import arena
    from src.monstermanagement import monster_management
    import os
    
    user_arr = csvtoarr('user.csv')
    monster_inventory_arr = csvtoarr('monster_inventory.csv')
    item_inventory_arr = csvtoarr('potion_inventory.csv')
    monster_arr = csvtoarr('monster.csv')
    monster_shop_arr = csvtoarr('monster_shop.csv')
    item_shop_arr = csvtoarr('item_shop.csv')

    import argparse
    
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
            new_player = sign_up(user_arr, player_id, monster_arr)
            if login_state == 0:
                user_arr.append(new_player['user'])
                monster_inventory_arr.append(new_player['mons_inv'])
                item_inventory_arr.append([new_player['user'][0], 'strength', 0])
                item_inventory_arr.append([new_player['user'][0], 'resilience', 0])
                item_inventory_arr.append([new_player['user'][0], 'healing', 0])
        
        elif operation == "LAB": #checked
            after_lab_state = lab(monster_arr, monster_inventory_arr, player_oc, player_id)
            if login_state == 1:
                player_oc = after_lab_state[0]
                monster_inventory_arr = after_lab_state[1]
        
        elif operation == "BATTLE":
            if login_state == 1:
                oc_reward = battle(monster_arr, monster_inventory_arr, player_id, item_inventory_arr, player_oc)
                player_oc = int(oc_reward)
                print('Anda telah kembali di halaman utama OWCA, ketik "HELP" Kalau lupa command!\n')
            else:
                print('Anda belum login!\n')
        
        
        elif operation == "ARENA":
            if login_state == 1:
                oc_reward_arena = arena(monster_inventory_arr, player_id, monster_arr, item_inventory_arr)
                player_oc += oc_reward_arena
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
        
        elif operation == "EXIT": #checked
            exited()
        
        elif operation == "CEK":
            print(user_arr)
            print(monster_inventory_arr)
            print(monster_arr)
            print(item_inventory_arr)
            print(player_role)
            print(player_id)
            print(player_username)

        elif operation == "HELP": #checked
            help(login_state, player_role)

        elif operation == "SHOP":
            shop(monster_inventory_arr, item_inventory_arr, monster_shop_arr, item_shop_arr, monster_arr, player_oc)

        elif operation == "MONSTER_MANAGE": #checked
            monster_management(monster_arr, player_role)
        
        elif operation == "SAVE": #checked
            save(user_arr, monster_inventory_arr, item_inventory_arr, monster_arr, monster_shop_arr, item_shop_arr)
        
        else: #checked
            print("Command tidak valid! Lupa command? ketik HELP untuk mengetahui list command\n")

main()