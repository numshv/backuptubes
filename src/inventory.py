def inventory(player_id, monster_inventory_arr, item_inventory_arr, player_oc, monster_arr):
    print(f'============ INVENTORY LIST (User ID: {player_id}) ============')
    print(f'Jumlah O.W.C.A. Coin-mu sekarang {player_oc}.')
    
    for i in range(len(monster_inventory_arr)):
        if monster_inventory_arr[i][0] == player_id:
            cur_monster_id = monster_inventory_arr[i][1]
            for j in range (len(monster_arr)):
                if monster_arr[j][0] == cur_monster_id:
                    print