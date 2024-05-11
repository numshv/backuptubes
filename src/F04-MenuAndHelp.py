import os

def Help():
    print ("""=========== Help ============""")

    global login_state
    if login_state:
        if username=="admin":
            print ("""
Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:
    1. Logout: Keluar dari akun yang sedang digunakan
    2. Shop_Management: Mengatur isi dari seluruh barang yang dijual di dalam shop
    3. Monster_Management: Menampilkan dan menambah monster yang ada di dalam program
                   
Footnote: 
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
    2. Jangan lupa untuk memasukkan input yang valid
        """)
        else:
            print ("""
Selamat datang, User. Berikut adalah hal-hal yang dapat kamu lakukan:
    1. Logout: Keluar dari akun yang sedang digunakan
    2. Shop: Menampilkan barang yang dijual di dalam shop
    3. Gacha: Menggacha monster
    4. Battle: Melawan monster
    5. Inventory: Melihat seluruh detail akun dan items user
    6. Arena: Latihan bertarung melawan monster
    7. Labolatory: Upgrade monster yang dimiliki
Footnote: 
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
    2. Jangan lupa untuk memasukkan input yang valid
            """)
    else:
        print(""" 
Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.
            
    1. Login: Masuk ke dalam akun yang sudah terdaftar
    2. Register: Membuat akun baru
              
Footnote: 
    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar
    2. Jangan lupa untuk memasukkan input yang valid
        """)
