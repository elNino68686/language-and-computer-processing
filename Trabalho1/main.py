import func, os
def printMenu():

    print("\n \t\t\t\t\tMenu\n")
    print("\t[1] - Calcular a frequência de procsessos por ano.", end = "\n") 
    print("\t[2] - Calcular a frequência de nomes próprios por século.", end = "\n")
    print("\t[3] - Calcular a frequência de apelidos por século.",end="\n")
    print("\t[4] - Calcular a frequência dos vários tipos de relação.",end="\n")
    print("\t[5] - Imprimir os 20 primeiros registos num novo ficheiro output em formato Json.", end="\n")
    print("\t[0] - Sair")



def init():

    
    printMenu()
    opc = input("Escolha uma opção: ")
    f = open("teste.txt", 'r')
    ficheiro = f.readlines()

    while opc != 0:

        if opc == '1': #frequêncida de processos por ano
            print(func.freq_processos_ano(ficheiro))
            func.dic_html(["Ano", "Numero de processos"], func.freq_processos_ano(ficheiro), "freq_processos_ano.html")
            os.system("open -a \"Google Chrome\" html/freq_processos_ano.html")
            
        elif opc == '2': #frequencia de nomes proprios por século
            print(func.freq_nomes_proprios_sec(ficheiro))
            func.dic_dic_html(["Seculo", "Primeiro Nome", "Frequencia"], func.freq_nomes_proprios_sec(ficheiro), "freq_nomes_proprios_sec.html")
            os.system("open -a \"Google Chrome\" html/freq_nomes_proprios_sec.html")
            

        elif opc == '3': #frequencia de apelidos por século
            print(func.freq_apelidos_sec(ficheiro))
            func.dic_dic_html(["Seculo", "Apelido", "Frequencia"], func.freq_apelidos_sec(ficheiro), "freq_apelidos_sec.html")
            os.system("open -a \"Google Chrome\" html/freq_apelidos_sec.html")
            

        elif opc == '4': #frequencia de relaçõess
            print(func.freq_relacoes(ficheiro))
            func.dic_html(["Relacoes", "Frequencia"], func.freq_relacoes(ficheiro), "freq_relacoes.html")
            os.system("open -a \"Google Chrome\" html/freq_relacoes.html")

        elif opc == '5':
            print(func.to_json(ficheiro))
            os.system("open output.json")
                
                    
          
        elif opc == '0':
            print("Fim")
            break 

        print()
        printMenu()
        opc = input("Escolha uma opção: ")   

init()