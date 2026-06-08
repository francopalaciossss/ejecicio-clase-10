#Adapter

class ImpresoraAntigua:
    def imprimir_documento(self):
        print("Imprimiendo documento...")


class AdaptadorImpresora:
    def __init__(self, impresora):
        self.impresora = impresora

    def imprimir(self):
        self.impresora.imprimir_documento()


impresora_vieja = ImpresoraAntigua()
adaptador = AdaptadorImpresora(impresora_vieja)

adaptador.imprimir()


#salida: Imprimiendo documento...

#Observer

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, noticia):
        print(f"{self.nombre} recibió: {noticia}")


class Diario:
    def __init__(self):
        self.suscriptores = []

    def suscribir(self, usuario):
        self.suscriptores.append(usuario)

    def publicar(self, noticia):
        print(f"\nNueva noticia: {noticia}")

        for usuario in self.suscriptores:
            usuario.actualizar(noticia)


u1 = Usuario("Juan")
u2 = Usuario("María")

diario = Diario()

diario.suscribir(u1)
diario.suscribir(u2)

diario.publicar("Argentina ganó el Mundial")

#salida:
#Nueva noticia: Argentina ganó el Mundial
#Juan recibió: Argentina ganó el Mundial
#María recibió: Argentina ganó el Mundial

#Factory method

class Auto:
    def mostrar(self):
        print("Se creó un Auto")

class Moto:
    def mostrar(self):
        print("Se creó una Moto")

class FabricaVehiculos:
    def crear_vehiculo(self, tipo):
        if tipo == "auto":
            return Auto()
        elif tipo == "moto":
            return Moto()

fabrica = FabricaVehiculos()

vehiculo1 = fabrica.crear_vehiculo("auto")
vehiculo2 = fabrica.crear_vehiculo("moto")

vehiculo1.mostrar()
vehiculo2.mostrar()

#salida:
#Se creó un Auto
#Se creó una Moto