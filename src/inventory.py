def spasing(str, des):
    len_str = len(str)
    sisa = des - len_str
    space = ''
    
    for i in range (sisa):
        space += ' '
    
    return space

def is_int(str):
    cond = True
    for i in range(len(str)):
        cur_ord = ord(str[i])
        if cur_ord < 48 or cur_ord > 57:
            cond = False
    return cond

def inventory(player_id, monster_inventory_arr, item_inventory_arr, player_oc, monster_arr, player_role):
    
    if player_id == 'NaN':
        print('Anda belum login! ')
    
    else:
        print(f'============ INVENTORY LIST (User ID: {player_id}) ============')
        print(f'Jumlah O.W.C.A. Coin-mu sekarang {player_oc}.')
        
        nomor = 1
        item_cur_arr = [[-999], ]
        for i in range(len(monster_inventory_arr)):
            if monster_inventory_arr[i][0] == player_id:
                cur_monster_id = monster_inventory_arr[i][1]
                for j in range (len(monster_arr)):
                    if monster_arr[j][0] == cur_monster_id:
                        print(f'{nomor}. Monster        (Name: {monster_arr[j][1]}, Lvl: {monster_inventory_arr[i][2]}, HP: {monster_arr[j][4]})')
                        nomor += 1
                        item_cur_arr.append(['monster', monster_arr[j][1], monster_arr[j][2], monster_arr[j][3], monster_arr[j][4], monster_inventory_arr[i][2]])
                        
        for i in range(len(item_inventory_arr)):
            if item_inventory_arr[i][0] == player_id:
                if item_inventory_arr[i][1] != 'monster ball':
                    print(f'{nomor}. Potion         (Type: {item_inventory_arr[i][1]}, Qty: {item_inventory_arr[i][2]})')
                    item_cur_arr.append(['potion', item_inventory_arr[i][1], item_inventory_arr[i][2]])
                else:
                    print(f'{nomor}. Monster ball   (Qty: {item_inventory_arr[i][2]})')
                    item_cur_arr.append(['monster ball', item_inventory_arr[i][2]])
                nomor += 1
        
        validate_go = 'NaN'
        while True:
            while True:
                print('\n')
                validate_go = input('Apakah anda ingin lanjut lihat detail atau keluar? (lihat/keluar): ')
                if validate_go != 'lihat' and validate_go != 'keluar':
                    print('Input tidak valid!')
                else:
                    break
            
            if validate_go == 'lihat':
                player_input = 'NaN'
                while True:
                    print('\nKetik nomor item yang ingin dilihat')
                    player_input = input('>>> ')
                    if is_int(player_input) == True and int(player_input) < len(item_cur_arr):
                        player_input = int(player_input)
                        break
                    else:
                        print('Input tidak valid.')
                
                if item_cur_arr[player_input][0] == 'monster':
                    print(f'''
Monster
Name      : {item_cur_arr[player_input][1]}
ATK Power : {item_cur_arr[player_input][2]}
DEF Power : {item_cur_arr[player_input][3]}
HP        : {item_cur_arr[player_input][4]}
Level     : {item_cur_arr[player_input][5]}''')
                elif item_cur_arr[player_input][0] == 'potion':
                    print(f'''
Potion
Type     : {item_cur_arr[player_input][1]}
Quantity : {item_cur_arr[player_input][2]}''')
                else:
                    print(f'''
Monster ball
Quantity : {item_cur_arr[player_input][1]}''')
                    
            else:
                print('Anda akan dikembalikan ke halaman utama!')
                break
            