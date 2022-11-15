import re


texto = """
- Eu gosto /mt de manga.
- Fixe! Eu /tb!
Fim da história /cqd.
"""

abreviaturas = {
	'tb': 'também',
	'mt': 'muito',
    'cqd': 'como queria demonstrar' 
}

def expande(m):
	return abreviaturas[m[1]]


texto_expandido = re.sub(r'/([a-z]+)', expande, texto)

print(texto_expandido)



