from math import floor
from time import sleep
from src.rng import RNG
from os import system

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

def is_int(str):
    cond = True
    for i in range(len(str)):
        cur_ord = ord(str[i])
        if cur_ord < 48 or cur_ord > 57:
            cond = False
    return cond

def print_potion(item_inventory_arr, player_id, player_item_inv_arr:list):
    j=0
    for i in range (len(item_inventory_arr)):
        if item_inventory_arr[i][0] == player_id:
            j += 1
            print(f"{j}. {item_inventory_arr[i][1]} potion (Qty: {item_inventory_arr[i][2]})")
            player_item_inv_arr.append(item_inventory_arr[i])

def battle(monster_arr:list, global_id:str, item_inventory_arr:list, player_mons_info_no:list, player_mons_lvl):
    oc_menang = [0,100,110,120,150,160]
    oc_reward = 0
    arena_level = 1
    while True:
        lose = False
        player_mons_info = player_mons_info_no.copy()
    
        print(f"============= STAGE {arena_level} ============= \n")
        
        sleep(1.5)
        
        print(mons_pict[RNG(0,4)])
        #rand range blm di ubah ke yg buatan sendiri
        enemy_info_arr_no = monster_arr[RNG(0,len(monster_arr))]
        enemy_level = arena_level
        
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

        sleep(2)
        turn = 1
        strength_used = False
        resilience_used = False
        healing_used = False
        damage_diberi = 0
        damage_diterima = 0
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
                            damage_diberi = int(deal_damage) + damage_diberi
                            print(damage_diberi)
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
                                    print(len(player_item_inv_arr))
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
                            print(f'Yahh, anda dikalahkan monster {enemy_info_arr[1]} !!!')
                            print(f'\nGAME OVER! Sesi latihan berakhir pada stage {arena_level}')
                            
                            # Print stats
                            
                            print('============== STATS ==============')
                            print(f'Total hadiah      : {oc_reward} OC')
                            print(f'Jumlah stage      : {arena_level}')
                            print(f'Damage diberikan  : {damage_diberi}')
                            print(f'Damage diterima   : {damage_diterima}')
                            lose = True
                            sleep(2.5)
                            return oc_reward
                            
                else:
                    print('Input harus berupa integer')
            
            sleep(2)
            
            # If menang
            
            if int(enemy_info_arr[4]) <= 0 and arena_level < 5:
                sleep(2)
                oc_reward += oc_menang[arena_level]
                print(f'Selamat, Anda berhasil mengalahkan monster {enemy_info_arr[1]} !!!')
                print(f'Total OC yang didapatkan pada stage ini adalah {oc_menang[arena_level]}')
                arena_level += 1
                break
            
            elif int(enemy_info_arr[4]) <= 0 and arena_level == 5:
                sleep(2)
                oc_reward += oc_menang[arena_level]
                print(f'Selamat, Anda berhasil mengalahkan monster {enemy_info_arr[1]} !!!')
                print(f'Total OC yang didapatkan pada stage ini adalah {oc_menang[arena_level]}')
                print('\nSelamat, Anda berhasil menyelesaikan seluruh stage Arena !!!')
                
                # Print stats
                
                print('============== STATS ==============')
                print(f'Total hadiah      : {oc_reward} OC')
                print(f'Jumlah stage      : 5')
                print(f'Damage diberikan  : {damage_diberi}')
                print(f'Damage diterima   : {damage_diterima}')
                
                return oc_reward
            
            #Bagian enemy attack
            
            enemy_attack = float(enemy_info_arr[2]) + (float(enemy_info_arr[2]) * 0.01 * RNG(-30, 30))
            pengali = (1 - (int(player_mons_info[3])*0.01))
            deal_damage = floor(enemy_attack * pengali)
            damage_diterima = int(deal_damage) + damage_diterima
            print(damage_diterima)
            player_mons_info[4] = int(player_mons_info[4]) - deal_damage
            
            sleep(2)
            print(f"""
============ TURN {turn} ({enemy_info_arr[1]}) | ENEMY ============

SCHWINKKK, {enemy_info_arr[1]} menyerang {player_mons_info[1]} !!!

Name        : {player_mons_info[1]}
ATK Power   : {player_mons_info[2]}
DEF Power   : {player_mons_info[3]}
HP          : {player_mons_info[4]}
Level       : {player_mons_lvl}
                    """)
            
            sleep(2)
            # If kalah
            
            if player_mons_info[4] <= 0:
                print(f'Yahh, anda dikalahkan monster {enemy_info_arr[1]} !!!')
                print(f'\nGAME OVER! Sesi latihan berakhir pada stage {arena_level}')
                
                # Print stats
                
                print('============== STATS ==============')
                print(f'Total hadiah      : {oc_reward} OC')
                print(f'Jumlah stage      : {arena_level}')
                print(f'Damage diberikan  : {damage_diberi}')
                print(f'Damage diterima   : {damage_diterima}')
                lose = True
                sleep(2.5)
                return oc_reward
                
                
            
            # If lanjut
            
            turn += 1
        
        if lose == True:
            print("""
  ________                              ________                        ._. 
 /  _____/ _____     _____    ____      \_____  \ ___  __  ____ _______ | | 
/   \  ___ \__  \   /     \ _/ __ \      /   |   \\  \/ /_/ __ \\_  __ \| | 
\    \_\  \ / __ \_|  Y Y  \\  ___/     /    |    \\   / \  ___/ |  | \/ \| 
 \______  /(____  /|__|_|  / \___  >    \_______  / \_/   \___  >|__|    __ 
        \/      \/       \/      \/             \/            \/         \/                                                       
                  """)
            break

def arena(monster_inventory_arr, global_id, monster_arr, item_inventory_arr, player_role):
    if global_id == 'NaN':
        print('Anda belum login!, silahkan ketik perintah LOGIN untuk login ke akun anda\n')
    
    elif player_role == 'admin':
        print('Admin tidak dapat mengakses fitur ini.')
    
    else:
        
        system("cls")
        
        sleep(1)
        print("""
   _____                                      __________                      ._. 
  /  _  \ _______   ____    ____  _____       \____    / ____    ____    ____ | | 
 /  /_\  \\_  __ \_/ __ \  /    \ \__  \        /     / /  _ \  /    \ _/ __ \| | 
/    |    \|  | \/\  ___/ |   |  \ / __ \_     /     /_(  <_> )|   |  \\  ___/ \| 
\____|__  /|__|    \___  >|___|  /(____  /    /_______ \\____/ |___|  / \___  >__ 
        \/             \/      \/      \/             \/            \/      \/ \/ 
                                                                                  
""")
        
        sleep(1.5)
        
        print("============ MONSTER LIST ============ ")
        
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

        sleep(2)
        oc_reward = battle(monster_arr, global_id, item_inventory_arr, player_mons_info_no, player_mons_lvl)
        return oc_reward

#monster_inventory_arr = [['007',1,1], ['007',2,2], ['008',2,1]]
#player_id = '007'
#monster_arr = [[1,'python',20,20,110], [2,'java',30,20,90], [3,'jigglypuff',33,30,82]]
#item_inventory_arr = [['007','strength',2], ['007','healing',2], ['007','resilience',1]]


#arena(monster_inventory_arr, player_id, monster_arr, item_inventory_arr)
