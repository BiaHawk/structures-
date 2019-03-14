class Grafo:
    def __init__(self,V):
        self.V = V
        self.adj = []

        for i in range(V):
            self.adj.append([])


    def inserir(self,u,v):
        if u not in self.adj[v]:
            self.adj[v].append(u)
        if v not in self.adj[u]:
            self.adj[u].append(v)


    def buscaProfundidade(self, origem):
        marcado = [False] * self.V
        antecessor = ['Source'] * self.V
        flag = False
        
        for v in range(len(self.adj)):
            if not flag:
                v = origem
                flag = True
                
            if not marcado[v]:
                self.__bfs(v,antecessor,marcado)
        
        print(antecessor)
        return antecessor

    def __bfs(self,v,antecessor,marcado):
        marcado[v] = True
        for u in self.adj[v]:
            if not marcado[u]:
                antecessor[u] = v
                self.__bfs(u,antecessor,marcado)

    def caminho_curto(self,u,v,antecessores):
        caminho = []
        caminho.append(v)
        i = v
        while i != "Source" and i != u:
            caminho.append(antecessores[i])
            i = antecessores[i]
            
        if i == "Source":
            print("There is no way between {} and {}".format(u,v))
        else:
            return len(caminho) 

        
    "Recursive funct. For, checking all adjacent of a vertex"
