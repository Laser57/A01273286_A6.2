'''
Codigo realizado para realizado para gestionar 
las diferentes reservas que un usuario puede
realizar en un hotel.
Escribira en archivos json las reservas para
su almacenamiento
LUIS ALFONSO SABANERO ESQUIVEL A01273286
Febrero 2024
'''
import json
import time
import os


class Reservation:
    '''
    clase Reservation:
    metodos
    a. Create a Reservation (Customer, Hotel)
    b. Cancel a Reservation
    '''
    # pylint: disable=too-many-arguments
    def __init__(self, reservation_id, customer, hotel, check_in, check_out):
        '''
         Constructor para instanciar los atributos de una reserva
        '''
        self.reservation_id = str(reservation_id)+str(int(time.time()))
        self.customer = customer
        self.hotel = hotel
        self.check_in = check_in
        self.check_out = check_out

    def create_reservation(self):
        '''
          Implementación para crear una nueva reserva
          guardaremos en un archivo json
        '''
        self.save_to_file()

    def cancel_reservation(self):
        '''
          Implementación para borrar una reserva
          guardaremos en un archivo json
        '''
        archivo_path = f"reservation_{self.reservation_id}_data.json"
        if os.path.exists(archivo_path):
            os.remove(archivo_path)
        print("No se encontró ninguna reserva.")

    def save_to_file(self):
        '''
          Implementación para guardar los datos
          en un archivo json
        '''
        data = {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer.customer_id,
            "hotel_name": self.hotel.name,
            "check_in": self.check_in,
            "check_out": self.check_out
        }
        with open(f"reservation_{self.reservation_id}_data.json", "w",
                  encoding='utf-8') as file:
            json.dump(data, file)

    @classmethod
    def load_from_file_reservation(cls, reservation_name):
        '''
        Optionalmente podemos leer un archivo del directorio
        '''
        nombre = f"reservation_{reservation_name.customer_id}_data.json"
        if os.path.exists(nombre):
            with open(nombre, "r",
                      encoding='utf-8') as file:
                reservations_data = json.load(file)

        if reservations_data is not None:
            print("Reservations:")
            print(f"Hotel: {reservations_data['hotel_name']}")
            print(f"Customer: {reservations_data['customer_id']}")
            print(f"Check-in: {reservations_data['check_in']}")
            print(f"Check-out: {reservations_data['check_out']}")
