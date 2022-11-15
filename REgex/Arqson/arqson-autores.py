# Quais os títulos das músicas de um dado cantor
import re

#cantor = input("Autor? ")

f = open("arqson.txt",encoding="utf-8")

for linha in f:
    campos = re.split(r'::', linha)
    if (len(campos) >= 5):
       esta = re.search(r'.*Jorge.*', campos[3])
       #esta = re.search(rf'.*{cantor}.*', campos[3])
    
       #esta = re.search(r'.+\.mp3', campos[4])
       if (esta):
           print(campos[1]," # ",campos[2])

