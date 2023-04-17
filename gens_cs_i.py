###############################################
# Workshop KORMA Intellogy | Hands on Project
# Scope : Cybersecurity with Python
# By : Genesaret Johnes (Genes)
# Date Created : UTC+7 | 17 April 2023
###############################################

# Source code memeriksa port dan juga atribut lainnya dalam satu host IP Address menggunakan NMAP

# Mengimpor library yang diperlukan
import nmap
import os, platform

# Konfirmasi apabila sudah menginstal nmap, karena SC ini membutuhkan NMAP terinstal dan sudah ada PATH nya
installed = input("\033[93mPastikan anda sudah menginstal nmap dan mengatur PATH untuk nmap. Input\033[0m \033[92my\033[0m \033[93matau \033[92mY\033[0m \033[93muntuk melanjutkan : \033[0m")

# Keluar aplikasi apabila input bukan y / Y
if installed != 'y' and installed != 'Y':
    print("\033[91mInstal NMAP terlebih dahulu...\033[0m")
    exit()

# Status untuk mengeluarkan dari looping While dibawah, dalam artian untuk keluar dari aplikasi
is_still_on_app = True

# Inisialisasi PortScanner
nm = nmap.PortScanner()

# Membuat fungsi untuk memeriksa host
def scan_host():
    try:
        # Input IP address yang akan diperiksa
        print('Input IP Address, bisa dalam bentuk range seperti \033[95m192.168.0-255.1-127\033[0m atau \033[95m172.10.10.2/20\033[0m')
        network_range = input('Masukkan IP Address (v4) untuk diperiksa : ')

        # Melakukan scanning terhadap network_range yang diberikan
        # Pastikan anda memberikan hak akses yang cukup untuk ini
        nm.scan(hosts=network_range, arguments='-sS -O')
        for host in nm.all_hosts():
            print('='*50)
            print('Host: {} ({})'.format(host, nm[host].hostname()))
            print('Status: {}'.format(nm[host].state()))
            print('='*50)
            print('')
            for proto in nm[host].all_protocols():
                print(f'Protokol: {proto}')
                ports = nm[host][proto].keys()
                for port in ports:
                    print('='*30)
                    print('Port: {} \tState: {}'.format(port, nm[host][proto][port]['state']))
                    print('Service: {}'.format(nm[host][proto][port]['name']))
                    print('='*30)
                    print('')
        print('*'*50)
        decision = input('\033[93mLanjut pemeriksaan IP Address ? (y/N)\033[0m')
        if(decision == 'N' or decision == 'n'):
            print('\033[91mPemeriksaan berakhir.\033[0m')
            global is_still_on_app
            is_still_on_app = False
        clear()
    except Exception as err:
        print('\033[93mTerjadi error pada aplikasi\033[0m')
        print(f'\033[93mPesan error : {err}\033[0m')
        exit()

# Hanya untuk membersihkan layar konsol
def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')

while(is_still_on_app):
    scan_host()