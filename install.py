import os
import time

os.system("sudo apt-get install figlet")
os.system("clear")

os.system("figlet XaLe")
print("YT-BoTTeR v2.0 Installation - Coded By Xale - GitHub: @xaletr")
print(" ")
select = input("Yükleme başlatılsın mı? (Y/N) ")

def kur():
 print("YT-BoTTeR Aracının VPN Ağı Kuruluyor. (Araç: Anonsurf)")
 os.system("git clone https://github.com/Und3rf10w/kali-anonsurf")
 os.system("cd kali-anonsurf && sudo sh installer.sh")

def iptal():
 os.system("clear")
 print("YT-BoTTeR yüklemesi iptal edildi.")

if select == "Y":
 kur()

elif select == "N":
 iptal()

elif select == "y":
 kur()

elif select == "n":
 iptal()

else:
 os.system("clear")
 print("Tanımsız Seçim , Tekrar Deneyin.")
