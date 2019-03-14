class Nodo:
    def __init__(self, dado=None,ant=None):
        self.dado = dado
        self.ant = ant

    def nodoGet(self):
        return self.dado

    def nodoSet(self, dado):
            self.dado = dado

class Lista:
    def __init__(self):
        self.ultimo = None

    def vazia(self):
        if self.ultimo == None:
            return True
        else:
            return False

    def inserir(self,dado):
        self.ultimo = Nodo(dado,self.ultimo)


    def removeFim(self):
        if self.ultimo == None:
            pass
        aux = self.ultimo
        self.ultimo = aux.ant
"list() = instance created"

#the code below is the answer for one exercise
"""n = int(input())
for x in range(n):
    printed = False
    pilhas = input()
    lista = Lista()
    for y in pilhas:
        if y == '(' or y == '[' or y == '{':
            lista.inserir(y)
        elif y == ']' and lista.ultimo != None and lista.ultimo.dado == '[':
            lista.removeFim()
        elif y == ')' and lista.ultimo != None and lista.ultimo.dado == '(':
            lista.removeFim()
        elif y == '}' and lista.ultimo != None and lista.ultimo.dado == '{':
            lista.removeFim()
        else:
            print('N')
            printed = True
            break

    if not printed:
        if (lista.ultimo == None):
            print('S')
        else:
            print('N')"""