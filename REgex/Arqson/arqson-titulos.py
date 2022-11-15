# Quais os títulos das músicas alentejanas
import re

alentejanas = []

f = open("arqson.txt",encoding="utf-8")

for linha in f:
    campos = re.split(r'::', linha)
    if (campos[0] == "Alentejo"): 
        alentejanas.append(campos[2])

for cancao in alentejanas:
    print(cancao)

