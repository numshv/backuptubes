

def main():
    
    from src.account_regist import login, sign_up, logout
    from src.texts import intro, exited
    from src.parsers import csvtoarr, RNG
    from src.laboratory import lab
    from src.battle import battle
    from src.help import help
    from src.shop import shop
    from src.arena import arena
    import os
    
    user_arr = csvtoarr('user.csv')
    monster_inventory_arr = csvtoarr('monster_inventory.csv')
    potion_inventory_arr = csvtoarr('potion_inventory.csv')
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
        if operation == "LOGIN": 
            user_info = login(player_username, login_state, user_arr)
            if user_info != 'logged in' and user_info != 'not_signed_up':
                player_username = user_info[1]
                player_id = user_info[0]
                player_oc = user_info[4]
                player_role = user_info[3]
                login_state = user_info[5]
            
        elif operation == "REGISTER":
            new_player = sign_up(user_arr, player_id, monster_arr)
            if login_state == 0:
                user_arr.append(new_player['user'])
                monster_inventory_arr.append(new_player['mons_inv'])
        
        elif operation == "LAB": 
            after_lab_state = lab(monster_arr, monster_inventory_arr, player_oc, player_id)
            if login_state == 1:
                player_oc = after_lab_state[0]
                monster_inventory_arr = after_lab_state[1]
        
        elif operation == "BATTLE":
            oc_reward = battle(monster_arr, monster_inventory_arr, player_id, potion_inventory_arr, player_oc)
            player_oc = int(oc_reward)
        
        elif operation == "ARENA":
            oc_reward_arena = arena(monster_inventory_arr, player_id, monster_arr, potion_inventory_arr)
            player_oc += oc_reward_arena
        
        elif operation == "LOGOUT":
            logout_info = logout(player_username, login_state)
            if logout_info != 'logged_out_alr':
                player_username = logout_info[1]
                player_id = logout_info[0]
                player_oc = logout_info[4]
                player_role = logout_info[3]
                login_state = logout_info[5]
        
        elif operation == "EXIT":
            exited()
        
        elif operation == "CEK":
            print(user_arr)
            print(monster_inventory_arr)

        elif operation == "HELP":
            help(login_state, player_role)

        elif operation == "SHOP":
            shop(monster_inventory_arr, potion_inventory_arr, monster_shop_arr, item_shop_arr, monster_arr, player_oc)

        else:
            print("Command tidak valid! Lupa command? ketik HELP untuk mengetahui list command\n")

main()