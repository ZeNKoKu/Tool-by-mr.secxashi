import os, sys

os.system("pkg install pip")
os.system("pkg install update")
os.system("pkg install git")
os.system("pkg install python")
os.system("pkg install sysvbanner")
os.system("pkg install banner")
os.system("pkg install figlet")
os.system("clear")
os.system("figlet -f mono9 Mr.SECXASHI | lolcat -a")
os.system("banner Script created by Mr.SECXASHI")
print("https://github.com/ZeNKoKu")
print("Version 0.0.1")
print("")
print("")
print("1.All Tool Hacking")
print("To exit, type exit.")
all = input("select : ")
if all == "1" or all == "01":
    print("1.Web hacking")

Tool = input("select : ")
if Tool == "1" or Tool == "01":
    print("")
    print("01.Sqlmap")
    print("02.Nmap")
    print("03.Hydra")
print("")
print("Which one do you want to install ?")
Tool2 = input("select : ")

if Tool2 == "1" or Tool2 == "01":
    os.system("pip install sqlmap")
if Tool2 == "2" or Tool2 == "02":
    os.system("pip install nmap")
if Tool2 == "3" or Tool2 == "03":
    os.system("pip install hydra")
print("")
print("")
print("Thank")
