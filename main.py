# Bautista Santos Tapia
# 45 686 196
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


A)  Al presionar el botón 'Agregar' se deberan cargar tantos vehiculos como el usuario desee. 
    Los datos a cargar de cada vehiculo son: tipo de vehiculo (auto, camioneta, moto) y kilometros*.

* Todos los autos son usados.

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar todos los vehiculos ingresados con su correspondiente kilometraje y su posicion en la lista.
Ejemplo: 1 - Auto - 1000 km
         2 - Camioneta - 2000 km
         etc..

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)     (6)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5).            (9 - 6 = 3)
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al presionar el boton Informar 
    0- El mayor kilometraje y su tipo de vehiculo.
    1- El menor kilometraje y su tipo de vehiculo.
    2- Kilometraje promedio de los autos.
    3- Precio promedios de todos los servicios.
    4- Informar los kilometrajes que superan el promedio (total).
    5- Informar los kilometrajes que NO superan el promedio (total).
    6- Informar la cantidad de vehiculos de cada tipo.
    7- Informar el precio promedio de los servicios cuyo kilometraje es mayor a 10000 kms.
    8- Indicar el mayor de los promedios de kilometros por tipo de vehiculo.
    9- Informar el monto promedio de cada servicio realizado.


Los montos de los servicios son:
    - Auto: $15000
    - Camioneta: $25000
    - Moto: $10000
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")
        
        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_tipo_vehiculo = []#"MOTO", "MOTO", "AUTO", "MOTO"
        self.lista_kilometros_vehiculo = []#12, 13, 14, 15

    def btn_agregar_on_click(self):
        while True:

            tipo = prompt("examen", "seleccones el tipo de vehiculo (auto, camioneta, moto)")  
            tipo = tipo.upper()
            while tipo == None or (tipo != "AUTO" and tipo != "CAMIONETA" and tipo != "MOTO"):
                tipo = prompt("examen", "Ingrese el tipo correctamente (auto / camioneta / moto)")
                tipo = tipo.upper()


            kilometros = prompt("examen", "selecciones los kilometros")
            while kilometros == None or not kilometros.isdigit() or int(kilometros) < 1:
                kilometros = prompt("examen", "selecciones los kilometros correctamente")
            kilometros = int(kilometros)

            self.lista_tipo_vehiculo.append(tipo)
            self.lista_kilometros_vehiculo.append(kilometros)

            respuesta = question("examen", "quiere seguir subiendo datos?")
            if respuesta == False:
                break

    
    def btn_mostrar_on_click(self):
        for i, tipo in enumerate(self.lista_tipo_vehiculo):
            print(f"{i} - {self.lista_tipo_vehiculo[i]} - {self.lista_kilometros_vehiculo[i]} km")


    def btn_informar_on_click(self):
    #6- Informar la cantidad de vehiculos de cada tipo.
        contador_auto = 0
        contador_camioneta = 0
        contador_moto = 0
        for i, tipo in enumerate(self.lista_tipo_vehiculo):
            if tipo == "AUTO":
                contador_auto += 1
            elif tipo == "CAMIONETA":
                contador_camioneta += 1
            elif tipo == "MOTO":
                contador_moto += 1

        print(f"La cantidad de autos es de {contador_auto}, de motos es de {contador_moto} y de camionetas es de {contador_camioneta}")
    
    #3- Precio promedios de todos los servicios.

        # Los montos de los servicios son:
            #   - Auto: $15000
            #   - Camioneta: $25000
            #  - Moto: $10000
       
        precio_autos = 0
        precio_autos = contador_auto * 15000

        precio_camioneta = 0
        precio_camioneta = contador_camioneta * 25000

        precio_motos = 0
        precio_motos = contador_moto * 10000

        suma_precios = precio_motos + precio_autos + precio_camioneta
        cantidad_contadores = contador_auto + contador_camioneta + contador_moto

        if cantidad_contadores > 0:
            promedio_precios = suma_precios / cantidad_contadores
            print(f"El promedio de precios es de: ${promedio_precios}")
        else:
            print("No hay vehiculos ingresados")


if __name__ == "__main__":
    app = App()
    app.geometry("200x400")
    app.mainloop()