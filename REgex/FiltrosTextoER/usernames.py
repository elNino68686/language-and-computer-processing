# -- Problema: Alien username
import re 

f = open("usernames.txt", "r+")


print("««« Searching Valid Alien Usernames »»»")

for linha in f:

  y = re.search(r'(_|.)([0-9]+[A-Za-z]{3,})(_?)$', linha)
  if y:
    print("----------inic match------------------")
    print(y)
    print(y.string)
    print(y.span())
    print(y.groups())
    print(y.group())
    print("-----------fim match-------------------")
    f.write("valido\n")
  else:
    f.write("invalido\n")




print("««« Search »»»")


