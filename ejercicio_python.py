class Pais:
    def __init__(self, nombre, capital, poblacion):
        self.nombre = nombre
        self.capital = capital
        self.poblacion = poblacion
        self.limitrofes = []

    def agregar_limitrofe(self, pais):
        if pais not in self.limitrofes:
            self.limitrofes.append(pais)
            pais.agregar_limitrofe(self)

    def obtener_limitrofes(self):
        return self.limitrofes

class ColeccionPaises:
    def __init__(self):
        self.paises = []

    def agregar_pais(self, pais):
        if pais not in self.paises: #Al pais A se le agrega B
            self.paises.append(pais) #Al pais B se le agrega A

    def buscar_pais(self, nombre):
        for pais in self.paises:
            if pais.nombre == nombre:
                return pais
        return None

    def mostrar_paises(self):
        for pais in self.paises:
            print(pais.nombre)

# Ejemplo de uso del programa

# Crear algunos países
argentina = Pais("Argentina", "Buenos Aires", 44938712)
uruguay = Pais("Uruguay", "Montevideo", 3461734)
chile = Pais("Chile", "Santiago", 19107216)
bolivia = Pais("Bolivia", "La Paz", 11673021)

# Crear una colección de países y agregar los países creados anteriormente
paises = ColeccionPaises()
paises.agregar_pais(argentina)
paises.agregar_pais(uruguay)
paises.agregar_pais(chile)
paises.agregar_pais(bolivia)

# Agregar los países limitrofes a Argentina
argentina.agregar_limitrofe(uruguay)
argentina.agregar_limitrofe(chile)
argentina.agregar_limitrofe(bolivia)

# Agregar los países limitrofes a Uruguay
uruguay.agregar_limitrofe(argentina)

# Obtener los países limitrofes de Argentina y mostrarlos
limitrofes_argentina = argentina.obtener_limitrofes()
print("Los países limitrofes de Argentina son:")
for pais in limitrofes_argentina:
    print(pais.nombre)

# Obtener los países limitrofes de Uruguay y mostrarlos
limitrofes_uruguay = uruguay.obtener_limitrofes()
print("Los países limitrofes de Uruguay son:")
for pais in limitrofes_uruguay:
    print(pais.nombre)

# Mostrar todos los países
print("Todos los países cargados en el sistema:")
paises.mostrar_paises()

print('este es el nombre ' + argentina.nombre)
print('esta es la capital ' + argentina.capital)
print('esta es la poblacion ' + str(argentina.poblacion))