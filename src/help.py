def help(login_state, player_role):
    print ("""===================== HELP ======================""")
    
    if login_state == 1:
        if player_role == "admin":
                print ("""
Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:
    1. LOGOUT        : Keluar dari akun yang sedang digunakan
    2. SHOP_MANAGE   : Mengatur isi dari seluruh barang yang dijual di dalam shop
    3. MONSTER_MANAGE: Menampilkan dan menambah monster yang ada di dalam program
                   
Footnote: 
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
    2. Jangan lupa untuk memasukkan input yang valid
        """)
        else:
            print ("""
Selamat datang, User. Berikut adalah command yang dapat kamu gunakan:
    1. LOGOUT   : Keluar dari akun yang sedang digunakan
    2. SHOP     : Menampilkan barang yang dijual di dalam shop
    3. Gacha    : Menggacha monster????
    4. BATTLE   : Melawan monster
    5. INVENTORY: Melihat seluruh detail akun dan items user
    6. ARENA    : Latihan bertarung melawan monster
    7. LAB      : Upgrade monster yang dimiliki di Laboratory 
Footnote: 
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
    2. Jangan lupa untuk memasukkan input yang valid
            """)
    else:
        print(""" 
Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu. 
Ketik command:
            
    1. LOGIN   : Untuk masuk ke dalam akun yang sudah terdaftar
    2. REGISTER: Untuk membuat akun baru
              
Footnote: 
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
    2. Jangan lupa untuk memasukkan input yang valid
        """)