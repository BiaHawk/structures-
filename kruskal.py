class Grafo: 
  
    def __init__(self,vertices): 
        self.numVertices = vertices 
        self.grafo = [] 


    def inserir(self,u,v,w): 
        self.grafo.append([u,v,w]) 

    def encontrar(self, pai, i): 
        if pai[i] == i: 
            return i 
        return self.encontrar(pai, pai[i]) 
  
    def unir(self, pai, rank, x, y): 
        x = self.encontrar(pai, x) 
        y = self.encontrar(pai, y) 
  
        if rank[x] < rank[y]: 
            pai[x] = y 
        elif rank[x] > rank[y]: 
            pai[y] = x 
        else: 
            pai[y] = x 
            rank[x] += 1

def KruskalMST(self): 

        resultado =[]
        i = 0
        e = 0

        #aqui tem que sortear usando  o w, que é o peso, por isso ele usa a key como item[2]
        self.grafo =  sorted(self.grafo,key=lambda item: item[2]) 
  
        pai = [] ; rank = [] 

        for node in range(self.numVertices): 
            pai.append(node) 
            rank.append(0) 

        while e < self.numVertices -1 : 
  
            u,v,w =  self.grafo[i] 
            i += 1
            
            x = self.encontrar(pai, u) 
            y = self.encontrar(pai ,v) 

            if x != y: 
                e = e + 1     
                resultado.append([u,v,w]) 
                self.unir(pai, rank, x, y)   

        return resultado

