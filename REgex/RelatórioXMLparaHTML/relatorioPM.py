import re


def xml_to_html(relatorio):

    configs = re.search(r'<\?xml.+\?>', relatorio)
    configs = configs.group()

    encoding = re.search(r'encoding=(".+")', configs)
    encoding = encoding.group(1) 
    
    relatorio = re.sub(r'<\?xml.+\?>', r'<!DOCTYPE html>', relatorio)
    relatorio = re.sub(
        r'<relatorio>((.|\n)*)</relatorio>',
        rf'''<html>\n<head>\n<meta charset={encoding}/>\n</head>\n<body>\1</body>\n</html>''',
        relatorio)
    
    relatorio = re.sub(r'<titulo>((.|\n)*)</titulo>', r'<h1>\1</h1><br>', relatorio)

    relatorio = re.sub(r'<data>((.|\n)*)</data>', r'<h3>\1</h3><br><hr>', relatorio)

    relatorio = re.sub(r'<autores>((.|\n)*)</autores>', r'<ul>\1</ul><br><hr>', relatorio)
    relatorio = re.sub(r'<autor>((.|\n)*?)</autor>', r'<li>\1</li>', relatorio)
    relatorio = re.sub(r'<(nome|numero|email)>((.|\n)*?)</\1>', r'<p>\2</p>', relatorio)
    
    relatorio = re.sub(r'<descricao>((.|\n)*)</descricao>', r'<p>\1</p><br>', relatorio)

    print(relatorio)
    


#with open('relatorioPM.xml') as f:
#    content = f.read()
#    xml_to_html(content)
#    
f = open("relatorioPM.xml", "r")
content = f.read()
xml_to_html(content)
