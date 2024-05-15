# Fungsi untuk menampilkan item
def show_items(monster_arr, item_shop_arr, monster_shop_arr):

    product_type = input(">>> Mau lihat apa? (monster/potion): ")
    if product_type == "monster":
        print("ID | Type          | ATK Power | DEF Power | HP   | Stok | Harga")
        print("-----------------------------------------------------------------")
        for i in range (len(monster_shop_arr)):
            print(f"{monster_arr[i][0]:<3} | {monster_arr[i][1]:<15} | {monster_arr[i][2]:<9} | {monster_arr[i][3]:<9} | {monster_arr[i][4]:<5} | {monster_shop_arr[i][1]:<5} | {monster_shop_arr[i][2]:<5}")
    elif product_type == "potion":
        print("ID | Type                | Stok | Harga")
        print("---------------------------------------")
        for i in range (len(item_shop_arr)):
            print(f"{i+1:<3} | {item_shop_arr[i][0]:<20} | {item_shop_arr[i][1]:<5} | {item_shop_arr[i][2]:<5}")
    else:
        print("Item tidak valid, silahkan ulangi lagi.\n")

# Fungsi untuk membeli item
def buy_item(monster_inventory_arr, potion_inventory_arr, monster_shop_arr, item_shop_arr, monster_arr, global_oc):
    print(f"Jumlah O.W.C.A. Coin-mu sekarang {global_oc}.\n")
    product = input(">>> Mau beli apa? (monster/potion): ")
    global_oc = int(global_oc)

    if product == "monster":
        monster_product_id = int(input(">>> Masukkan id monster: "))

        for_var_in_row_monster = monster_product_id - 1 #untuk mengganti variabel id pada baris di matrix dikarenakan pada input nilai i ialah i+1 sehingga perlu dikuarangi
        monster_price = int(monster_shop_arr[for_var_in_row_monster][2])
        monster_stock = int(monster_shop_arr[for_var_in_row_monster][1])

        if monster_stock == 0:
            print("Stok tidak mencukupi.\n")
        
        else:
            if global_oc < monster_price:
                print("OC-mu tidak cukup.\n")

            elif global_oc >= monster_price:
                for i in range (len(monster_inventory_arr)):
                    if monster_inventory_arr[i][0] == monster_arr[for_var_in_row_monster][0]:
                        print("Monster sudah ada dalam inventory-mu!\n")
                        break

                else:
                    global_oc -= monster_price
                    monster_inventory_arr.append(monster_arr[for_var_in_row_monster])
                    monster_shop_arr[for_var_in_row_monster][1] = int(monster_shop_arr[for_var_in_row_monster][1]) - 1
                    print(f"Berhasil membeli monster {monster_arr[for_var_in_row_monster][1]}!\n")

    elif product == "potion":
        potion_product_id = int(input(">>> Masukkan id potion: "))
        potion_qty = int(input(">>> Masukkan jumlah: "))
        for_var_in_row_potion = potion_product_id -1 #untuk mengganti variabel id pada baris di matrix dikarenakan pada input nilai i ialah i+1 sehingga perlu dikuarangi

        potion_price = int(item_shop_arr[for_var_in_row_potion][2]) * potion_qty
        
        if potion_qty > int(item_shop_arr[for_var_in_row_potion][1]):
            print("Stok tidak mencukupi.\n")
        
        else:
            if global_oc < potion_price:
                print("OC-mu tidak cukup.\n")
            
            elif global_oc >= potion_price:
                global_oc -= potion_price
                potion_inventory_arr[for_var_in_row_potion][2] = int(potion_inventory_arr[for_var_in_row_potion][2]) + potion_qty
                item_shop_arr[for_var_in_row_potion][1] = int(item_shop_arr[for_var_in_row_potion][1]) - potion_qty
                print(f"Berhasil membeli {potion_qty} {item_shop_arr[for_var_in_row_potion][0]}!\n")

    else:
        print("Item tidak valid, silahkan ulangi lagi.\n")

# fungsi main shop
def shop(monster_inventory_arr, potion_inventory_arr, monster_shop_arr, item_shop_arr, monster_arr, global_oc):
    print("Irasshaimase! Selamat datang di SHOP!!\n")

    while True:

        action = input(">>> Pilih aksi (lihat/beli/keluar): ")

        if action == "lihat":
            show_items(monster_arr, item_shop_arr, monster_shop_arr)

        elif action == "beli":
            buy_item(monster_inventory_arr, potion_inventory_arr, monster_shop_arr, item_shop_arr, monster_arr, global_oc)

        elif action == "keluar":
            print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)\n")
            break

        else:
            print("Aksi tidak valid! Silakan coba lagi.\n")
            continue