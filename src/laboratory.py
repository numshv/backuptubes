
def yesorno(text):
    while True:
        agreement = input(text).lower()
        if agreement == 'y' or agreement == 'n':
            break
        else:
            print('Input tidak valid!')
    return agreement

def is_int(str):
    cond = True
    for i in range(len(str)):
        cur_ord = ord(str[i])
        if cur_ord < 48 or cur_ord > 57:
            cond = False
    return cond

def lab(monster_arr, monster_inventory_arr, player_oc, global_id):
    if global_id == 'NaN':
        print('Anda belum login!, silahkan ketik perintah LOGIN untuk login ke akun anda\n')

    else:
        global_oc = int(player_oc)
        # HYPOTHETICAL
        up_price = [0, 200, 300, 600, 950]
        
        print("\nSelamat datang di lab! \n")
        
        while True:
            print("========= LIST MONSTER =========")

            monster_name = [0]
            monster_id = []
            monster_level = [0]

            actual_i = 1
            for i in range (len(monster_inventory_arr)):
                if monster_inventory_arr[i][0] == global_id:
                    for j in range (len(monster_arr)):
                        if monster_inventory_arr[i][1] == monster_arr[j][0]: 
                            cur_monster = monster_arr[j][1]
                            monster_name.append(monster_arr[j][1])
                            monster_id.append(monster_arr[j][0])
                    print(f"{actual_i}. {cur_monster} (Level: {monster_inventory_arr[i][2]})")
                    actual_i += 1
                    monster_level.append(int(monster_inventory_arr[i][2]))

            print("\n\n========= HARGA UPSKILL =========")
            print("Level 1 -> Level 2: 200 OC\nLevel 2 -> Level 3: 300 OC\nLevel 3 -> Level 4: 600 OC\nLevel 4 -> Level 5: 950 OC")
            monster_up = -1
            while True:
                
                monster_up_no = input('\n>>> Pilih monster nomor: ')
                
                if is_int(monster_up_no) == False:
                    print('Input harus berupa integer')
                
                
                else:
                    monster_up = int(monster_up_no)
                    if 0 < monster_up <= len(monster_name):
                        break
                    else:
                        print('Input tidak valid!')

            transaction_price = up_price[monster_level[monster_up]]
            transaction_level = monster_level[monster_up]

            print(f'\n{monster_name[monster_up]} akan di-upgrade ke level {transaction_level+1} !')
            print(f'Harga untuk melakukan upgrade pada {monster_name[monster_up]} adalah {transaction_price}')

            agreement = yesorno('\n>>> Lanjutkan upgrade (Y/N): ')

            if agreement == 'y' and global_oc >= int(transaction_price) and transaction_level < 5:
                print(f'Selamat, {monster_name[monster_up]} berhasil di-upgrade ke level {monster_level[monster_up]+1} !\n')
                global_oc -= transaction_price
                for i in range (len(monster_inventory_arr)):
                    if monster_inventory_arr[i][0] == global_id and monster_inventory_arr[i][1] == monster_id[monster_up-1]:
                        upped_lvl = int(monster_inventory_arr[i][2]) + 1
                        monster_inventory_arr[i][2] = upped_lvl
                cont = yesorno('>>> Masih mau lanjut belanja? (Y/N): ')
                if cont == 'n':
                    print('\nSampai bertemu lagi! Sering sering belanja disini ya!')
                    return [global_oc, monster_inventory_arr]

            elif agreement == 'y' and global_oc>= transaction_price and transaction_level >= 5:
                print(f'Maaf, monster yang anda pilih telah mencapai level maximum.\n')
                cont = yesorno('>>> Masih mau lanjut belanja? (Y/N): ')
                if cont == 'n':
                    print('\nSampai bertemu lagi! Sering sering belanja disini ya!')
                    return [global_oc, monster_inventory_arr]
            
            elif agreement == 'y' and transaction_level < 5 and global_oc < transaction_price:
                print(f'Maaf, OC anda tidak mencukupi transaksi ini ({global_oc}/{transaction_price})\n')
                cont = yesorno('>>> Masih mau lanjut belanja? (Y/N): ')
                if cont == 'n':
                    print('\nSampai bertemu lagi! Sering sering belanja disini ya!')
                    return [global_oc, monster_inventory_arr]
            
            else:
                cont = yesorno('>>> Masih mau lanjut belanja? (Y/N): ')
                if cont == 'n':
                    print('\nSampai bertemu lagi! Sering sering belanja disini ya!\n')
                    return [global_oc, monster_inventory_arr]