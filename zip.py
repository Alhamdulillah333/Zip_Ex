import os

os.system("clear")
print("""\033[1;32m             _.-'`)     (`'-._
          .' -' / __    \\ '- '.
         / .-' ( '-°,`|   ) '-. \\
        / .-',-`'._/ \\_.'`-,'-. \\
       ; ; /.`'.-'(   )'-.'`.\\ ; ;
       | .-'|\\//'-/   \\-'\\\/|'-. |
       |` |; :|'._\\   /_,'|: ;| `|
       || : |;    `Y-Y`    ;| : ||
       \\:| :/======"="======\\| |:/
       /_:-`                 `-;_\\
      System Maker :: Rules Breaker
\033[1;31m════════════════════════════════════════════
\033[1;33m[•] Tool Name    : Zip Password Cracker
[•] Developed By : Dark-NH
[•] GitHub       : github.com/DarkNH-cyber
[•] Version      : 1.0.0
[•] Status       : ONLINE
\033[1;31m════════════════════════════════════════════
\033[36m[!] A high-speed ZIP password cracker tool designed for.
[!] Uses a wordlist to perform a brute-force style attack.
\033[1;31m≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈\033[0m""")

import zipfile

z = input("\033[1;33mEnter Zip File path: \033[0m")
zip_file = zipfile.ZipFile(z)

pw = input("\033[1;33mEnter Password List File path: \033[0m")
file = open(pw, "r")

for password in file:
    password = password.strip()
    try:
        zip_file.extractall(pwd=bytes(password, "utf-8"))
        print("\033[1;32mPassword Found: " + password)
        break
    except:
        print("\033[1;31mWrong Password: " + password)
        
print("\n\033[1;36mFile Extract Successfully...!")