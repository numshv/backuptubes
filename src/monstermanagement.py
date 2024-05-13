monster_arr = [[1,'python',20,20,110], [2,'java',30,20,90], [3,'jigglypuff',33,30,82]]

def spasing(str, des):
    len_str = len(str)
    sisa = des - len_str
    space = ''
    
    for i in range (sisa):
        space += ' '
    
    return space

def monster_management(monster_arr:list):
    print('Selamat datang di database para monster')
    print('1. Lihat database monster')
    print('2. Edit database monster')
    print('3. Untuk melihat navigasi command ini kembali')
    print('4. Keluar \n')
    
    while True:
    
        player_input = int(input('>>> '))
        
        if player_input == 1:
            print('ID |    TYPE    | ATK POWER | DEF POWER |  HP  ')
            for i in range (len(monster_arr)):
                print(f' {monster_arr[i][0]} | {monster_arr[i][1] + spasing(monster_arr[i][1], 10)} | {monster_arr[i][2]}        | {monster_arr[i][3]}        | {monster_arr[i][4]}')
            print('\n')
            
        elif player_input == 2:
            
            new_type = ''
            new_atk = 0
            new_def = 0
            new_hp = 0
            
            print('Mulai pembuatan moster baru! \n')
            
            while True:
                input_type = input('Masukkan type/nama dari monster anda: ')
                
                cond = True
                for i in range (len(monster_arr)):
                    if monster_arr[i][1] == input_type:
                        cond = False
                
                if cond == True:
                    new_type = input_type
                    print('\n')
                    break
                
                else:
                    print('Type/nama sudah ada! \n')
            
            while True:
                try:
                    input_atk = int(input('Masukkan power ATK monster baru: '))
                    if 0 < input_atk <=50:
                        new_atk = input_atk
                        break
                    else:
                        print('DEF harus dalam range nilai 0 sampai 50')
                except ValueError:
                    print('Input harus berupa integer')
                
            while True:
                try:
                    input_def = int(input('Masukkan power DEF monster baru: '))
                    if 0 < input_def <=50:
                        new_def = input_def
                        break
                    else:
                        print('DEF harus dalam range nilai 0 sampai 50')
    
                except ValueError:
                    print('Input harus berupa integer\n')
            
            while True:
                try:
                    input_hp = int(input('Masukkan HP monster baru: '))
                    if 0 < input_hp <=150:
                        new_hp = input_hp
                        break
                    else:
                        print('HP harus dalam range nilai 0 sampai 150')
                except ValueError:
                    print('Input harus berupa integer')
            
            print('\nMonster baru berhasil dibuat!')
            print(f'TYPE    : {new_type}')
            print(f'ATK     : {new_atk}')
            print(f'DEF     : {new_def}')
            print(f'HP      : {new_hp}')
            
            while True:
                yesorno = input('Tambahkan monster ke database? (Y/N): ').lower()
                if yesorno != 'y' and yesorno != 'n':
                    print('Input tidak valid')
                else:
                    break
            
            if yesorno == 'y':
                monster_arr.append([len(monster_arr)+1, new_type, new_atk, new_def, new_hp])
                print('Monster berhasil dimasukkan!')
            
            else:
                print('Monster gagal dimasukkan.')
        
        elif player_input == 4:
            break
        
        elif player_input ==3:
            print('\nSelamat datang di database para monster')
            print('1. Lihat database monster')
            print('2. Edit database monster')
            print('3. Untuk melihat navigasi command ini kembali')
            print('4. Keluar \n')
        
        else:
            print('Input tidak valid, ketik 3 untuk melihat kembali navigasi command')
            



monster_management(monster_arr)