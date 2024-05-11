from random import randrange

#ini hypothetical, harus dihapus later
monster_arr = [[1,'python',20,20,110],[2,'java',30,20,90], [3,'jigglypuff',33,30,82]]
monster_inventory_arr = [['007',1,1], ['007',2,2], ['008',2,1]]
item_inventory_arr = [['007','strength',5], ['007','resilience',5], ['007','healing',5]]

def print_potion(item_inventory_arr, global_id):
    j=0
    for i in range (len(item_inventory_arr)):
        if item_inventory_arr[i][0] == global_id:
            j += 1
            print(f"{j}. {item_inventory_arr[i][1]} potion (Qty: {item_inventory_arr[i][2]})")
    

def battle(monster_arr, monster_inventory_arr, global_id, item_inventory_arr):
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
    enemy_info_arr = monster_arr[randrange(3)]
    enemy_level = randrange(1,3)
    print(f"""
RAWRRR, Monster {enemy_info_arr[1]} telah muncul !!!

Name      : {enemy_info_arr[1]}
ATK Power : {enemy_info_arr[2]}
DEF Power : {enemy_info_arr[3]}
HP        : {enemy_info_arr[4]}
Level     : {enemy_level}

============ MONSTER LIST ============ """)
    
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
    
    player_mons_info = monster_arr[select_number-1]

    # Penyesuaian level figthing monster
    if player_mons_lvl != 1:
        for i in range(2, 5):
            player_mons_info[i] = player_mons_info[i] + player_mons_info[i] * (player_mons_lvl-1) * 0.1

    if enemy_level != 1:
        for i in range(2, 5):
            enemy_info_arr[i] = enemy_info_arr[i] + enemy_info_arr[i] * (enemy_level-1) * 0.1
    
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

    turn = 1
    while True:
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
                    player_attack = player_mons_info[2] + (player_mons_info[2] * 0.01 * randrange(-30, 31))
                    enemy_info_arr[4] = enemy_info_arr[4] - (player_attack * (100 - enemy_info_arr[3])*0.01)
                    break
                
                elif player_input == 2:
                    print('\n============ POTION LIST ============')
                    print_potion(item_inventory_arr, global_id)
                    print('4. Cancel \n')
                    
                    potion_input = int(input('>>> Pilih potion yang ingin digunakan: '))
                    
                    if potion_input != 4:
                        potion_info = item_inventory_arr[potion_input-1]
                        
                        if potion_info[1] == 'strength':
                            player_mons_info[2] = player_mons_info[2] + (player_mons_info[2] * 0.05)
                        
                        elif potion_info[1] == 'resilience':
                            player_mons_info[3] = player_mons_info[3] + (player_mons_info[3] * 0.05)
                        
                        else:
                            player_mons_info[4] = player_mons_info[4] + (base_hp_player * 0.25)
                            if player_mons_info[4] > base_hp_player:
                                player_mons_info[4] = base_hp_player
                        break

                        
                else:
                    exit(0)
        
        print('here')
        break
    

battle(monster_arr, monster_inventory_arr, '007', item_inventory_arr)