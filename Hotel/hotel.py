'''
Codigo realizado para determinar poder gestionar la clase hotel
con los siguientes clases reservation y customer.
importante esta clase requiere que los modulos de python
se carguen con sys.path
Escribira en archivos json las reservas para
su almacenamiento
LUIS ALFONSO SABANERO ESQUIVEL A01273286
Febrero 2024
'''
import sys
import json
import os
# pylint: disable=E0401
# pylint: disable=C0413
sys.path.append('/Users/luissabaneroesquivel/Downloads/A01273286_A6.2-MAIN')
from Reservation.reservation import Reservation # noqa


class Hotel:
    '''
    Clase hotel
    metodos:
    a. Create Hotel
    b. Delete Hotel
    c. Display Hotel information
    d. Modify Hotel Information
    e. Reserve a Room
    f. Cancel a Reservation
    '''
    def __init__(self, name, location, rooms):
        '''
        Constructor para instanciar los 3 atributos de hotel
        '''
        self.name = name
        self.location = location
        self.rooms = rooms
        self.reservations = []

    def create_hotel(self):
        '''
          Implementación para crear un nuevo cliente
        '''
        archivo_path = f"{self.name.lower().replace(' ', '_')}_data.json"
        if os.path.exists(archivo_path):
            raise FileExistsError("El archivo para el hotel ya existe.")
        self.save_to_file()

    def delete_hotel(self):
        '''
        Implementación para eliminar un cliente
        usa la misma funcion dado que sobreescribe el contenido
        '''
        archivo_path = f"{self.name}_data.json"
        if os.path.exists(archivo_path):
            os.remove(archivo_path)
            print("Hotel eliminado.")
        else:
            raise FileNotFoundError("No se encontró ningún hotel.")

    def modify_information(self, new_name=None,
                           new_location=None, new_rooms=None):
        '''
        Modifica la información del hotel con los
        nuevos valores proporcionados.
        '''
        if new_name:
            self.name = new_name

        if new_location:
            self.location = new_location

        if new_rooms is not None:
            self.rooms = new_rooms

        self.save_to_file()  # Guardar en un archivo después de cada cambio
        print("Información del hotel modificada exitosamente.")
        self.display_information()

    def create_reservation(self, customer, check_in, check_out):
        '''
        Crea una reservacion asegurandose que
        exista espacio y crea un objeto del tipo reservacion
        '''
        if self.rooms > 0:
            reservation_id = len(self.reservations) + 1
            reservation = Reservation(reservation_id, customer,
                                      self, check_in, check_out)
            reservation.create_reservation()
            self.reservations.append(reservation)
            self.rooms -= 1
            self.save_to_file()
            print(f"Reserva creada en {self.name}.")
            print("Datos de la reservacion nuevos:")
            customer.display_information()
        else:
            print(f"No hay habitaciones disponibles {self.name}")

    def cancel_reservation(self, customer):
        '''
        En caso de borrar una reservacion liberamos
        el numero disponible de habitaciones
        '''
        archivo_path = f"reservation_{customer}_data.json"
        if os.path.exists(archivo_path):
            os.remove(archivo_path)
        print(f"No se encontró ninguna reserva para {customer}.")

    def display_information(self):
        '''
        Funcion usada para desplegar informacion del hotel
        unicamente usamos print de los atributos de la clase
        '''
        print(f"Hotel: {self.name}")
        print(f"Location: {self.location}")
        print(f"Available rooms: {self.rooms}")

    def save_to_file(self):
        '''
        Guardamos los datos en un archivo json unico
        con el nombre del hotel
        '''
        data = {
            "name": self.name,
            "location": self.location,
            "rooms": self.rooms,
        }
        with open(f"{self.name.lower().replace(' ', '_')}_data.json", "w",
                  encoding='utf-8') as file:
            json.dump(data, file)

    @classmethod
    def load_from_file(cls, hotel_name):
        '''
        Optionalmente podemos leer un archivo del directorio
        '''
        with open(f"{hotel_name.lower().replace(' ', '_')}_data.json", "r",
                  encoding='utf-8') as file:
            data = json.load(file)
        return cls(name=data["name"],
                   location=data["location"],
                   rooms=data["rooms"])
