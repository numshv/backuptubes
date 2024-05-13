from math import floor
from time import sleep
from rng import RNG

def print_potion(item_inventory_arr, global_id):
    j=0
    for i in range (len(item_inventory_arr)):
        if item_inventory_arr[i][0] == global_id:
            j += 1
            print(f"{j}. {item_inventory_arr[i][1]} potion (Qty: {item_inventory_arr[i][2]})")

def battle(monster_arr:list, global_id:str, item_inventory_arr:list, player_mons_info_no:list, player_mons_lvl):
    oc_menang = [0,100,110,120,150,160]
    oc_reward = 0
    arena_level = 1
    while True:
        lose = False
        player_mons_info = player_mons_info_no.copy()
    
        print(f"============= STAGE {arena_level} ============= \n")
        
        
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


        turn = 1
        while True:
            damage_diberi = 0
            damage_diterima = 0
            
            while True: #Loop turn player
                print(f"""
    ============ TURN {turn} ({player_mons_info[1]}) ============
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
                        player_attack = player_mons_info[2] + (player_mons_info[2] * 0.01 * RNG(-30, 30))
                        damage_diberi_cur = player_attack * (100 - int(enemy_info_arr[3]))*0.01
                        damage_diberi += damage_diberi_cur
                        enemy_info_arr[4] = floor(int(enemy_info_arr[4]) - (damage_diberi_cur))
                        print(f'\nSCHWINKKK, {player_mons_info[1]} menyerang {enemy_info_arr[1]} !!!')
                        print(f'''
    Name        : {enemy_info_arr[1]}
    ATK Power   : {enemy_info_arr[2]}
    DEF Power   : {enemy_info_arr[3]}
    HP          : {enemy_info_arr[4]}
    Level       : {enemy_level}
                        ''')
                        
                        print(enemy_info_arr)
                        print(f'state: {monster_arr}')
                        
                        break
                    
                    elif player_input == 2:
                        print('\n============ POTION LIST ============')
                        print_potion(item_inventory_arr, global_id)
                        print('4. Cancel \n')
                        
                        potion_input = int(input('>>> Pilih potion yang ingin digunakan: '))
                        
                        if potion_input != 4:
                            potion_info = item_inventory_arr[potion_input-1]
                            
                            if potion_info[1] == 'strength' and potion_info[2] > 0:
                                player_mons_info[2] = player_mons_info[2] + (player_mons_info[2] * 0.05)
                                print('done')
                            
                            elif potion_info[1] == 'resilience' and potion_info[2] > 0:
                                player_mons_info[3] = player_mons_info[3] + (player_mons_info[3] * 0.05)
                                print('done')
                            
                            elif potion_info[1] == 'healing' and potion_info[2] > 0:
                                player_mons_info[4] = player_mons_info[4] + (base_hp_player * 0.25)
                                if player_mons_info[4] > base_hp_player:
                                    player_mons_info[4] = base_hp_player
                                print('done')
                            break
                            
                    else:
                        exit(0)
            
            sleep(2)
            
            # If menang
            
            
            if enemy_info_arr[4] <= 0 and arena_level < 5:
                oc_reward += oc_menang[arena_level]
                print(f'Selamat, Anda berhasil mengalahkan monster {enemy_info_arr[1]} !!!')
                print(f'Total OC yang didapatkan pada stage ini adalah {oc_menang[arena_level]}')
                arena_level += 1
                break
            
            elif enemy_info_arr[4] <= 0 and arena_level == 5:
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
            
            #Bagian enemy attack
            
            enemy_attack = int(enemy_info_arr[2]) + (int(enemy_info_arr[2]) * 0.01 * RNG(-30, 30))
            damage_diterima_cur = (enemy_attack * (100 - player_mons_info[3])*0.01)
            damage_diterima += damage_diterima_cur
            player_mons_info[4] = floor(int(player_mons_info[4]) - (damage_diterima_cur))
            
            print(f"""
    ============ TURN {turn} ({enemy_info_arr[1]}) ============

    SCHWINKKK, {enemy_info_arr[1]} menyerang {player_mons_info[1]} !!!

    Name        : {player_mons_info[1]}
    ATK Power   : {player_mons_info[2]}
    DEF Power   : {player_mons_info[3]}
    HP          : {player_mons_info[4]}
    Level       : {player_mons_lvl}
                    """)
            
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
                break
                
                
            
            # If lanjut
            
            turn += 1
        
        if lose == True:
            break

def arena(monster_inventory_arr, global_id, monster_arr, item_inventory_arr):
    
    print("============ MONSTER LIST ============ ")
    
    monster_name = []
    monster_id = [0]
    monster_level = [0]

    for i in range (len(monster_inventory_arr)):
        if monster_inventory_arr[i][0] == global_id:
            for j in range (len(monster_arr)):
                if monster_inventory_arr[i][1] == monster_arr[j][0]: 
                    cur_monster = monster_arr[j][1]
                    monster_name.append(monster_arr[j][1])
                    monster_id.append(monster_arr[j][0])
            print(f"{i+1}. {cur_monster} (Level: {monster_inventory_arr[i][2]})")
            monster_level.append(int(monster_inventory_arr[i][2]))
    

    player_mons_lvl = 0
    select_number = -999
    
    while True:
        select_number = int(input('\n>>> Pilih monster nomor: '))
        if select_number <= len(monster_name):
            player_mons_lvl = monster_level[select_number]
            break
        else:
            print('Input tidak valid!')
    
    player_mons_info_no = monster_arr[select_number-1]
    
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

    battle(monster_arr, global_id, item_inventory_arr, player_mons_info_no, player_mons_lvl)

monster_inventory_arr = [['007',1,1], ['007',2,2], ['008',2,1]]
player_id = '007'
monster_arr = [[1,'python',20,20,110], [2,'java',30,20,90], [3,'jigglypuff',33,30,82]]
item_inventory_arr = [['007','strength',2], ['007','healing',2], ['007','resilience',1]]


arena(monster_inventory_arr, player_id, monster_arr, item_inventory_arr)
