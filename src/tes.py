def yesorno(text):
    while True:
        agreement = input(text).lower()
        if agreement == 'y' or agreement == 'n':
            break
        else:
            print('Input tidak valid!')
    return agreement

tes = yesorno('lanjut? (Y/N): ')
print(tes)

