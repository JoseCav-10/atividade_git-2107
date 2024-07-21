class Felino():
    def __init__(self, peso, tamanho, habitat):
        self.__id = None
        self.peso = peso
        self.tamanho = tamanho
        self._habitat = habitat

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

a=Felino(18, 165, "amazônia")
a.setId(2)
print(a.getId())