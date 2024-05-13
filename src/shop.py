# Fungsi untuk menampilkan item
def show_items(monster_arr, item_shop_arr, monster_shop_arr ):

    product_type = input(">>> Mau lihat apa? (monster/potion): ")
    if product_type == "monster":
        print("ID | Type          | ATK Power | DEF Power | HP   | Stok | Harga")
        for i in range (len(monster_arr)):
            print (f"{monster_arr[i][0]}  | {monster_arr[i][1]} | {monster_arr[i][2]} | {monster_arr[i][3]} | {monster_arr[i][4]} | {monster_shop_arr[i][1]} | {monster_shop_arr[i][2]}")
    elif product_type == "potion":
        print("ID | Type                | Stok | Harga")
        for i in range (len(item_shop_arr)):
            print(f"{i+1}  | {item_shop_arr[i][0]} | {item_shop_arr[i][1]} | {item_shop_arr[i][2]}")
    else:
        print("Tipe item tidak valid.")

# Fungsi untuk membeli item
def buy_item(monster_inventory_arr, potion_inventory_arr, monster_shop_arr, item_shop_arr, monster_arr):
    print(f"Jumlah O.W.C.A. Coin-mu sekarang {global_oc}.\n")
    product = input(">>> Mau beli apa? (monster/potion): monster")

    if product == "monster":
        monster_product_id = input(">>> Masukkan id monster: ")
        monster_price = monster_arr[monster_product_id][4]
        monster_stock = monster_shop_arr[monster_product_id][1]

        if monster_stock == 0:
            print("Stok tidak mencukupi.")
        
        else:
            if global_oc < monster_price:
                print("OC-mu tidak cukup.")

            elif global_oc >= monster_price:
                for i in range (len(monster_inventory_arr)):
                    if monster_inventory_arr[i][0] == monster_arr[monster_product_id][0]:
                        print("Monster sudah ada dalam inventory-mu!")
                        break
                    else:
                        global_oc -= monster_price
                        monster_inventory_arr.append(monster_arr[monster_product_id])
                        monster_shop_arr[monster_product_id][1] -= 1
                        print(f"Berhasil membeli monster {monster_arr[monster_product_id][1]}!")

    if product == "potion":
        potion_product_id = input(">>> Masukkan id potion: ")
        potion_qty = input(">>> Masukkan jumlah: ")
        potion_price = item_shop_arr[potion_product_id][2] * potion_qty

        if potion_qty > item_shop_arr[potion_product_id][1]:
            print("Stok tidak mencukupi.")
        else:
            if global_oc < potion_price:
                print("OC-mu tidak cukup.")
            elif global_oc >= potion_price:
                global_oc -= potion_price
                potion_inventory_arr[potion_product_id][2] += potion_qty
                print(f"Berhasil membeli {potion_qty} {item_shop_arr[potion_product_id][1]}!")


# fungsi main shop
def shop(monster_inventory_arr, potion_inventory_arr, monster_shop_arr, item_shop_arr, monster_arr):
    print("Irasshaimase! Selamat datang di SHOP!!")

    while True:

        action = input(">>> Pilih aksi (lihat/beli/keluar): ")

        if action == "lihat":
            show_items(monster_arr, item_shop_arr, monster_shop_arr )

        elif action == "beli":
            buy_item(monster_inventory_arr, potion_inventory_arr, monster_shop_arr, item_shop_arr, monster_arr)

        elif action == "keluar":
            print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)")
            break
