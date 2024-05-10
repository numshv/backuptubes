login_state = 0
global_username = 'nope'
running_state = True


def yesorno(text):
    while True:
        agreement = input(text).lower()
        if agreement == 'y' or agreement == 'n':
            break
        else:
            print('Input tidak valid!')
    return agreement

def lab(monster_arr, monster_inventory_arr, global_oc, global_id):

    # HYPOTHETICAL
    up_price = [0, 200, 300, 600, 950]
    
    print("\nSelamat datang di lab! \n")
    
    while True:
        print("========= LIST MONSTER =========")

        monster_name = [0]
        monster_id = []
        monster_level = [0]


        for i in range (1, len(monster_inventory_arr)):
            if monster_inventory_arr[i][0] == global_id:
                for j in range (len(monster_arr)):
                    if monster_inventory_arr[i][1] == monster_arr[j][0]: 
                        cur_monster = monster_arr[j][1]
                        monster_name.append(monster_arr[j][1])
                        monster_id.append(monster_arr[j][0])
                print(f"{i}. {cur_monster} (Level: {monster_inventory_arr[i][2]})")
                monster_level.append(int(monster_inventory_arr[i][2]))

        print("\n\n========= HARGA UPSKILL =========")
        print("Level 1 -> Level 2: 200 OC\nLevel 2 -> Level 3: 300 OC\nLevel 3 -> Level 4: 600 OC\nLevel 4 -> Level 5: 950 OC")
        monster_up = -1
        while True:
            monster_up = int(input('\n>>> Pilih monster nomor: '))
            if monster_up <= len(monster_name):
                break
            else:
                print('Input tidak valid!')

        transaction_price = up_price[monster_level[monster_up]]
        transaction_level = monster_level[monster_up]

        print(f'\n{monster_name[monster_up]} akan di-upgrade ke level {transaction_level+1} !')
        print(f'Harga untuk melakukan upgrade pada {monster_name[monster_up]} adalah {transaction_price}')

        agreement = yesorno('\n>>> Lanjutkan upgrade (Y/N): ')

        if agreement == 'y' and global_oc >= transaction_price and transaction_level < 5:
            print(f'Selamat, {monster_name[monster_up]} berhasil di-upgrade ke level {monster_level[monster_up]+1} !')
            global_oc -= transaction_price
            for i in range (len(monster_inventory_arr)):
                if monster_inventory_arr[i][0] == global_id and monster_inventory_arr[i][1] == monster_id[monster_up-1]:
                    upped_lvl = int(monster_inventory_arr[i][2]) + 1
                    monster_inventory_arr[i][2] = upped_lvl
            cont = yesorno('>>> Masih mau lanjut belanja? (Y/N): ')
            if cont == 'n':
                return [global_oc, monster_inventory_arr]

        elif agreement == 'y' and global_oc>= transaction_price and transaction_level >= 5:
            print(f'Maaf, monster yang anda pilih telah mencapai level maximum.')
            cont = yesorno('>>> Masih mau lanjut belanja? (Y/N): ')
            if cont == 'n':
                break
        
        elif agreement == 'y' and transaction_level < 5 and global_oc < transaction_price:
            print(f'Maaf, OC anda tidak mencukupi transaksi ini ({global_oc}/{transaction_price})')
            cont = yesorno('>>> Masih mau lanjut belanja? (Y/N): ')
            if cont == 'n':
                break
        
        else:
            cont = yesorno('>>> Masih mau lanjut belanja? (Y/N): ')
            if cont == 'n':
                break