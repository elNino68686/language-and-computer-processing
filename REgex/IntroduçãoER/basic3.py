import re
# output only the lines with the following characteristics:
# 1. that contains the word hello at the beginning of the line

print("substituição de hello na linha")
inputFromUser = input(">> ")
while inputFromUser != "":
  new_text = re.sub(r'(?i:hello)', '*YEP*', inputFromUser)
  print(new_text) 
  #y = re.search(r'(?i:hello)([0-9]+)', inputFromUser)
  #print(y.group(), " ==> " , y.group(1))
  new_text1 = re.sub(r'(?i:<\/?([^>]+)>)', r' ', inputFromUser) #tira as tags todas deixando o texto limpo
  print(new_text1)
  inputFromUser = input(">> ")


# substituição da palavra hello por *YEP*
# >> hello joao pedro hello
# *YEP* joao pedro *YEP*
  
  
#por exemplo em html, para deitar fora uma tag e ficar com o conteudo
#(?i:\<\/(.+)\>
#falta adicionar a parte de tirar a barra no fecho da tag