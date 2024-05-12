running_state = True

def intro():
    intro1= " __      __         .__                                    __          ________  __      ___________     _____    "
    intro2= "/  \    /  \  ____  |  |    ____   ____   _____   ____   _/  |_ ____   \_____  \/  \    /  \_   ___ \   /  _  \   "
    intro3= "\   \/\/   /_/ __ \ |  |  _/ ___\ /  _ \ /     \_/ __ \  \   __|  _ \   /   |   \   \/\/   /    \  \/  /  /_\  \  "
    intro4= " \        / \  ___/ |  |__\  \___(  <_> )  Y Y  \  ___/   |  |(  <_> ) /    |    \        /\     \____/    |    \ "
    intro5= "  \__/\  /   \___  >|____/ \___  >\____/|__|_|  /\___  >  |__| \____/  \_______  /\__/\  /  \______  /\____|__  / "
    intro6= "       \/        \/            \/             \/     \/                        \/      \/          \/         \/  "
    
    intro7= 'Selamat datang di markas rahasia O.W.C.A. !'
    intro8= 'Bersama O.W.C.A. mari kita basmi Asep Spakbor dan anteknya!'.center(45, ' ')
    
    intro7_ctr = intro7.center(len(intro7)+90, ' ')
    intro8_ctr = intro8.center(len(intro8)+76, ' ')
                                                                                                                       
    intro_ctr_arr = [intro1, intro2, intro3, intro4, intro5, intro6]
    
    print('\n\n\n')
    
    for i in range (len(intro_ctr_arr)):
        ctr_intro = intro_ctr_arr[i].center(len(intro_ctr_arr[i])+17, ' ')
        print(ctr_intro)
    
    print('\n')
    print(intro7_ctr)
    print(intro8_ctr)
    
    print('\n\nKetik command HELP untuk mengetahui navigasi perintah.')
    print('Sebelum memulai misi, pastikan anda telah LOGIN ke akun anda.\n')
    
    # Mau tambahin tulisan buat akses help sama cerita awal

# Fungsi untuk navigasi command
def help():
    pass


def exited():
    global running_state
    print("""
__________                     __________                  
\______   \ ___.__.  ____      \______   \ ___.__.  ____   
 |    |  _/<   |  |_/ __ \      |    |  _/<   |  |_/ __ \  
 |    |   \ \___  |\  ___/      |    |   \ \___  |\  ___/  
 |______  / / ____| \___  >     |______  / / ____| \___  > 
        \/  \/          \/             \/  \/          \/  
                                                            
          """)
    running_state == False
    exit(0)