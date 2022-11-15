import re, json

def freq_processos_ano(ficheiro):

	#f = open(ficheiro, 'r')
	#l = ficheiro.readlines()

	dic = {} 
	proc = []
	for line in ficheiro.readlines():
		x = re.split(r'::',line)
		data = re.search(r'([0-9]{4})-([0-9]{2})-([0-9]{2})',line)

		if(data):
			if (x[0],x[1]) not in proc: 
				proc.append((x[0],x[1]))
	
				ano = data.group(1)
	
				if ano not in dic:
					dic[ano] = 1
				else:
					dic[ano] += 1	
	#f.close()
	return dic
            


def freq_nomes_proprios_sec(ficheiro):

	f = open(ficheiro, 'r')
	l = f.readlines()

	proc = []
	dic = {}

	for line in l:
		data = re.search(r'([0-9]{4})-([0-9]{2})-([0-9]{2})',line)
		y = re.sub(r'([A-Za-z]+)([ ][A-Za-z]+)*(\,[A-Za-z]+)?', r'\1', line)
		x = re.split(r'::', str(y))

		if(data):
			ano = data.group(1)
			seculo = int(ano[:2]) + 1
	
			if (x[0],x[1]) not in proc: 
				proc.append((x[0],x[1]))
	
				if seculo not in dic:
					dic[seculo] = {}
				for nome in x[2:5]:
					if nome != "":
						if nome not in dic[seculo]:
							dic[seculo][nome] = 1
						else:	
							dic[seculo][nome] += 1
	f.close()
	return dic	

	


def freq_apelidos_sec(ficheiro):

	f = open(ficheiro, 'r')
	l = f.readlines()

	proc = []
	dic = {}

	for line in l:
		data = re.search(r'([0-9]{4})-([0-9]{2})-([0-9]{2})',line)
		y = re.sub(r'([A-Za-z]+[ ])*([A-Za-z]+)(\,[A-Za-z]+)*', r'\2',line)
		x = re.split(r'::',str(y))

		if(data):
			ano = data.group(1)
			seculo = int(ano[:2]) + 1
	
			if (x[0],x[1]) not in proc: 
				proc.append((x[0],x[1]))
	
				if seculo not in dic:
					dic[seculo] = {}
				for nome in x[2:5]:
					if nome != "":
						if nome not in dic[seculo]:
							dic[seculo][nome] = 1
						else:	
							dic[seculo][nome] += 1
	
	f.close()
	return dic
	


def freq_relacoes(ficheiro):

	f = open(ficheiro, 'r')
	l = f.readlines()

	dic={}

	for line in l:
		x = re.split(r',',line)

		for elem in x[1:]:
			y = re.match(r'[A-Za-z]*(Irmao|Tio|Mae|Sobrinh[ao]|Pai|[nN]et[ao]|Meio|[Aa]vo)[A-Za-z ]*\.', elem)

			if(y):
				relacao = y.group()[:-1]
				if relacao not in dic:
					dic[relacao] = 1
				else:
					dic[relacao] += 1
	f.close()
	return dic			



def to_json(ficheiro):

	f = open(ficheiro, 'r')

	campos = ["Numero", "Data", "Nome", "Pai", "Mae", "Informacao Adicional"]
	lista = []
	dic = {}
	for i in range(20):
		l = f.readline()
		x = re.split(r'::', l)
		for elem in range(len(campos)):
			dic[campos[elem]] = x[elem]
		lista.append(dic)
		dic = {}
	
	f.close()

	with open("output.json", 'w') as fp:
		json.dump(lista,fp, indent = 4)



def dic_html(headers,info,ficheiro):
    f = open("html/" + ficheiro, "w+")
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")

    f.write("<style>\n")
    f.write("\ttable,td,th {\n \t\tborder: 1px solid black; \n")
    f.write("\t\tborder-collapse: collapse;\n \t\ttext-align: center;\n \t}\n")
    f.write("</style>\n")

    f.write("\t<table>\n")
    f.write("\t\t<tr>\n")
    # headers
    for i in range(0,len(headers)):
        f.write("\t\t\t<th>")
        f.write(headers[i])
        f.write("</th>\n")
    f.write("\t\t</tr>\n")

    for key,value in info.items():
        f.write("\t\t<tr>\n")
        f.write("\t\t\t<td>")
        f.write(key)
        f.write("</td>\n")
        f.write("\t\t\t<td>")
        f.write(str(value))
        f.write("</td>\n")
        f.write("\t\t</tr>\n")
    
    f.write("\t</table>\n")
    f.write("</html>")
    f.close()


def dic_dic_html(headers,info,ficheiro):
    f = open("html/" + ficheiro, "w+")
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")

    f.write("<style>\n")
    f.write("\ttable,td,th {\n \t\tborder: 1px solid black; \n")
    f.write("\t\tborder-collapse: collapse;\n \t\ttext-align: center;\n \t}\n")
    f.write("</style>\n")

    f.write("\t<table>\n")
    f.write("\t\t<tr>\n")
    # headers
    for i in range(0,len(headers)):
        f.write("\t\t\t<th>")
        f.write(headers[i])
        f.write("</th>\n")
    f.write("\t\t</tr>\n")	

    for key,value in info.items():
        f.write("\t\t<tr>\n")
        for x,y in value.items():
        	f.write("\t\t\t<td>")
        	f.write(str(key))
        	f.write("</td>\n")
        	f.write("\t\t\t<td>")
        	f.write(str(x))
        	f.write("</td>\n")
        	f.write("\t\t\t<td>")
        	f.write(str(y))
        	f.write("</td>\n")
        	f.write("\t\t</tr>\n")
    
    f.write("\t</table>\n")
    f.write("</html>")
    f.close()


	