import os, sys
try:os.system("clear")
except:pass
os.system('termux-setup-storage')
os.system('git pull')
os.system('xdg-open https://chat.whatsapp.com/FvEW9ARKwOOLVTJIzd8SKH')
try:
    __import__("RANDOM").menu()
except Exception as e:
    exit(str(e))
