import os
from bibliografos import*

print("BEM VINDO AO PROGRAMA DE GRAFOS. Quer escrever um grafo[a], ler um grafo[b] ou sair do programa[c]?\n")

modo=input("opcao:")

modo.lower()

os.system('cls')

while modo!='c':
    if modo=="a":

        print("Qual tipo de grafo?\n")

        print("[a]- Grafo nao orientadado qualquer\n")

        print("[b]- Grafo especial\n")

        print("[c]-Voltar\n")

        submodo=input("opcao:")

        submodo.lower()

        os.system('cls')

        if submodo=="a": #Cria um grafo nao direcionado qualer
              
            nome = input("Coloque o nome do grafo: ") #Nome do grafo

            arquivo = open(nome+".txt","w") #Criação de arquivo como nome do grafo + .txt e escreve no arquivo

            arquivo.write(nome+"\n")

            n=int(input("Coloque o tamanho da matriz NxN: ")) #Cria a matriz

            m=[]
            for i in range(0,n):
                t = []
                for i in range(0,n):
                    t.append(0)
                m.append(t)

            os.system('cls')

            are = MatrizAdj(m,n) #Cria a matriz de adjacência baseado na matriz já pré-criada.


            print(nome + '\n') #Escreva a matriz de adjência num arquivo
            for i in range(0,n):
                for j in range(0,n):
                    arquivo.write("%s" %(m[i][j])+" ")
                    print(m[i][j],end=" ")
                print('\n')
                arquivo.write('\n')

            print("A quantidade de arestas eh " + str(are))

            arquivo.write("A quantidade de arestas eh " + str(are)) #Escreve a quantidade de arestas:
            arquivo.close()

            input("Aperte qualquer tecla para sair:")

            os.system('cls') 

        elif submodo=="b": #Entra em Grafos com classes especiais.
            print("Qual tipo de grafo?\n") #Determina com tipo de Grafo o usuário quer criar

            print("[a]-Grafo Completo\n")

            print("[b]-Grafo Bicompleto\n")

            print("[c]-Grafo estrela\n")

            print("[d]-Caminho\n")

            print("[e]-Ciclo\n")

            print("[f]-Roda\n")

            print("[g]-N-Cubo\n")

            modo_de_grafo=input("opcao:")

            modo_de_grafo.lower()

            if modo_de_grafo=='a': #Cria um Grafo completo
                nome = input("Coloque o nome do grafo: ") #Nome do grafo

                arquivo = open(nome+".txt","w") #Criação de arquivo como nome do grafo + .txt e escreve no arquivo

                arquivo.write(nome+"\n")

                n=int(input("Coloque a quantidade de vertices do grafo: ")) #Cria a matriz

                m=criamatrizquad(n)


                matrizcomp(n,m) #Cria a matriz completa

                print(nome + '\n')
                for i in range(0,n):
                    for j in range(0,n):
                        arquivo.write("%s" %(m[i][j])+" ")
                        print(m[i][j],end=" ")
                    print('\n')
                    arquivo.write('\n')

    
                arquivo.close()

                input("Aperte qualquer tecla para sair:")

                os.system('cls') 



            elif modo_de_grafo =='b': #Cria um Grafo bicompleto
                nome = input("Coloque o nome do grafo: ") #Nome do grafo

                arquivo = open(nome+".txt","w") #Criação de arquivo como nome do grafo + .txt e escreve no arquivo

                arquivo.write(nome+"\n")

                n1= int(input("Coloque a quantidade de vertices do conjunto 1")) # Input para a quantidade de vertices do Conjunto U

                n2 = int(input("Coloque a quantidade de vertices do conjunto 2")) #input para a quantidade de vertices do conjunto V

                n=n1+n2 

                m=criamatrizquad(n) #Cria a matriz

                matrizbicomp(n1,n2,m) #Cria a matriz bicompleta
                
                print(nome + '\n')

                for i in range(0,n):
                    for j in range(0,n):
                        arquivo.write("%s" %(m[i][j])+" ")
                        print(m[i][j],end=" ")
                    print('\n')
                    arquivo.write('\n')

    
                arquivo.close()

                input("Aperte qualquer tecla para sair:")

                os.system('cls')


            elif modo_de_grafo =='c': #Cria um Grafo estrela
                nome = input("Coloque o nome do grafo: ") #Nome do grafo

                arquivo = open(nome+".txt","w") #Criação de arquivo como nome do grafo + .txt e escreve no arquivo

                arquivo.write(nome+"\n")

                n=int(input("Coloque o tamanho dos vertices adjacentes ao vertice central: ")) #Cria a matriz
                n+=1

                m=criamatrizquad(n)

                matrizestr(n,m)

                print(nome + '\n')

                for i in range(0,n):
                    for j in range(0,n):
                        arquivo.write("%s" %(m[i][j])+" ")
                        print(m[i][j],end=" ")
                    print('\n')
                    arquivo.write('\n')

                arquivo.close()

                input("Aperte qualquer tecla para sair:")

                os.system('cls')

            elif modo_de_grafo =='d': #Cria um Caminho
                nome = input("Coloque o nome do grafo: ") #Nome do grafo

                arquivo = open(nome+".txt","w") #Criação de arquivo como nome do grafo + .txt e escreve no arquivo

                arquivo.write(nome+"\n")

                n=int(input("Coloque o tamanho do caminho ")) #Cria a matriz

                m=criamatrizquad(n)

                caminho(n,m)

                print(nome + '\n')
                for i in range(0,n):
                    for j in range(0,n):
                        arquivo.write("%s" %(m[i][j])+" ")
                        print(m[i][j],end=" ")
                    print('\n')
                    arquivo.write('\n')

    
                arquivo.close()

                input("Aperte qualquer tecla para sair:")

                os.system('cls')


            elif modo_de_grafo =='e': #Cria um Ciclo
                nome = input("Coloque o nome do grafo: ") #Nome do grafo

                arquivo = open(nome+".txt","w") #Criação de arquivo como nome do grafo + .txt e escreve no arquivo

                arquivo.write(nome+"\n")

                n=int(input("Coloque o numero de vertices do ciclo: "))

                m=criamatrizquad(n)#Cria a matriz            
    
                ciclo(n,m) #Faz a matriz de Adjacência do ciclo

                print(nome + '\n')

                for i in range(0,n):
                    for j in range(0,n):
                        arquivo.write("%s" %(m[i][j])+" ")
                        print(m[i][j],end=" ")
                    print('\n')
                    arquivo.write('\n')

    
                arquivo.close()

                input("Aperte qualquer tecla para sair:")

                os.system('cls')
                

            elif modo_de_grafo =='f': #Cria uma Roda
                nome = input("Coloque o nome do grafo: ") #Nome do grafo

               

                n=int(input("Coloque a quantidade dos vertices da roda, excluindo o vertice central: ")) #Cria a matriz

                m=criamatrizquad(n+1)


                roda(n,m) #Gera a roda

                
                if(n>=3):
                    arquivo = open(nome+".txt","w") #Criação de arquivo como nome do grafo + .txt e escreve no arquivo

                    arquivo.write(nome+"\n")
                    print(nome + '\n')
                    for i in range(0,n+1):
                        for j in range(0,n+1):
                            arquivo.write("%s" %(m[i][j])+" ")
                            print(m[i][j],end=" ")
                        print('\n')
                        arquivo.write('\n')
                    arquivo.close()

                    input("Aperte qualquer tecla para sair:")

                    os.system('cls')

                else:

                    input("Aperte qualquer tecla para sair:")

                    os.system('cls')

            elif modo_de_grafo =='g':#Cria um NCubo

                nome = input("Coloque o nome do grafo: ") #Nome do grafo

                arquivo = open(nome+".txt","w") #Criação de arquivo como nome do grafo + .txt e escreve no arquivo

                arquivo.write(nome+"\n")

                n=int(input("Coloque a dimensao do cubo: ")) #Cria a matriz

                v=2**n

                m=criamatrizquad(v)

                cubo(n,m)

                print(nome + '\n')
                for i in range(0,n+1):
                    for j in range(0,n+1):
                        arquivo.write("%s" %(m[i][j])+" ")
                        print(m[i][j],end=" ")
                    print('\n')
                    arquivo.write('\n')
                arquivo.close()

                input("Aperte qualquer tecla para sair:")

                os.system('cls')


        elif submodo=="c": #Retorna a tela inicial
            print("BEM VINDO AO PROGRAMA DE GRAFOS. Quer escrever um grafo[a] ou ler um grafo[b] ou sair do programa[c]?\n")
            modo=input("opcao:")

            modo.lower()

            os.system('cls')


    elif modo=='b': #Ler e imprime na tela o Grafo
        nome = input("Coloque o nome do grafo: ")
        if(os.path.isfile(nome+".txt")== True):#imprime se verdadeiro
            arquivo=open(nome+".txt","r")
            line=" "
            while(line!=''):
                line=arquivo.readline()
                print(line)

            arquivo.close()
            print("Escolha uma opcao. Quer escrever um grafo[a], ler mais um grafo[b] ou sair do programa[c]?\n")

            modo=input("opcao:")

            modo.lower()

            os.system('cls')
        else:#
            print("Esse grafo nao existe no programa\n")
            print("Escolha uma opcao. Quer escrever um grafo[a] ou ler um grafo[b] ou sair do programa[c]\n?")
            modo=input("opcao:")
            modo.lower()

            os.system('cls')

            
            

    else:
        print("Esse modo nao existe\n")
        print("Escolha uma opcao. Quer escrever um grafo[a] ou ler um grafo[b] ou sair do programa[c]?")

        modo=input()
        modo.lower()

        os.system('cls')

