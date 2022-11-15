import re


texto = """
este texto foi feito por Pedro  Rafael Paiva   Moura com a ajuda
do professor Pedro   Henriques.
"""


def processa_nome(m):
	primeiro = m[1]
	ultimo = m[2].lstrip() 
	#lstrip() remove todos os espaços

	return f"{ultimo}, {primeiro[0]}."

nome = r'[A-Z][a-z]+'

#novo_texto = re.sub(rf'({nome})([ ]+{nome})+', r'\2 \1', texto)
novo_texto = re.sub(rf'({nome})([ ]+{nome})+', processa_nome, texto)
print(novo_texto)

