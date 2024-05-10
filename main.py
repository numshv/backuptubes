from src.account_regist import login, sign_up, logout
from src.texts import intro, help, exited
from src.parsers import csvtoarr
from src.laboratory import lab

#STATING INITIAL STATE OF ALL GLOBAL VARIABLES
running_state = True
user_arr = csvtoarr('user.csv')
monster_inventory_arr = csvtoarr('monster_inventory.csv')
potion_inventory_arr = csvtoarr('potion_inventory.csv')
monster_arr = csvtoarr('monster.csv')

login_state = 0
global_username = 'nope'
global_id = 0
global_oc = 0
running_state = True


def main():
    global global_username
    global global_id
    global global_oc
    global monster_inventory_arr
    intro()
    while running_state == True:
        operation = input(">> ")
        if operation == "LOGIN": 
            user_info = login(global_username)
            if user_info != 'logged in':
                global_username = user_info[1]
                global_id = user_info[0]
                global_oc = user_info[4]
            
        elif operation == "SIGNUP":
            sign_up()
        
        elif operation == "HELP":
            help()
        
        elif operation == "LAB": #blm integrated sama oc dan ganti level langsung
            after_lab_state = lab(monster_arr, monster_inventory_arr, global_oc, global_id)
            global_oc = after_lab_state[0]
            monster_inventory_arr = after_lab_state[1]
        
        elif operation == "LOGOUT":
            logout(global_username, global_id)
        
        elif operation == "EXIT":
            exited()
        
        elif operation == "CEK":
            print(monster_inventory_arr, global_oc)
            print(global_id, global_username)
        
        else:
            print("Command tidak valid! Lupa command? ketik HELP untuk mengetahui list command")

main()