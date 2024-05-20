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

def shop_management(login_state, player_role, monster_shop_arr:list, item_shop_arr:list, monster_arr:list):
    print('Selamat datang di shop management!')
    item_arr = ['NaN', 'strength', 'resilience', 'healing', 'monster ball']
    
    while True:
        print('\n')
        player_input = input('>>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ')
        if player_input == 'lihat':
            while True:
                player_input_lihat = input('>>> Mau lihat apa? (monster/item): ')
                if player_input_lihat == 'monster':
                    print('\n ID |     TYPE     | ATK POWER | DEF POWER |  HP  | STOK | HARGA ')
                    for i in range(len(monster_shop_arr)):
                        monster_id = int(monster_shop_arr[i][0])
                        print(f' {monster_id}  | {monster_arr[monster_id-1][1] + spasing(monster_arr[monster_id-1][1], 12)} | {monster_arr[monster_id-1][2] + spasing(monster_arr[monster_id-1][2], 9)} | {monster_arr[monster_id-1][3]+ spasing(monster_arr[monster_id-1][3], 9)} | {str(monster_arr[monster_id-1][4]) + spasing(str(monster_arr[monster_id-1][4]), 3)}  | {str(monster_shop_arr[i][1]) + spasing(str(monster_shop_arr[i][1]), 4)} | {monster_shop_arr[i][2]}')
                    break
                
                if player_input_lihat == 'item':
                    print('\n ID |    TYPE    | STOK | HARGA ')
                    for i in range(len(item_shop_arr)):
                        print(f' {item_shop_arr[i][0]}  | {item_shop_arr[i][1] + spasing(item_shop_arr[i][1], 10)} | {str(item_shop_arr[i][2]) + spasing(str(item_shop_arr[i][2]), 4)} | {str(item_shop_arr[i][3]) + spasing(str(item_shop_arr[i][3]), 5)}')
                    break
                
                else:
                    print('Input tidak valid!\n')
                    
        elif player_input == 'tambah':
            while True:
                cond_done = False
                player_input_tambah = input('>>> Mau tambah apa? (monster/item): ')
                if player_input_tambah == 'monster':
                    if len(monster_arr) == len(monster_shop_arr):
                        print('Semua type monster sedang dijual di shop, tidak ada yang bisa ditambah.')
                        break
                    
                    else:
                        okay_id_arr = []
                        
                        # Bagian print
                        print('\n ID |    TYPE    | ATK POWER | DEF POWER | HP  ')
                        for i in range(len(monster_arr)): 
                            cond_okay = True
                            for j in range(len(monster_shop_arr)):
                                if monster_arr[i][0] == monster_shop_arr[j][0]:
                                    cond_okay = False
                            if cond_okay == True:
                                okay_id_arr.append(monster_arr[i][0])
                                print(f' {monster_arr[i][0]}  | {monster_arr[i][1] + spasing(monster_arr[i][1], 10)} | {monster_arr[i][2]}        | {monster_arr[i][3]}        | {monster_arr[i][4]} ')
                        print('\n')  
                        
                        while True:
                        
                            id_input = input('>>> Masukkan id monster: ')
                            stok_input = input('>>> Masukkan stok awal: ') 
                            harga_input = input('>>> Masukkan harga: ')

                            if is_int(id_input) == False or is_int(stok_input) == False or is_int(harga_input) == False:
                                print('Input harus berupa integer')
                            
                            else:
                                cond1 = False
                                print(okay_id_arr)
                                for i in range(len(okay_id_arr)):
                                    if id_input == okay_id_arr[i]:
                                            cond1 = True
                                if cond1 == False:
                                    print('ID tidak valid!\n')
                                cond2 = True
                                if int(stok_input)>=100 or int(stok_input)<0:
                                    cond2 = False
                                
                                if cond2 == False:
                                    print('Stok harus di atas 0 dan di bawah 100\n')
                                
                                cond3 = True
                                if int(harga_input)>=500 or int(harga_input)<0:
                                    cond3 = False
                                if cond3 == False:
                                    print('Harga harus lebih besar dari 0 dan lebih kecil dari 500\n')
                                
                                if cond1 == True and cond2 == True and cond3 == True:
                                    monster_shop_arr.append([id_input,stok_input,harga_input])
                                    cond_done = True
                                    print(f'monster {monster_arr[int(id_input)-1][1]} berhasil ditambahkan ke shop!')
                                    break
                            
                elif player_input_tambah == 'item':
                    if len(item_shop_arr) == 4:
                        print('Semua item/potion sedang dijual di shop, tidak ada yang bisa ditambahkan.\n')
                        break
                    
                    else:
                        okay_id_arr = []
                        # Bagian print
                        print('\n ID |    TYPE    ')
                        for i in range(1, 5): 
                            cond_okay = True
                            for j in range(len(item_shop_arr)):
                                if i == int(item_shop_arr[j][0]):
                                    cond_okay = False
                            if cond_okay == True:
                                okay_id_arr.append(i)
                                print(f' {i}  | {item_arr[i]} ')
                        print('\n')  
                        
                        while True:
                            try:
                                id_input = int(input('>>> Masukkan id potion: '))    
                                stok_input = int(input('>>> Masukkan stok awal: '))      
                                harga_input = int(input('>>> Masukkan harga: '))
                                    
                                
                            except:
                                print('Input harus sebuah angka (integer)!\n')
                            
                            cond1 = False
                            for i in range(len(okay_id_arr)):
                                if id_input == okay_id_arr[i]:
                                        cond1 = True
                            if cond1 == False:
                                print('ID tidak valid!\n')
                            cond2 = True
                            if stok_input>=100 or stok_input<0:
                                cond2 = False
                            
                            if cond2 == False:
                                print('Stok harus di atas 0 dan di bawah 100\n')
                            
                            cond3 = True
                            if harga_input>=500 or harga_input<0:
                                cond3 = False
                            if cond3 == False:
                                print('Harga harus lebih besar dari 0 dan lebih kecil dari 500\n')
                            
                            if cond1 == True and cond2 == True and cond3 == True:
                                item_shop_arr.append([id_input, item_arr[id_input] ,stok_input,harga_input])
                                cond_done = True
                                break
                
                if cond_done == True:
                    break
                else:
                    print('Input tidak valid!')
                            
        
        elif player_input == 'ubah':
            while True:
                player_input_ubah = input('>>> Mau ubah apa? (monster/item): ')
                okay_id_arr = []
                if player_input_ubah == 'monster':
                    print('\n ID |     TYPE     | ATK POWER | DEF POWER |  HP  | STOK | HARGA ')
                    for i in range(len(monster_shop_arr)):
                        monster_id_str = monster_shop_arr[i][0]
                        okay_id_arr.append(monster_id_str)
                        monster_id = int(monster_id_str)
                        print(f' {monster_id}  | {monster_arr[monster_id-1][1] + spasing(monster_arr[monster_id-1][1], 12)} | {monster_arr[monster_id-1][2]}        | {monster_arr[monster_id-1][3]}        | {str(monster_arr[monster_id-1][4]) + spasing(str(monster_arr[monster_id-1][4]), 3)}  | {str(monster_shop_arr[i][1]) + spasing(str(monster_shop_arr[i][1]), 4)} | {monster_shop_arr[i][2]}')
                        okay_id_arr.append(monster_id)
                    print('\n')
                    while True:
                        
                        id_input = input('>>> Masukkan id monster: ')   
                        stok_input = input('>>> Masukkan stok awal: ')      
                        harga_input = input('>>> Masukkan harga: ')
 
                        if is_int(id_input) == False or is_int(stok_input) == False or is_int(harga_input) == False:
                            print('Input harus berupa integer')
                        
                        else:
                            
                            cond1 = False
                            for i in range(len(okay_id_arr)):
                                if id_input == okay_id_arr[i]:
                                        cond1 = True
                            if cond1 == False:
                                print('ID tidak valid!\n')
                            cond2 = True
                            if int(stok_input)>=100 or int(stok_input)<0:
                                cond2 = False
                            
                            if cond2 == False:
                                print('Stok harus di atas 0 dan di bawah 100\n')
                            
                            cond3 = True
                            if int(harga_input)>=500 or int(harga_input)<0:
                                cond3 = False
                            if cond3 == False:
                                print('Harga harus lebih besar dari 0 dan lebih kecil dari 500\n')
                            
                            if cond1 == True and cond2 == True and cond3 == True:
                                for i in range (len(monster_shop_arr)):
                                    if monster_shop_arr[i][0] == str(id_input):
                                        monster_shop_arr[i][1] = stok_input
                                        monster_shop_arr[i][2] = harga_input
                                cond_done = True
                                print(f'Data shop monster {monster_arr[int(id_input)-1][1]} berhasil diubah!')
                                break
                
                if player_input_ubah == 'item':
                    print('\n ID |    TYPE    | STOK | HARGA ')
                    for i in range(len(item_shop_arr)):
                        okay_id_arr.append(item_shop_arr[i][0])
                        print(f' {item_shop_arr[i][0]}  | {item_shop_arr[i][1] + spasing(item_shop_arr[i][1], 10)} | {str(item_shop_arr[i][2]) + spasing(str(item_shop_arr[i][2]), 4)} | {str(item_shop_arr[i][3]) + spasing(str(item_shop_arr[i][3]), 5)}')
                    print('\n')
                    while True:

                        id_input = input('>>> Masukkan id item: ')  
                        stok_input = input('>>> Masukkan stok awal: ')   
                        harga_input = input('>>> Masukkan harga: ')
                                
                        if is_int(id_input) == False or is_int(stok_input) == False or is_int(harga_input) == False:
                            print('Input harus berupa integer')
                        
                        
                        cond1 = False
                        for i in range(len(okay_id_arr)):
                            if id_input == okay_id_arr[i]:
                                cond1 = True
                        if cond1 == False:
                            print('ID tidak valid!\n')
                        cond2 = True
                        if int(stok_input)>=100 or int(stok_input)<0:
                            cond2 = False
                        
                        if cond2 == False:
                            print('Stok harus di atas 0 dan di bawah 100\n')
                        
                        cond3 = True
                        if int(harga_input)>=500 or int(harga_input)<0:
                            cond3 = False
                        if cond3 == False:
                            print('Harga harus lebih besar dari 0 dan lebih kecil dari 500\n')
                        
                        if cond1 == True and cond2 == True and cond3 == True:
                            for i in range (len(item_shop_arr)):
                                if item_shop_arr[i][0] == id_input:
                                    item_shop_arr[i][2] = stok_input
                                    item_shop_arr[i][3] = harga_input
                            cond_done = True
                            break
                
                if cond_done == True:
                    break
                else:
                    print('Input tidak valid!\n')
        
        elif player_input == 'hapus':
            cond_done = False
            while True:
                okay_id_arr = []
                player_input_hapus = input('>>> Mau hapus apa? (monster/item): ')
                if player_input_hapus == 'monster':
                    print('\n ID |     TYPE     | ATK POWER | DEF POWER |  HP  | STOK | HARGA ')
                    for i in range(len(monster_shop_arr)):
                        monster_id = monster_shop_arr[i][0] 
                        okay_id_arr.append(monster_id)
                        print(f' {monster_id}  | {monster_arr[int(monster_id)-1][1] + spasing(monster_arr[int(monster_id)-1][1], 12)} | {monster_arr[int(monster_id)-1][2] + spasing(monster_arr[int(monster_id)-1][2], 9)} | {monster_arr[int(monster_id)-1][3] + spasing(monster_arr[int(monster_id)-1][3], 9)} | {str(monster_arr[int(monster_id)-1][4]) + spasing(str(monster_arr[int(monster_id)-1][4]), 3)}  | {str(monster_shop_arr[i][1]) + spasing(str(monster_shop_arr[i][1]), 4)} | {monster_shop_arr[i][2]}')
                    print('\n')
                    while True:
                        
                        id_input = input('>>> Masukkan id monster: ')  
 
                        if is_int(id_input) == False:
                            print('Input harus sebuah angka (integer)!\n')
                        
                        else:
                            cond1 = False
                            for i in range(len(okay_id_arr)):
                                if id_input == okay_id_arr[i]:
                                    cond1 = True
                            if cond1 == False:
                                print('ID tidak valid!\n')
                            
                            if cond1 == True:
                                validate = input(f'Apakah anda yakin ingin menghapus {monster_arr[int(id_input)-1][1]} dari shop? (y/n): ')
                                
                                while True:
                                    if validate == 'y':
                                        for i in range (len(monster_shop_arr)):
                                            if monster_shop_arr[i][0] == id_input:
                                                monster_shop_arr.pop(i)
                                                break
                                        print('Berhasil dihapus.')
                                        cond_done = True
                                        break
                                    elif validate == 'n':
                                        print('Batal dihapus.')
                                        cond_done = True
                                        break
                                    else:
                                        print('Input tidak valid!')
                            break
                if cond_done == True:
                    break
                else:
                    print('Input tidak valid!\n')
                
                if player_input_hapus == 'item':
                    print('\n ID |    TYPE    | STOK | HARGA ')
                    for i in range(len(item_shop_arr)):
                        okay_id_arr.append(item_shop_arr[i][0])
                        print(f' {item_shop_arr[i][0]}  | {item_shop_arr[i][1] + spasing(item_shop_arr[i][1], 10)} | {str(item_shop_arr[i][2]) + spasing(str(item_shop_arr[i][2]), 4)} | {str(item_shop_arr[i][3]) + spasing(str(item_shop_arr[i][3]), 5)}')
                    print('\n')
                    
                    while True:
                        id_input = input('>>> Masukkan id item: ') 
 
                        if is_int(id_input) == False:
                            print('Input harus sebuah angka (integer)!\n')
                        
                        else:
                            cond1 = False
                            for i in range(len(okay_id_arr)):
                                if id_input == okay_id_arr[i]:
                                    cond1 = True
                            if cond1 == False:
                                print('ID tidak valid!\n')
                            
                            if cond1 == True:
                                validate = input(f'Apakah anda yakin ingin menghapus {item_arr[int(id_input)]} dari shop? (y/n): ')
                                
                                while True:
                                    if validate == 'y':
                                        for i in range(len(item_shop_arr)):
                                            if item_shop_arr[i][0] == id_input:
                                                item_shop_arr.pop(i)
                                                break
                                        print('Berhasil dihapus.')
                                        cond_done = True
                                        break
                                    elif validate == 'n':
                                        print('Batal dihapus.')
                                        cond_done = True
                                        break
                                    else:
                                        print('Input tidak valid!')
                            break
                
                if cond_done == True:
                    break
                else:
                    print('Input tidak valid!\n')
        
        elif player_input == 'keluar':
            print('Sampai jumpa kembali di shop management!')
            break
        
        else:
            print('Input tidak valid!')
            
#monster_arr = [[1,'python',20,20,110], [2,'java',30,20,90], [3,'jigglypuff',33,30,82]]
#login_state = 1 
#player_role = 'admin'
#monster_shop_arr = [[1,10,100], [3,10,800]]
#item_shop_arr = [[1, 'strength', 10, 100], [2, 'resilience', 10, 100], [3, 'healing', 10, 100]]

#shop_management(login_state, player_role, monster_shop_arr, item_shop_arr, monster_arr)
    