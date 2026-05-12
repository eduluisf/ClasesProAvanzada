class Personal_uniguajira:
    def __init__(self,nombre:str,apellidos:str,codigo:int):

        self.nombre=nombre
        self.apellido=apellidos
        self.codigo=codigo
       
    
     

    def presentarse(self):
        print(f"mi nombre es {self.nombre} {self.apellido}")

    # def modificar_nota(self,nota_nueva):
    #     if(self.rol == "Estudiante"):
    #         raise ValueError("Ojo no puedes modificar")
    #     else:
    #         self._nota=nota_nueva

    

        

class Estudiante(Personal_uniguajira):
        def __init__(self,nombre:str,apellidos:str,codigo:int,pregrado:str):
            super().__init__(nombre,apellidos,codigo)
            self.pregrado=pregrado


        def presentarse(self):
             print(f"mi nombre es {self.nombre} {self.apellido} y estudio {self.pregrado}")

        

cristian=Estudiante("Cris","Ceb",123,"IngSis")

cristian.presentarse()
 