import os, sys
try:
    __import__("FILE").menu()
except Exception as e:
    exit(str(e))
