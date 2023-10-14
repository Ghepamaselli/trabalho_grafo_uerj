def MatrizAdj(m,n):#Faz um grafo nao direcionado e retorna o numero de arestas utilizadas
    are=0
    for i in range(0,n):
        for j in range(i,n):

            print('O vertice' , i+1,'eh adjacente ao vertice',j+1,'(s/n)')

            eh_adjacente = input()

            eh_adjacente.lower()

            if eh_adjacente == "s" or eh_adjacente == "sim":

                if i!=j:

                    m[j][i] = 1

                    m[i][j] = 1

                    are+=1

                else:

                    print("infelizmente essa operação não é suportada pelo nosso programa")

    return are

def matrizcomp(n,m): #determina a matriz adjacência de uma grafo completo de n vertices qualquer.
    for i in range(0,n):
        for j in range(i,n):
            if i!=j:
                m[j][i] = 1
                m[i][j] = 1
    return



def caminho(n,m): #determina a matriz adjacência de um caminho qualquer de n vertices.
    cont=0
    for i in range(0,n-1):
        for j in range(i,n-1):
            if cont==0:
                m[i][j+1] = 1
                m[i+1][j] = 1
                cont+=1
        cont=0
    return

def matrizbicomp(n1,n2,m):
    n=n1+n2
    cont=0
    arestas = n1*n2
    for i in range(0,n):
        for j in range(i,n):
            if j>n1-1 and arestas>0:
                m[i][j] = 1
                m[j][i] = 1
                arestas-=1
                
    return

def matrizestr(n,m):
    for i in range(0,n):
        for j in range(i,n):
            if i==0 and i!=j:
               m[i][j] = 1
               m[j][i] = 1
    return



def ciclo(n,m): #determina a matriz adjacência de um clico qualquer de n vertices.
    cont=0
    for i in range(0,n-1):
        for j in range(i,n-1):
            if cont==0 and i==0:
                 m[i][j+1] = 1

                 m[i+1][j] = 1

                 m[i][n-1] = 1

                 m[n-1][j] = 1

                 cont+=1

            elif cont==0:
                m[i][j+1] = 1
                m[i+1][j] = 1
                cont+=1
        cont=0
    return

def roda(n,m): #Determina a matriz adjacência de uma roda qualquer
    if(n<3):
       print("Isso nao eh uma roda")
       return
    else:
        cont=0
        for i in range(0,n):
            for j in range(i,n):
                if i==0:
                    m[i][j+1]=1
                    m[j+1][i]=1
                elif cont<1 and i==1 and j==1:
                    m[i][j+1]=1
                    m[i][j+(n-1)]=1
                    m[j+1][i]=1
                    m[j+(n-1)][i]=1
                    cont+=1
                elif cont<1:
                    m[i][j+1]=1
                    m[j+1][i]=1
                    cont+=1
            cont=0
    return

def cubo(n,m):
    cont=0
    v=2**n
    ContrlArestas=v-3
    for i in range(0,v-1):
        for j in range(i,v-1):
            if i==0 and cont<1: #Serve quando a linha eh 1
                m[i][j+1]=1
                m[j+1][i]=1 #determina a aresta mais proxima
                cont+=1 
                if n>2: #determina as arestas a partir de um cubo maior que n>2
                    for k in range(1,n): 
                        if cont<n-1:
                            m[i][i+(k*n)]=1
                            m[i+(k*n)][i]=1
                            cont+=1
                    m[i][v-1]=1
                    m[v-1][i]=1
           
                    
            elif cont<1 and i<v-1:
                if  i==(v//2)-1: #caso especial onde eh apenas necessário adicionar uma aresta a mais. Este caso sempre eh v//2-1
                    m[i][j+1]=1
                    m[j+1][i]=1
                    cont+=1
                else:
                    m[i][j+1]=1
                    m[j+1][i]=1
                    cont+=1
                    if i<(v//2)-1: #determina as arestas para os vertices menores que v//2-1
                            m[i][v-i-1]=1
                            m[v-i-1][i]=1
                            if n>3:
                                m[v//2-(1+(i-1))][i]=1
                                m[i][v//2-(1+(i-1))]=1
                            
                                                 
                    elif i==(v//2): #determina para o vertices v//2 sua arestas
                        m[i][v-1]=1
                        m[v-1][i]=1
                
        cont=0

    return

def criamatrizquad(n): #criamatriz
    m=[]
    for i in range(0,n):
        t = []
        for i in range(0,n):
            t.append(0)
        m.append(t)
    return m

