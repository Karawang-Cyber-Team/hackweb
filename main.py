"""
Please don't remove name author! Belajarlah ngoding bro. 
Jangan bisanya ganti nama author doang, gpp lah ganti nama author,
asal untuk pemakaian pribadi. Kalau mau repost izin dulu ya!

Team      : Karawang Cyber Team And Kobustor Ghost Team
WhatsaApp : 085811309493
Facebook  : TrueFalseID

warning this tools!!
gunakan tools ini sewajarnya saja. Jangan di gunakan untuk tindak
criminal, cyber crime dll. Hacking Itu Ilegal bro! Apabila You
terkena pidana karena sudah merusak suatu website pembuat tools
jangan di bawa - bawa okeyy?! Kalo mau rusak suatu website mending
website luar negeri aja. Jangan dalam negeri. 
Karena Resiko ke Ciduk kang bakso lebih kecil, di banding dalam negeri.
"""

import os, time, sys
import urllib3, urllib 
import re 
from lib.colors import *
from src import*

def clear():
  os.system('clear')
  
def main():
  time.sleep(3);clear()
  print(f"""{R}
\t\t  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠛⠛⠛⠛⠛⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\t\t⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣄⠀⠀⠀⠀⠀⠀⠀⠀
\t\t⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀
\t\t⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀
\t\t⠀⠀⠀⠀⠀⠀⢀⡿⠀⠀⢀⣀⣤⡴⠶⠶⢦⣤⣀⡀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀
\t\t⠀⠀⠀⠀⠀⠀⠘⣧⡀⠛⢻⡏⠀⠀⠀⠀⠀⠀⠉⣿⠛⠂⣼⠇⠀⠀⠀⠀⠀⠀
\t\t⠀⠀⠀⠀⢀⣤⡴⠾⢷⡄⢸⡇⠀⠀⠀⠀⠀⠀⢀⡟⢀⡾⠷⢦⣤⡀⠀⠀⠀⠀
\t\t⠀⠀⠀⢀⡾⢁⣀⣀⣀⣻⣆⣻⣦⣤⣀⣀⣠⣴⣟⣡⣟⣁⣀⣀⣀⢻⡄⠀⠀⠀
\t\t⠀⠀⢀⡾⠁⣿⠉⠉⠀⠀⠉⠁⠉⠉⠉⠉⠉⠀⠀⠈⠁⠈⠉⠉⣿⠈⢿⡄⠀⠀
\t\t{W}⠀⠀⣾⠃⠀⣿⠀⠀⠀⠀⠀⠀⣠⠶⠛⠛⠷⣤⠀⠀⠀⠀⠀⠀⣿⠀⠈⢷⡀⠀
\t\t⠀⣼⠃⠀⠀⣿⠀⠀⠀⠀⠀⢸⠏⢤⡀⢀⣤⠘⣧⠀⠀⠀⠀⠀⣿⠀⠀⠈⣷⠀
\t\t⢸⡇⠀⠀⠀⣿⠀⠀⠀⠀⠀⠘⢧⣄⠁⠈⣁⣴⠏⠀⠀⠀⠀⠀⣿⠀⠀⠀⠘⣧
\t\t⠈⠳⣦⣀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠻⠶⠶⠟⠀⠀⠀⠀⠀⠀⠀⣿⠀⢀⣤⠞⠃
\t\t⠀⠀⠀⠙⠷⣿⣀⣀⣀⣀⣀⣠⣤⣤⣤⣤⣀⣤⣠⣤⡀⠀⣤⣄⣿⡶⠋⠁⠀⠀
\t\t⠀⠀⠀⠀⠀⢿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⠀⠀⠀\n
\t     {R} ＩＮＤＯＮＥＳＩＡ {W}ＨＡＣＫＴＩＶＩＳＴ
\t{W}[{R}${W}]{O}-------------------------------------------{W}[{R}${W}]
\t{W}[{R}${W}]{W} Author   : TrueFalseID                    {W}[{R}${W}]{B}
\t{W}[{R}${W}]{W} Github   : github.com/Karawang-Cyber-Team {W}[{R}${W}]{B}
\t{W}[{R}${W}]{W} Team     : Karawang Cyber Team            {W}[{R}${W}]{B}
\t{W}[{R}${W}]{O}-------------------------------------------{W}[{R}${W}]\n
\t  {W}[{R}01{W}]{W} Admin Finder              {W}[{R}02{W}]{W} Batsploit
\t  {W}[{R}03{W}]{W} Brouter                   {W}[{R}04{W}]{W} Brute any
\t  {W}[{R}05{W}]{W} CrackPass                 {W}[{R}06{W}]{W} DdosWeb
\t  {W}[{R}07{W}]{W} Fc Crack                  {W}[{R}08{W}]{W} KeyLogger
\t  {W}[{R}09{W}]{W} Pdis Cover                {W}[{R}10{W}]{W} Ransomware
\t  {W}[{R}11{W}]{W} Socket Web                {W}[{R}12{W}]{W} Ud Flood
\t  {W}[{R}13{W}]{W} Wd Generator              {W}[{R}14{W}]{W} Z Crack
\t  {W}[{R}15{W}]{W} Informations Tools        {W}[{R}00{W}]{W} Exit Program\n
  """)
  chose = input(f'\t\t\t{W}[{R}●{W}]{W} Choose >>: ')
  
  if chose in ["01"]:
    import src.admin_finder
  elif chose in ["02"]:
    import src.batsploit
  elif chose in ["03"]:
    import src.brouter
  elif chose in ["04"]:
    import src.brute_any
  elif chose in ["05"]:
    import src.crackpass
  elif chose in ["06"]:
    import src.ddos_web
  elif chose in ["07"]:
    import src.fcrak
  elif chose in ["08"]:
    import src.keylogger
  elif chose in ["09"]:
    import src.pdiscover
  elif chose in ["10"]:
    import src.ransomware
  elif chose in ["11"]:
    import src.socket
  elif chose in ["12"]:
    import src.udpd
  elif chose in ["13"]:
    import src.wd_generator
  elif chose in ["14"]:
    import src.zCrack
  elif chose in ["15"]:
    import src.data_memek
  elif chose in ["00"]:
    print("\n\t\tPlease Starts My Repository Bro:)");time.sleep(3);os.system("xdg-open https://github.com/Karawang-Cyber-Team");sys.exit()
  else:print(f"\n\t\t\t{W}[{R}!{W}]{R} Wrong Input Bro");time.sleep(3);clear();main()
if __name__ =='__main__':
  main()
