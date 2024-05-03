from src.account_regist import login, sign_up, logout
from src.texts import intro, help, exited


#STATING INITIAL STATE OF ALL GLOBAL VARIABLES
running_state = True

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
        
        elif operation == "LOGOUT":
            logout()
        
        elif operation == "EXIT":
            exited()
        
        else:
            print("Command tidak valid! Lupa command? ketik HELP untuk mengetahui list command")

main()