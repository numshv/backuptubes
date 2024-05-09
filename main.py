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


def main():
    intro()
    while running_state == True:
        operation = input(">> ")
        if operation == "LOGIN":
            login()
            
        elif operation == "SIGNUP":
            sign_up()
        
        elif operation == "HELP":
            help()
        
        elif operation == "LAB":
            lab(monster_inventory_arr, monster_arr)
        
        elif operation == "LOGOUT":
            logout()
        
        elif operation == "EXIT":
            exited()
        
        else:
            print("Command tidak valid! Lupa command? ketik HELP untuk mengetahui list command")

main()