import os
from parser import csv_parser

print("\nSelamat datang di lab! \n")
print("========= LIST MONSTER =========")

id_player = '007'
monster_name = []

monster_inventory_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)),'databases', 'monster_inventory.csv')
file_monster_inventory = open(monster_inventory_path, 'r')

monster_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)),'databases', 'monster.csv')
file_monster = open(monster_path, 'r')

i = 0

for line in file_monster_inventory:
    file_monster.seek(0)
    cur_monster = ''
    stripped = line.replace('\n', '')
    monster_inv = csv_parser(stripped)
    if monster_inv[0] == id_player:
        for lined in file_monster:
            monster = csv_parser(lined)
            if monster_inv[1] == monster[0]: 
                cur_monster = monster[1]
                monster_name.append(monster[1])
        i += 1
        print(f"{i}. {cur_monster} (Level: {monster_inv[2]})")

print("\n\n========= HARGA UPSKILL =========")
print("""Level 1 -> Level 2: 200 OC
Level 2 -> Level 3: 300 OC
Level 3 -> Level 4: 600 OC
Level 4 -> Level 5: 950 OC
""")

print(monster_name)

#monster_up = input('>>> Pilih monster: ')

