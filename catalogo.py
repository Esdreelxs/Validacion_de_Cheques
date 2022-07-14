class pelicula:
    def _init_(self,titulo,duracion,lanzamiento):
        self.titulo=titulo
        self.duracion=duracion
        self.lanzamiento=lanzamiento
        print("Sea creado la pelicula: "+self.titulo)

    def _str(self):
        return f'{self.titulo} ({self.lanzamiento})'


minions= pelicula("minions",160,2022)
top_gun=pelicula("top gun",160,2022)
print(mi_pelicula.duracion)


class catalogo:
    nombreCatalogo=""
    peliculas=[]
    def _init_(self, nombreCatalogo, peliculas=[]):
        self.nombreCatalogo=nombreCatalogo
        self.peliculas=peliculas

    def agregar(self,pelicula):
        self.peliculas.append(pelicula)
    
    def mostrarNombreCatalogo(self):
        print(self.nombreCatalogo)

    def mostrar(self):
        for p in self.peliculas:
            print(p)

Catalogo= catalogo("peliculas_nuevas",[minions,top_gun])
Catalogo.mostrar()

Catalogo_2=catalogo("peliculas_nuevas",[])
Catalogo_2.mostrar()
#-----------------------------------------------------------------------------------------------------------------

class Ejemplo:
    def __metodo_privado_(self):
        print("Soy un metodo inancansable desde fuera.")

e=Ejemplo()
e.__metodo_privado_()