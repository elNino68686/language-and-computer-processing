import re

eu = ''
ele = ''

f = open("entrevista.txt", "r", encoding="utf-8")
for linha in f:
    entrev = re.search( r'^(?i:eu)\ *=\ *(.*)\.', linha)
    if (entrev):
        eu = entrev.group(1)
        print("--------")
    elif ( entrev := re.search( r'^(?i:ele)\ *=\ *(.*)\.', linha) ):
        ele = entrev.group(1)
        print("--------")
    else:
        linha = re.sub( r'^(?i:eu)\ *:\ *', 
                    rf'{eu}: ', 
                    linha)
        linha = re.sub( r'^(?i:ele)\ *:\ *', 
                    rf'{ele}: ', 
                    linha)
        print(linha) 


f.close()
