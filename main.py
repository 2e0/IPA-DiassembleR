import asyncio
import time
from time import sleep
import os
import colorama
from colorama import *


banner = '''

 ____  ____   __       ____  ____    __    ___  ___  ____  __  __  ____  __    ____  ____ 
(_  _)(  _ \ /__\  ___(  _ \(_  _)  /__\  / __)/ __)( ___)(  \/  )(  _ \(  )  ( ___)(  _ \
 _)(_  )___//(__)\(___))(_) )_)(_  /(__)\ \__ \\__ \ )__)  )    (  ) _ < )(__  )__)  )   /
(____)(__) (__)(__)   (____/(____)(__)(__)(___/(___/(____)(_/\/\_)(____/(____)(____)(_)\_)

'''

print(Fore.RED + banner)
sleep(3)
os.system("clear")

banner1 = '''
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
'''

print(Fore.WHITE + banner1)
base = "_base__src"
sleep(1)

fileText = '''
     -|_
      |
     _|_
    //_/\


@root/ipa-dias! # Merci de sélectionner votre fichier .ipa : '''

file = input(Fore.RED + fileText)
name = file.rsplit('.', maxsplit=1)[0]
os.system("clear")

print(Fore.WHITE + banner1)


print (Fore.BLUE + "En cours de tester si le fichier " + file.rsplit('.', maxsplit=1)[0] + " existe...")
sleep(3)
print(Fore.GREEN + "[+] Succès")
print(Fore.BLUE + "Deobfuscation IPA metadatas")
sleep(2)
print(Fore.GREEN + "[+] Succès")
print(Fore.BLUE + "Conversion de l'IPA en ZIP")
def ipa2zip():
    import pathlib
    from pathlib import Path
    p = Path(file)
    p.rename(p.with_suffix('.zip'))
ipa2zip()
sleep(5)
print(Fore.GREEN + "[+] Succès")
print(Fore.BLUE + "Exécution de mkdir (pour stocker le code source de l'IPA")
def mkdir():
    os.system("mkdir " + name + base)
mkdir()
sleep(2)
print(Fore.GREEN + "[+] Succès")
print(Fore.BLUE + "Déplacement du fichier IPA dans la base_src")
def deplacement():
    os.system("mv " + name + ".zip -t " + name + base)
deplacement()
print(Fore.GREEN + "[+] Succès")
sleep(3)
print(Fore.BLUE + "Décompression du fichier")
def decompression():
    os.system("cd " + name + base + " && unzip " + name + ".zip")
decompression()

print(Fore.BLUE + "\n Merci d'avoir utilisé mon tool")




































