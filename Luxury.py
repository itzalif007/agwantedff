import os, sys
os.system("git pull")
os.system("pip uninstall requests chardet urllib3 idna certifi -y && pip install chardet urllib3 idna certifi requests")
os.system('xdg-open https://chat.whatsapp.com/FvEW9ARKwOOLVTJIzd8SKH')
try:
    __import__("FILE").menu()
except Exception as e:
    exit(str(e))
