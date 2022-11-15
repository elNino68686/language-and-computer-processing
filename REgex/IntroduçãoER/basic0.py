import re
# output only the lines with the following characteristics:
# 1. that contains the word hello at the beginning of the line

print("Linhas que contêm a palavra: hello no início (à esquerda)")
inputFromUser = input(">> ")
while inputFromUser != "":
  y = re.match(r'(?i)hello', inputFromUser)
  if(y): 
    print("Sucesso, padrão encontrado:")
    print(y.string,' contém ',y.group())   
  else:
    print("hello não encontrado")
  inputFromUser = input(">> ")
  
  
#?i  case insensitive, a palavra pode ter letras maiusculas e minusculas misturadas