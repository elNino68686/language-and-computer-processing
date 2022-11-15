import re
# Split string by the specified re:

print("Split com limites, de uma linha, por uma RE: ")
print("Informação dum aluno no formato: NumAl; NomeCompl; N1; ...; Nn")
inputFromUser = input(">> ")
while inputFromUser != "":
  lista = re.split(r';', inputFromUser, maxsplit=2)
  notas = re.split(r';', lista[2])
  soma = 0
  for n in notas:
      soma = soma + int(n)
  med = soma/len(notas)
  print(lista)
  print("O aluno com número ", lista[0], " e nome ", lista[1], " tem média: ", med) 
  inputFromUser = input(">> ")

"""
>> 87; joao; 20; 20; 20
O aluno com número  87  e nome   joao  tem média:  20.0
>> 
"""

#maxsplit(2) parte a lista nos 2 primeiros e o ultimo todo