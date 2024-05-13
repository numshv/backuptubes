def monster(nama, tingkat, kesehatan, serangan):
    return {
        'nama': nama,
        'tingkat': tingkat,
        'kesehatan': kesehatan,
        'kesehatan_maks': kesehatan,
        'serangan': serangan
    }

def arena():
    def randint(start, end):
        return start + (hash(str(start) + str(end)) % (end - start + 1))

    def pilih_random(array):
        return array[randint(0, len(array) - 1)]

    monsters = [
        monster("Goblin", 1, 20, 5),
        monster("Orc", 2, 35, 8),
        monster("Dragon", 3, 50, 12),
        monster("Giant", 4, 70, 15),
        monster("Demon", 5, 100, 20)
    ]
    hadiah_stage = [30, 50, 100, 150, 200]
    total_hadiah = 0
    total_serangan_diberikan = 0
    total_serangan_diterima = 0

    def memulai_sesi_latihan():
        nonlocal total_hadiah, total_serangan_diberikan, total_serangan_diterima
        stage = 1
        while stage <= 5:
            print("\n========== Stage", stage, "==========")
            monster = pilih_random(monsters)
            print("Agent menghadapi", monster['nama'], "tingkat", monster['tingkat'])
            input("Tekan Enter untuk memulai pertarungan...")
            hasil = pertarungan(monster)
            if not hasil:  # Agent kalah
                print("Game Over! Agent kalah pada Stage", stage)
                break
            total_hadiah += hadiah_stage[stage - 1]
            stage += 1
            print("Agent berhasil menyelesaikan Stage", stage - 1)
            input("Tekan Enter untuk melanjutkan...")

        tampilkan_statistik()

    def pertarungan(monster):
        nonlocal total_serangan_diberikan, total_serangan_diterima
        while True:
            # Agent attack
            serangan_agent = randint(5, 20)
            monster['kesehatan'] -= serangan_agent
            print("Agent memberikan", serangan_agent, "damage kepada", monster['nama'])
            total_serangan_diberikan += serangan_agent
            if monster['kesehatan'] <= 0:
                print("Agent berhasil mengalahkan", monster['nama'])
                monster['kesehatan'] = monster['kesehatan_maks']  # Pulihkan kesehatan monster
                return True

            # Monster attack
            serangan_monster = randint(3, 15)
            print(monster['nama'], "memberikan", serangan_monster, "damage kepada Agent")
            total_serangan_diterima += serangan_monster
            if serangan_monster >= 20:  # Jika serangan monster besar, agent kalah
                return False

            input("Tekan Enter untuk melanjutkan pertarungan...")

    def tampilkan_statistik():
        print("\n========== Hasil Sesi Latihan ==========")
        print("Total hadiah yang diterima:", total_hadiah, "OC")
        print("Berhasil menang hingga stage:", min(5, (total_hadiah // 30)))
        print("Total damage yang diberikan:", total_serangan_diberikan)
        print("Total damage yang diterima:", total_serangan_diterima)

    return memulai_sesi_latihan

latihan = arena()
latihan()