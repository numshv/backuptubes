# Fungsi untuk menampilkan item
def show_items(inventory, item_type):
    if item_type == "monster":
        print("ID | Type          | ATK Power | DEF Power | HP   | Stok | Harga")
        for i in range (len(monster_arr)):
            print (f"{monster_arr[i][0]}  | {monster_arr[i][1]} | {monster_arr[i][2]} | {monster_arr[i][3]} | {monster_arr[i][4]} | {monster_shop_arr[i][1]} | {monster_shop_arr[i][2]}")
    elif item_type == "potion":
        print("ID | Type                | Stok | Harga")
        for item in inventory["potion"]:
            print(f"{i+1}  | {item_shop_arr[i][0]} | {item_shop_arr[i][1]} | {item_shop_arr[i][2]}")
    else:
        print("Tipe item tidak valid.")

# Fungsi untuk membeli item
def buy_item(inventory, item_type, item_id, qty, global_oc):
    print(f"Jumlah O.W.C.A. Coin-mu sekarang {global_oc}.\n")

    product = input(">>> Mau beli apa? (monster/potion): monster")
    if product == "monster":
        monster_product_id = input(">>> Masukkan id monster: ")
        

    item = next((i for i in items if i["id"] == item_id), None)
    if not item:
        print("Item tidak ditemukan.")
        return False

    if item_type == "monster":
        if qty > 1:
            print("Hanya dapat membeli 1 monster sekaligus.")
            return False
        if oc < item["harga"]:
            print("OC-mu tidak cukup.")
            return False
    else:
        if oc < item["harga"] * qty:
            print("OC-mu tidak cukup.")
            return False
        if item["stok"] < qty:
            print("Stok tidak mencukupi.")
            return False

    # Validasi pembelian monster: cek apakah monster sudah ada di inventory
    if item_type == "monster":
        if any(i["type"] == item["type"] for i in inventory["monster"]):
            print(f"Monster {item['type']} sudah ada dalam inventory-mu! Pembelian dibatalkan.")
            return False

    # Lakukan pembelian
    if item_type == "monster":
        print(f"Berhasil membeli item: {item['type']}. Item sudah masuk ke inventory-mu!")
    else:
        print(f"Berhasil membeli {qty} {item['type']}. Item sudah masuk ke inventory-mu!")
        item["stok"] -= qty
    return True

def shop(inventory, item_type, item_id, qty, oc):
    print("Irasshaimase! Selamat datang di SHOP!!")
    Print(">>> Pilih aksi (lihat/beli/keluar): ")

    if action == "lihat":
        show_items(inventory, item_type)
    elif action == "beli":
        buy_item(inventory, item_type, item_id, qty, oc)
    elif action == "keluar":
        print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)")

# Main program
"""
def main():
    inventory = {
        "monster": [
            {"id": 1, "type": "Pokemon Air", "ATK Power": 10, "DEF Power": 1000, "HP": 200, "stok": 1, "harga": 100},
            {"id": 2, "type": "Pokemon Api", "ATK Power": 20, "DEF Power": 1000, "HP": 200, "stok": 5, "harga": 20},
            {"id": 3, "type": "Pokemon Tanah", "ATK Power": 30, "DEF Power": 430, "HP": 100, "stok": 0, "harga": 300}
        ],
        "potion": [
            {"id": 1, "type": "Strength Potion", "stok": 1, "harga": 20},
            {"id": 2, "type": "Resilience Potion", "stok": 5, "harga": 300}
        ]
    }

    oc = 1000  # Jumlah O.W.C.A. Coin

    while True:
        print("\nIrasshaimase! Selamat datang di SHOP!!")
        action = input(">>> Pilih aksi (lihat/beli/keluar): ")

        if action == "lihat":
            item_type = input(">>> Mau lihat apa? (monster/potion): ").lower()
            show_items(inventory, item_type)

        elif action == "beli":
            print(f"Jumlah O.W.C.A. Coin-mu sekarang {oc}.")
            item_type = input(">>> Mau beli apa? (monster/potion): ").lower()
            if item_type == "monster":
                item_id = int(input(">>> Masukkan id monster: "))
                success = buy_item(inventory, "monster", item_id, 1, oc)
            elif item_type == "potion":
                item_id = int(input(">>> Masukkan id potion: "))
                qty = int(input(">>> Masukkan jumlah: "))
                success = buy_item(inventory, "potion", item_id, qty, oc)
            else:
                print("Tipe item tidak valid.")
                continue

            if success:
                # Update OC agent setelah pembelian sukses
                if item_type == "monster":
                    oc -= inventory["monster"][item_id - 1]["harga"]
                else:
                    oc -= inventory["potion"][item_id - 1]["harga"] * qty

        elif action == "keluar":
            print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    main() """