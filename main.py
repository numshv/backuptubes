

def main():
    
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number",
                        type=int)
    args = parser.parse_args()
    print(args.square)
    
    user_arr = csvtoarr('user.csv')
    monster_inventory_arr = csvtoarr('monster_inventory.csv')
    potion_inventory_arr = csvtoarr('potion_inventory.csv')
    monster_arr = csvtoarr('monster.csv')
    
    from src.account_regist import login, sign_up, logout
    from src.texts import intro, help, exited
    from src.parsers import csvtoarr
    from src.laboratory import lab
    from src.battle import battle

    #STATING INITIAL STATE OF ALL GLOBAL VARIABLES
    running_state = True
    global_username = 'NaN'
    global_id = 'NaN'
    global_oc = 0
    player_role = 'NaN'
    running_state = True
    login_state = 0
    
    
    intro()
    while running_state == True:
        operation = input(">> ")
        if operation == "LOGIN": 
            user_info = login(global_username, login_state, user_arr)
            if user_info != 'logged in' and user_info != 'not_signed_up':
                global_username = user_info[1]
                global_id = user_info[0]
                global_oc = user_info[4]
                player_role = user_info[3]
                login_state = user_info[5]
            
        elif operation == "SIGNUP":
            new_player = sign_up(user_arr, global_id)
            user_arr.append(new_player)
        
        elif operation == "HELP":
            help()
        
        elif operation == "LAB": #blm integrated sama oc dan ganti level langsung
            after_lab_state = lab(monster_arr, monster_inventory_arr, global_oc, global_id)
            global_oc = after_lab_state[0]
            monster_inventory_arr = after_lab_state[1]
        
        elif operation == "BATTLE":
            oc_reward = battle(monster_arr, monster_inventory_arr, global_id, potion_inventory_arr, global_oc)
            global_oc = int(oc_reward)
        
        elif operation == "LOGOUT":
            logout_info = logout(global_username, login_state)
            if logout_info != 'logged_out_alr':
                global_username = logout_info[1]
                global_id = logout_info[0]
                global_oc = logout_info[4]
                player_role = logout_info[3]
                login_state = logout_info[5]
        
        elif operation == "EXIT":
            exited()
        
        elif operation == "CEK":
            print(global_id, global_username, global_oc)
            print(monster_arr)
            print(user_arr)
            print(monster_inventory_arr)
            print(potion_inventory_arr)
        
        else:
            print("Command tidak valid! Lupa command? ketik HELP untuk mengetahui list command")

main()