'''
Codigo realizado para gestionar el alta de nuevos
clientes en el hotel, se requiere:
nombre, correo y telefono
No requiere heredar nada de otras clases
Escribira en archivos json las reservas para
su almacenamiento
LUIS ALFONSO SABANERO ESQUIVEL A01273286
Febrero 2024
'''
import json
import time
import os


class Customer:
    '''
    Clase customer
    metodos:
    a. Create Customer
    b. Delete a Customer
    c. Display Customer Information
    d. Modify Customer Information
    '''
    def __init__(self, customer_id, name, email, phone):
        '''
        Constructor para instanciar los atributos de customer
        Generamos timestamp por cliente para prevenir duplicados
        '''
        self.customer_id = str(customer_id)+str(int(time.time()))
        self.name = name
        self.email = email
        self.phone = phone

    def create_customer(self):
        '''
        Implementación para crear un nuevo cliente
        guardamos el archivo en un .json
        '''
        archivo_path = f"customer_{self.customer_id}_data.json"
        if os.path.exists(archivo_path):
            raise FileExistsError("El archivo para el cliente ya existe.")
        self.save_to_file()

    def delete_customer(self):
        '''
        Implementación para eliminar un cliente
        sobre escribimos el archivo
        '''
        archivo_path = f"customer_{self.customer_id}_data.json"
        if os.path.exists(archivo_path):
            os.remove(archivo_path)
        else:
            raise FileNotFoundError("No se encontró ningún cliente.")

    def display_information(self):
        '''
        Mostamos la informacion del cliente
        '''
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        reservations_data = self.load_from_file_reservation(self.customer_id)
        if reservations_data is not None:
            print("Reservations:")
            print(f"Hotel: {reservations_data['hotel_name']}")
            print(f"Customer: {reservations_data['customer_id']}")
            print(f"Check-in: {reservations_data['check_in']}")
            print(f"Check-out: {reservations_data['check_out']}")

    def modify_information(self, name=None, email=None, phone=None):
        '''
        Implementación para modificar la información del cliente
        '''
        archivo_path = f"customer_{self.customer_id}_data.json"
        if os.path.exists(archivo_path):
            if name is not None:
                self.name = name
            if email is not None:
                self.email = email
            if phone is not None:
                self.phone = phone
            self.save_to_file()
        else:
            raise FileNotFoundError("No se encontró cliente.")

    def save_to_file(self):
        '''
        Guardamos los datos en un archivo json unico
        con el nombre del cliente
        '''
        data = {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }
        with open(f"customer_{self.customer_id}_data.json", "w",
                  encoding='utf-8') as file:
            json.dump(data, file)

    @classmethod
    def load_from_file(cls, customer_id):
        '''
        Optionalmente podemos leer un archivo del directorio
        '''
        with open(f"customer_{customer_id}_data.json", "r",
                  encoding='utf-8') as file:
            data = json.load(file)
        return cls(customer_id=data["customer_id"],
                   name=data["name"],
                   email=data["email"],
                   phone=data["phone"])

    @classmethod
    def load_from_file_reservation(cls, reservation_name):
        '''
        Optionalmente podemos leer un archivo del directorio
        '''
        data = None
        nombre = f"reservation_{reservation_name}_data.json"
        if os.path.exists(nombre):
            with open(nombre, "r",
                      encoding='utf-8') as file:
                data = json.load(file)
        return data
