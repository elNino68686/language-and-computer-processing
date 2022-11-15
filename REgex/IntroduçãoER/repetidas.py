#Elimina palavras ou numeros seguidos repetidos
import re

frase = input()
while frase != "":
  frase = re.sub(r'([a-zA-Z]+|[0-9]+)(\s+\1)+', r'\1', frase)

  print(frase)
  frase = input()
