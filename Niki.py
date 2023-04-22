import os, sys
try:
    __import__("ANE").menu()
except Exception as e:
    exit(str(e))
