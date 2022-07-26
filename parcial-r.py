from lista import Lista
from jurassic_park import dinosaurs
from cola import Cola

class Dinosaurios:
    
    def __init__(self, time, zone_code, dino_number, alert_level, name, type, number, period, named_by):
        self.name = name
        self.type = type
        self.number = number
        self.period = period
        self.named_by = named_by
        self.time = time
        self.zone_code = zone_code
        self.dino_number = dino_number
        self.alert_level = alert_level
      
    def __str__(self):
        return f"{self.name} - {self.type} - {self.number} - {self.period} - {self.named_by} - {self.time} - {self.zone_code} - {self.dino_number} - {self.alert_level}"

lista_dinosaurs = Lista()
lista_dinosaurs2=Lista()

archivo = open("C:/Users/54344/Documents/facu/Uader 3er año cursado/algoritmo y estructura de datos/Lista/alerts.txt")

lineas = archivo.readlines()
lineas.pop(0)

def busqueda(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino["number"]):
            return dino["name"]


def busqueda1(buscado):
    for dino in dinosaurs:
        if(buscado == dino["name"]):
            return dino["type"]

def busqueda2(buscado):
    for dino in dinosaurs:
        if(buscado == dino["name"]):
            return dino["number"] 

def busqueda3(buscado):
    for dino in dinosaurs:
        if(buscado == dino["name"]):
            return dino["period"] 

def busqueda4(buscado):
    for dino in dinosaurs:
        if(buscado == dino["name"]):
            return dino["named_by"]         


for linea in lineas:
    dato = linea.split(';')
    dato[3] = dato[3][:-1]
    dato.append(busqueda(dato[2]))
    dato.append(busqueda1(dato[4]))
    dato.append(busqueda2(dato[4]))
    dato.append(busqueda3(dato[4]))
    dato.append(busqueda4(dato[4]))
    lista_dinosaurs.insertar(Dinosaurios(dato[0],
                                        dato[1],
                                        dato[2],
                                        dato[3],
                                        dato[4],
                                        dato[5],
                                        dato[6],
                                        dato[7],
                                        dato[8]),"name")
    lista_dinosaurs2.insertar(Dinosaurios(dato[0],              #ordenamiento para time
                                        dato[1],
                                        dato[2],
                                        dato[3],
                                        dato[4],
                                        dato[5],
                                        dato[6],
                                        dato[7],
                                        dato[8]),"time")

#datos a eliminar
dato_eliminar = lista_dinosaurs.eliminar("WYG075","zone_code")
dato_eliminar1 = lista_dinosaurs.eliminar("SXH966","zone_code")
dato_eliminar2 = lista_dinosaurs.eliminar("LYF010","zone_code")



dato_modificar = lista_dinosaurs.busqueda("HYD195", "zone_code")

if dato_modificar:
    dato_modificar.info.name = "Mosasaurus."

cola_dinosaurios = Cola()
cola_carnivoros = Cola()
cola_hervivoros = Cola()

for i in range(lista_dinosaurs.tamanio()):
    x = lista_dinosaurs.obtener_elemento(i)
    cola_dinosaurios.arribo(x)
    if (x.alert_level == "high" or x.alert_level == "critical"):
        if (x.type == "carnívoro "):
            cola_carnivoros.arribo(x)
        else:
            if (x.type == "herbívoro "):
                cola_hervivoros.arribo(x)


#print cola carnivoros
for i in range(cola_carnivoros.tamanio()):
    x = cola_carnivoros.mover_al_final()
    #print(x)

print()

#print cola herviboros
for i in range(cola_hervivoros.tamanio()):
    x = cola_hervivoros.mover_al_final()
    #print(x)

print()

#eliminar de la cola el codigo EPC944
cola_dinosaurios.arribo("EPC944")


for i in range(cola_dinosaurios.tamanio()):
    x = cola_dinosaurios.mover_al_final()
    #print(x)



#barridos
print("barrido ordenado por nombres")
lista_dinosaurs.barrido()
print()
print("barrido ordenado por time")
lista_dinosaurs2.barrido()
print()
print("barrido dinosaurios Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con nivel  ́critical’ o ‘high’")
lista_dinosaurs.barrido_dinosaurios_filtrado()
print()
print("barrido raptors y cangotauros")
lista_dinosaurs.barrido_dinosaurios_raptors()
print()
print("barrido zone_code de dinosaurios Compsognathus")
lista_dinosaurs.barrido_codigo_Compsognathus()
print()
