


#Crear un objetos o instanciar la clase 
print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
coche1.getInfo()

#Crear otro objeto e imprimir valores
print("Objeto 2")
coche2=Coches("Azul","Nissan","2020",180.150,6)
coche2.getInfo()

#Crear los objetos o instancias de las clases camiones y camioneta
print("Objeto 3")
camion1=Camiones("Negro","Dina","2020",180,300,12,8,2500)
print(f"Marca: {camion1.getMarca()} {camion1.getColor()}, numeros de plazas: {camion1.getplazas()} \nModelo: {camion1.getModelo()} 
con una velocidad de {self.getVelocidad()} km/h, una potencia de {self.getCaballaje} hp, con {self.getEje()} ejes de carga ")