from math import floor
from time import sleep
from src.rng import RNG
from os import system

def is_int(str):
    cond = True
    for i in range(len(str)):
        cur_ord = ord(str[i])
        if cur_ord < 48 or cur_ord > 57:
            cond = False
    return cond

mons_1 = '''                               
      .-"-.
    _/_-.-_\_
   / __} {__ \\
  / //  "  \\  \\
 /  \\     //   \\
/    '.___.'    \\
\     /__\     /
 \___/____\___/                  
'''

mons_2 = '''
    =/\                 /\=
    / \'._   (\_/)   _.'/ \\
   / .''._'--(o.o)--'_.''. \\
  /.' _/ |`'=/ " \='`| \_ `.\\
 /` .' `\;-,'\___/',-;/` '. '\\
/.-'       `\(-V-)/`       `-.\\
`            "   "            `
'''

mons_3 = '''
                           <\              _
                            \\          _/{
                     _       \\       _-   -_
                   /{        / `\   _-     - -_
                 _~  =      ( @  \ -        -  -_
               _- -   ~-_   \( =\ \           -  -_
             _~  -       ~_ | 1 :\ \      _-~-_ -  -_
           _-   -          ~  |V: \ \  _-~     ~-_-  -_
        _-~   -            /  | :  \ \            ~-_- -_
     _-~    -   _.._      {   | : _-``               ~- _-_
  _-~   -__..--~    ~-_  {   : \:}
=~__.--~~              ~-_\  :  /
                           \ : /__
                          //`Y'--\\      
                         <+       \\
                          \\      WWW
                          MMM
'''

mons_4 = '''
 .             _.--._       /|
        .    .'()..()`.    / /
            ( `-.__.-' )  ( (    .
   .         \        /    \ \\
       .      \      /      ) )        .
            .' -.__.- `.-.-'_.'
 .        .'  /-____-\  `.-'       .
          \  /-.____.-\  /-.
           \ \`-.__.-'/ /\|\|           .
          .'  `.    .'  `.
          |/\/\|    |/\/\|
'''

mons_5 = '''
 <>=======() 
(/\___   /|\\          ()==========<>_
      \_/ | \\        //|\   ______/ \)
        \_|  \\      // | \_/
          \|\/|\_   //  /\/
           (oo)\ \_//  /
          //_/\_\/ /  |
         @@/  |=\  \  |
              \_=\_ \ |
                \==\ \|\_ 
             __(\===\(  )\\
            (((~) __(_/   |
                 (((~) \  /
                 ______/ /
                 '------'
'''

mons_pict =[mons_1, mons_2, mons_3, mons_4, mons_5]

def print_potion(item_inventory_arr, player_id, player_item_inv_arr:list):
    j=0
    for i in range (len(item_inventory_arr)):
        if item_inventory_arr[i][0] == player_id:
            j += 1
            print(f"{j}. {item_inventory_arr[i][1]} potion (Qty: {item_inventory_arr[i][2]})")
            player_item_inv_arr.append(item_inventory_arr[i])


def battle(monster_arr:list, monster_inventory_arr:list, global_id:str, item_inventory_arr:list, oc_player:int, player_role):
    if global_id == 'NaN':
        print('Anda belum login!, silahkan ketik perintah LOGIN untuk login ke akun anda\n')
        return oc_player

    elif player_role == 'admin':
        print('Admin tidak dapat mengakses fitur ini.')
        return oc_player
    
    else:
        
        system("cls")
        
        sleep(1)
        print("""
__________          __     __   .__                     _________  __                    __   ._. 
\______   \_____  _/  |_ _/  |_ |  |    ____           /   _____/_/  |_ _____  _______ _/  |_ | | 
 |    |  _/\__  \ \   __\\   __\|  |  _/ __ \          \_____  \ \   __\\__  \ \_  __ \\   __\| | 
 |    |   \ / __ \_|  |   |  |  |  |__\  ___/          /        \ |  |   / __ \_|  | \/ |  |   \| 
 |______  /(____  /|__|   |__|  |____/ \___  >        /_______  / |__|  (____  /|__|    |__|   __ 
        \/      \/                         \/                 \/             \/                \/ 
            """)
        
        sleep(1.5)
        
        system("cls")
        
        print(mons_pict[RNG(0,4)])
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

            select_number_no = input('\n>>> Pilih monster nomor: ')
            if is_int(select_number_no) == True:
                select_number= int(select_number_no)
                if select_number <= len(monster_name):
                    player_mons_lvl = monster_level[select_number]
                    break
                else:
                    print('Input tidak valid!')
            else:
                print('Input harus berupa integer.')
        
        selected_id = monster_id[select_number]
        player_mons_info_no = monster_arr[int(selected_id)-1]
        
        # Copy
        player_mons_info = player_mons_info_no.copy()

        # Penyesuaian level figthing monster
        if player_mons_lvl != 1:
            for i in range(2, 5):
                player_mons_info[i] = int(float(player_mons_info[i]) + float(player_mons_info[i]) * float((player_mons_lvl-1)) * 0.1)
        
        
        print(mons_pict[RNG(0,4)])
        print(f"""

RAWRRR, Agent X mengeluarkan monster {player_mons_info[1]} !!!

Name      : {player_mons_info[1]}
ATK Power : {player_mons_info[2]}
DEF Power : {player_mons_info[3]}
HP        : {player_mons_info[4]}
Level     : {player_mons_lvl}
""")

        sleep(3)
        
        turn = 1
        strength_used = False
        resilience_used = False
        healing_used = False
        while True:
            while True: #Loop turn player
                print(f"""
============ TURN {turn} ({player_mons_info[1]}) | ANDA ============
1. Attack
2. Use Potion
3. Quit
                """)
                
                
                player_input_no = input('>>> Pilih perintah: ')
                
                if is_int(player_input_no) == True:
                    player_input = int(player_input_no)
                    player_attack = 0
                    base_hp_copy = player_mons_info_no.copy()
                    base_hp_player = int(base_hp_copy[4]) + int(float(base_hp_copy[4]) * float((player_mons_lvl-1)) * 0.1)
                    
                    if player_input < 1 or player_input > 3:
                        print('Input tidak valid')
                    
                    else:
                        if player_input == 1:
                            player_attack = float(player_mons_info[2]) + (float(player_mons_info[2]) * 0.01 * RNG(-30, 30))
                            pengali = (1 - (int(enemy_info_arr[3])*0.01))
                            deal_damage = floor(player_attack * pengali)
                            enemy_info_arr[4] = int(enemy_info_arr[4]) - deal_damage
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
                            player_item_inv_arr = []
                            print('\n============ POTION LIST ============')
                            print_potion(item_inventory_arr, global_id, player_item_inv_arr)
                            print(f'{len(player_item_inv_arr)+1}. Cancel \n')
                            
                            while True:
                                potion_input_no = input('>>> Pilih potion yang ingin digunakan: ')
                                cond_potion_done = False
                                
                                if is_int(potion_input_no) ==True:
                                    potion_input = int(potion_input_no)
                                    if 0<potion_input<len(player_item_inv_arr)+2:
                                        if 0<potion_input<len(player_item_inv_arr)+1:
                                            potion_info = player_item_inv_arr[potion_input-1]
                                            if potion_info[1] == 'strength' and int(potion_info[2]) > 0 and strength_used == False:
                                                player_mons_info[2] = floor(float(player_mons_info[2]) + (float(player_mons_info[2]) * 0.05))
                                                potion_info[2] = int(potion_info[2])-1
                                                strength_used= True
                                                cond_potion_done= True
                                                print('Setelah meminum potion ini, monster anda merasa semakin kuat!')
                                            
                                            elif potion_info[1] == 'resilience' and int(potion_info[2]) > 0 and resilience_used == False:
                                                player_mons_info[3] = floor(float(player_mons_info[3]) + (float(player_mons_info[3]) * 0.05))
                                                potion_info[2] = int(potion_info[2])-1
                                                resilience_used = True
                                                cond_potion_done = True
                                                print('Setelah meminum potion ini, monster anda merasa lebih kuat!')
                                            
                                            elif potion_info[1] == 'healing' and int(potion_info[2]) > 0 and healing_used == False:
                                                healed = floor(float(base_hp_player) * 0.25)
                                                player_mons_info[4] = int(player_mons_info[4]) + healed
                                                if player_mons_info[4] > base_hp_player:
                                                    player_mons_info[4] = base_hp_player
                                                potion_info[2] = int(potion_info[2])-1
                                                healing_used = True
                                                cond_potion_done = True
                                                print('Setelah meminum potion ini, monster anda merasa lebih sehat!')
                                        else:
                                            break
                                            
                                        
                                        if cond_potion_done == True:
                                            break
                                        if cond_potion_done == False and 0<potion_input<len(player_item_inv_arr)+1:
                                            print('Tidak dapat menggunakan potion yang sama lebih dari satu kali')
                                    
                                    else:
                                        print('Input tidak valid')
                                else:
                                    print('Input harus berupa integer.')
                            if cond_potion_done == True:
                                break
                                    
                        if player_input == 3:
                            return oc_player
                            
                else:
                    print('Input harus berupa integer')
            
            sleep(2)
            
            # If menang
            
            if int(enemy_info_arr[4]) <= 0:
                oc_reward = RNG(50, 100)
                print(f'Selamat, Anda berhasil mengalahkan monster {enemy_info_arr[1]} !!!')
                print(f'Total OC yang didapatkan {oc_reward}')
                return oc_reward+int(oc_player)
            
            #Bagian enemy attack
            
            enemy_attack = float(enemy_info_arr[2]) + (float(enemy_info_arr[2]) * 0.01 * RNG(-30, 30))
            pengali = (1 - (int(player_mons_info[3])*0.01))
            deal_damage = floor(enemy_attack * pengali)
            player_mons_info[4] = int(player_mons_info[4]) - deal_damage
            
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

