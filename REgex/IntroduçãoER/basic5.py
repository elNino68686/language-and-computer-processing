import re


print("Split de uma linha por virgulas")

inputFromUser = input(">> ")

while inputFromUser != "":
  lista = re.split(r',', inputFromUser)
  for i in lista:
    print(i) 
  inputFromUser = input(">> ")


#>> joao,pedro
#joao
#pedro
#divide o texto pelo caracter dado neste caso a virgula  ','  
  
