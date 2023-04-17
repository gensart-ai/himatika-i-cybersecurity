###############################################
# Workshop KORMA Intellogy | Hands on Project II
# Scope : Cybersecurity with Python
# By : Genesaret Johnes (Genes)
# Date Created : UTC+7 | 17 April 2023
###############################################

# Source code men-generate password acak

# Mengimpor library yang diperlukan
import random
import string
import os, platform
from password_strength import PasswordStats

# Untuk state aplikasi
is_still_on_app = True

def generate_password_combines_name():

    # Meminta input nama
    name = input("\033[93mIsikan nama anda: \033[0m")

    # Meminta input panjang karakter
    length = int(input("\033[93mIsikan panjang karakter (berupa angka integer): \033[0m"))

    # Meminta input password dapat mengandung angka
    number_containable = input("\033[93mPassword dapat mengandung angka (y/N): \033[0m")

    # Meminta input password dapat mengandung simbol
    symbol_containable = input("\033[93mPassword dapat mengandung simbol (y/N): \033[0m")

    # Mengambil data ASCII dari library string
    characters = string.ascii_letters

    if(number_containable == 'y'):
        characters += string.digits
    
    if(symbol_containable == 'y'):
        characters += string.punctuation

    # Menambahkan string nama ke dalam data ASCII
    characters += name

    # Men-generate password
    password = ''.join(random.choice(characters) for i in range(length))

    # Inisiasi stat password untuk melihat skor kekuatan
    stat = PasswordStats(password)

    # Menampilkan password yang telah dibuat
    print('='*50)
    print(f"\033[93mPassword tergenerate untuk nama \033[0m\033[95m'{name}'\033[0m\033[93m: \033[95m{password}\033[0m")
    print('='*50)
    print('Skor kekuatan password (skor bagus >= 0.6) : {}'.format(stat.strength()))
    print('='*50)
    print('')

    # Decision untuk lanjut generate atau tidak
    decision = input('\033[93mLanjut generate password ? (y/N)\033[0m')
    if(decision == 'N' or decision == 'n'):
        print('\033[91mPemeriksaan berakhir.\033[0m')
        global is_still_on_app
        is_still_on_app = False
        exit()
    clear()


# Hanya untuk membersihkan layar konsol
def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')

# Ini akan terus berjalan sampai user menginput N atau n pada konfirmasi lanjut generate password
while(is_still_on_app):
    generate_password_combines_name()