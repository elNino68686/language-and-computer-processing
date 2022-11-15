import re
# Split string by the specified re:

lista = []
print("Split de uma linha por uma RE: ")
opc = int( input("Escolha: 1. Separar Datas; 2. Separar por Virgulas; 3. Separar por Numeros; 0. Terminar  ? ") )

while opc:
  if (opc<0 or opc >3):
     print("Opção Inválida!") 
  else:
    inputFromUser = input("Frase-fonte >> ")
    if opc == 1:
       lista = re.split(r'[-/.:]', inputFromUser)
       if len(lista) == 3:
          print("Dia: ", lista[2]) 
    elif opc == 2:
       lista = re.split(r',', inputFromUser)
    elif opc == 3:
       lista = re.split(r'[0-9]+', inputFromUser)
    print(lista)     
  
  opc = int(input("EScolha: 1. Separar Datas; 2. Separar por Virgulas; 3. Separar por Numeros; 0. Terminar  ? "))

"""
Separar por virgulas:
Split de uma linha por uma RE:
>> [1,2,3,4,5]
['[1', '2', '3', '4', '5]']
>> olá, isto é fixe, e cool!
['olá', ' isto é fixe', ' e cool!']
>>

Separar datas
Frase-fonte >> 24-6-1998
Dia:  24
['24', '6', '1998']


Separar por numeros:
Frase-fonte >> 1 joao 2 pedro 34 joao
['', ' joao ', ' pedro ', ' joao']
"""
