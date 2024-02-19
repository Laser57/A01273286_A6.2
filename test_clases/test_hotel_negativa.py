import unittest
import json
import sys
import os
sys.path.append('/Users/luis/Downloads/A01273286_A6.2-main')
from Hotel.hotel import Hotel
class TestHotel(unittest.TestCase):

    def test_create_hotel_negative_existing_file(self):
        # Crear una instancia de Hotel
        hotel = Hotel(name="ExistingHotel", location="City1", rooms=10)
        hotel.create_hotel()

        # Intentar crear un hotel con el mismo nombre (archivo ya existente)
        with self.assertRaises(FileExistsError):
            hotel.create_hotel()

    def test_delete_hotel_negative_nonexistent_file(self):
        # Crear una instancia de Hotel
        hotel = Hotel(name="NonexistentHotel", location="City2", rooms=15)

        # Intentar eliminar un hotel que no existe (archivo no existente)
        with self.assertRaises(FileNotFoundError):
            hotel.delete_hotel()

if __name__ == '__main__':
    unittest.main()