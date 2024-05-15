from math import floor
from time import sleep
from src.rng import RNG
from os import system

def print_potion(item_inventory_arr, global_id):
    j=0
    for i in range (len(item_inventory_arr)):
        if item_inventory_arr[i][0] == global_id:
            j += 1
            print(f"{j}. {item_inventory_arr[i][1]} potion (Qty: {item_inventory_arr[i][2]})")


    

def battle(monster_arr:list, monster_inventory_arr:list, global_id:str, item_inventory_arr:list, oc_player:int):
    if global_id == 'NaN':
        print('Anda belum login!, silahkan ketik perintah LOGIN untuk login ke akun anda\n')
    # if role admin blm dibikin
    else:
        
        system("cls")
        
        sleep(1)
        
        print("""
__________          __     __   .__                 _________  __                    __       ._. 
\______   \_____  _/  |_ _/  |_ |  |    ____       /   _____/_/  |_ _____  _______ _/  |_     | | 
|    |  _/\__  \ \   __\\   __\|  |  _/ __ \      \_____  \ \   __\\__    \ \_  __ \\   __\   | | 
|    |   \ / __ \_|  |   |  |  |  |__\  ___/      /        \ |  |   / __   \_|  | \/ |  |      \| 
|______  /(____  /|__|   |__|  |____/ \___  >    /_______  / |__|  (____    /|__|    |__|      __ 
        \/      \/                         \/             \/             \/                    \/ 
                                                                                                
            """)
        
        sleep(1.5)
        
        system("cls")
        
        print("""
    @@                     
    @                     
    @@  @%@     @@        
    @@@ @%@@@@@@@@        
        @@@@@@  @%  @        
        @@@@@@  @@  @        
        @@%@@@@@@@@@@        
    %%%@@@@@@@@@@         
    @@@@@@@@@@@@@@@        
    @@@@@@@@@@@@@@@@        
    @@@@ @@@@@@@@@@@@@       
@@@@  @@@@@     @@@@      
@@@    @@@@       @@@@    
@@@    @@@@        @@@@   
                                                    
    """)
        #rand range blm di ubah ke yg buatan sendiri
        enemy_info_arr_no = monster_arr[RNG(0, len(monster_arr)-1)]
        enemy_level = RNG(0, 5)
        
        #copy
        enemy_info_arr = enemy_info_arr_no.copy()
        
        if enemy_level != 1:
            for i in range(2, 5):
                enemy_info_arr[i] = float(enemy_info_arr[i]) + float(enemy_info_arr[i]) * (enemy_level-1) * 0.1
        
        print(f"""
RAWRRR, Monster {enemy_info_arr[1]} telah muncul !!!

Name      : {enemy_info_arr[1]}
ATK Power : {enemy_info_arr[2]}
DEF Power : {enemy_info_arr[3]}
HP        : {enemy_info_arr[4]}
Level     : {enemy_level}

    """)
        
        sleep(3)
        
        print('============ MONSTER LIST ============ ')
        
        monster_name = []
        monster_id = [0]
        monster_level = [0]

        actual_i = 0
        
        for i in range (len(monster_inventory_arr)):
            if monster_inventory_arr[i][0] == global_id:
                for j in range (len(monster_arr)):
                    if monster_inventory_arr[i][1] == monster_arr[j][0]: 
                        cur_monster = monster_arr[j][1]
                        monster_name.append(monster_arr[j][1])
                        monster_id.append(monster_arr[j][0])
                        actual_i += 1
                print(f"{actual_i}. {cur_monster} (Level: {monster_inventory_arr[i][2]})")
                monster_level.append(int(monster_inventory_arr[i][2]))
        

        player_mons_lvl = 0
        select_number = -999
        
        print('\nPilih monster yang akan kamu ajak bertarung!')
        
        while True:
            select_number = int(input('\n>>> Pilih monster nomor: '))
            if select_number <= len(monster_name):
                player_mons_lvl = monster_level[select_number]
                break
            else:
                print('Input tidak valid!')
        
        selected_id = monster_id[select_number]
        player_mons_info_no = monster_arr[int(selected_id)-1]
        
        # Copy
        player_mons_info = player_mons_info_no.copy()

        # Penyesuaian level figthing monster
        if player_mons_lvl != 1:
            for i in range(2, 5):
                player_mons_info[i] = int(float(player_mons_info[i]) + float(player_mons_info[i]) * float((player_mons_lvl-1)) * 0.1)
        
        print(f"""

            /\----/\_   
            /         \   /|
            |  | O    O | / |
            |  | .vvvvv.|/  /
          /   | |     |   /
          /    | `^^^^^   /
         | /|  |         /
         / |    ___    |
            \  |   |   |
            |  |   |   |
            \._\   \._\ 

RAWRRR, Agent X mengeluarkan monster {player_mons_info[1]} !!!

Name      : {player_mons_info[1]}
ATK Power : {player_mons_info[2]}
DEF Power : {player_mons_info[3]}
HP        : {player_mons_info[4]}
Level     : {player_mons_lvl}
""")

        sleep(3)
        
        turn = 1
        while True:
            while True: #Loop turn player
                print(f"""
============ TURN {turn} ({player_mons_info[1]}) | ANDA ============
1. Attack
2. Use Potion
3. Quit
                """)
                
                
                player_input = int(input('>>> Pilih perintah: '))
                player_attack = 0
                base_hp_player = player_mons_info[4]
                
                if player_input < 1 or player_input > 3:
                    print('Input tidak valid')
                
                else:
                    if player_input == 1:
                        player_attack = float(player_mons_info[2]) + (float(player_mons_info[2]) * 0.01 * RNG(-30, 30))
                        enemy_info_arr[4] = floor(int(enemy_info_arr[4]) - (player_attack * (100 - int(enemy_info_arr[3]))*0.01))
                        print(f'\nSCHWINKKK, {player_mons_info[1]} menyerang {enemy_info_arr[1]} !!!')
                        print(f'''
Name        : {enemy_info_arr[1]}
ATK Power   : {enemy_info_arr[2]}
DEF Power   : {enemy_info_arr[3]}
HP          : {enemy_info_arr[4]}
Level       : {enemy_level}
                    ''')
                        
                        break
                    
                    elif player_input == 2:
                        print('\n============ POTION LIST ============')
                        print_potion(item_inventory_arr, global_id)
                        print('4. Cancel \n')
                        
                        potion_input = int(input('>>> Pilih potion yang ingin digunakan: '))
                        
                        if potion_input != 4:
                            potion_info = item_inventory_arr[potion_input-1]
                            
                            if potion_info[1] == 'strength' and int(potion_info[2]) > 0:
                                player_mons_info[2] = float(player_mons_info[2]) + (float(player_mons_info[2]) * 0.05)
                                print('Setelah meminum potion ini, monster anda merasa semakin kuat!')
                            
                            elif potion_info[1] == 'resilience' and int(potion_info[2]) > 0:
                                player_mons_info[3] = float(player_mons_info[3]) + (float(player_mons_info[3]) * 0.05)
                                print('Setelah meminum potion ini, monster anda merasa lebih kuat!')
                            
                            elif potion_info[1] == 'healing' and int(potion_info[2]) > 0:
                                player_mons_info[4] = float(player_mons_info[4]) + (float(base_hp_player) * 0.25)
                                if player_mons_info[4] > base_hp_player:
                                    player_mons_info[4] = base_hp_player
                                print('Setelah meminum potion ini, monster anda merasa lebih sehat!')
                            break
                            
                    else:
                        exit(0)
            
            sleep(2)
            
            # If menang
            
            if enemy_info_arr[4] <= 0:
                oc_reward = RNG(50, 100)
                print(f'Selamat, Anda berhasil mengalahkan monster {enemy_info_arr[1]} !!!')
                print(f'Total OC yang didapatkan {oc_reward}')
                return oc_reward+int(oc_player)
            
            #Bagian enemy attack
            
            enemy_attack = int(enemy_info_arr[2]) + (int(enemy_info_arr[2]) * 0.01 * RNG(-30, 30))
            player_mons_info[4] = floor(float(player_mons_info[4]) - (enemy_attack * (100 - float(player_mons_info[3]))*0.01))
            
            print(f"""
============ TURN {turn} ({enemy_info_arr[1]}) | MUSUH ============

SCHWINKKK, {enemy_info_arr[1]} menyerang {player_mons_info[1]} !!!

Name        : {player_mons_info[1]}
ATK Power   : {player_mons_info[2]}
DEF Power   : {player_mons_info[3]}
HP          : {player_mons_info[4]}
Level       : {player_mons_lvl}
                """)
            
            # If kalah
            
            if player_mons_info[4] <= 0:
                print(f'Yahhh, Anda dikalahkan monster {enemy_info_arr[1]}. Jangan menyerah, masih ada kesempatan lain !!!')
                sleep(2)
                system("cls")
                print("""

  ________                              ________                        ._. 
 /  _____/ _____     _____    ____      \_____  \ ___  __  ____ _______ | | 
/   \  ___ \__  \   /     \ _/ __ \      /   |   \\  \/ /_/ __ \\_  __ \| | 
\    \_\  \ / __ \_|  Y Y  \\  ___/     /    |    \\   / \  ___/ |  | \/ \| 
 \______  /(____  /|__|_|  / \___  >    \_______  / \_/   \___  >|__|    __ 
        \/      \/       \/      \/             \/            \/         \/ 
                                                                            
""")
                sleep(3)
                system("cls")
                return int(oc_player)
            
            # If lanjut
            
            turn += 1
            sleep(3)

