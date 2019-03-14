class Nodo:
    def __init__(self, dado = None, prox = None, anterior = None):
        self.dado = dado
        self.prox = prox
        self.anterior = anterior

class Lista:
    
    def __init__(self):
        self.primeiro = self.ultimo = Nodo()

    def vazia(self):
        return self.primeiro.dado == self.ultimo.dado

    
    def pesquisar(self, dado):
        if self.vazia(): return None
        
        auxiliar = self.primeiro.prox
        while auxiliar.prox != None and auxiliar.dado != dado:
                auxiliar = auxiliar.prox

        if auxiliar.dado == dado:
            return auxiliar.dado

        return None
        
    def append(self, dado):
        self.ultimo.prox = Nodo(dado = dado, prox = None, anterior = self.ultimo)
        self.ultimo = self.ultimo.prox


    def __str__(self):
        
        if self.vazia():
            return ""

        aux = self.primeiro
        formato = ""
        
        while aux.prox != None:
            if aux.dado!= None:
                formato += str(aux.dado) + " "
            aux = aux.prox
        formato += str(aux.dado) + ""
        
        return formato

    def remove(self, dado):
        if self.vazia(): return None

        auxiliar = self.primeiro.prox

        while auxiliar != None and auxiliar.dado != dado:
            auxiliar = auxiliar.prox

        if auxiliar == None: return None
        else:
            item = auxiliar.dado

            if auxiliar.anterior != None:
                auxiliar.anterior.prox = auxiliar.prox
            if auxiliar.prox != None:
                auxiliar.prox.anterior = auxiliar.anterior

        if self.vazia(): self.ultimo = self.primeiro = Nodo()
        elif auxiliar.prox == None: self.ultimo = auxiliar.anterior

        del auxiliar
        return item
            

#The Code below is a URI question solution
"""lista = Lista()
n = int(input())
for x in input().split():
    lista.append(x)
y = int(input())
sairam = input().split()
for x in range(y):
    lista.remove(sairam[x])

print(lista)""




