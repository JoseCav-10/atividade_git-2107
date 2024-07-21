from classe import Felino

class Jaguatirica(Felino):
    def __init__(self, peso, tamanho, habitat, cor):
        super().__init__(peso, tamanho, habitat)
        self.cor = cor

    def cacar(self):
        print("A jaguatirica está caçando!")


class Onca(Felino):
    def __init__(self, peso, tamanho, habitat, pelagem):
        super().__init__(peso, tamanho, habitat)
        self.pelagem = pelagem

    def andar(self):
        print("Onça está em movimento!!")

jaguatirica1 = Jaguatirica(13, 65, "Amazonia", "Rajado")
print("Instanciando a jaguatirica")
jaguatirica1.setId(1)
print("Id da jaguatirica ", jaguatirica1.getId())

onca1 = Onca(200, 125, "Amazonia", "Preta")
print("Instanciando a onça")
onca1.setId(54)
print("Id da onça ", onca1.getId())

    