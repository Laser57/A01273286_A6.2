import unittest
import sys
import os
from unittest.mock import patch
sys.path.append('/Users/luis/Downloads/A01273286_A6.2-main')
from Reservation.reservation import Reservation
from Hotel.hotel import Hotel
from Customer.customer import Customer

class TestReservation(unittest.TestCase):

    def test_create_reservation(self):
        # Crear una instancia de Hotel para la reserva
        hotel = Hotel(name="Hotel1", location="City1", rooms=10)
        with self.assertRaises(FileExistsError):
            hotel.create_hotel()
        # Crear una instancia de Customer para la reserva
        customer = Customer(customer_id="1", name="John Doe", email="john@example.com", phone="123456789")
        with self.assertRaises(FileExistsError):
            customer.create_customer()

        # Crear una reserva
        reservation = Reservation(reservation_id="1", customer=customer, hotel=hotel, check_in="2024-02-18", check_out="2024-02-20")
        reservation.create_reservation()
        reservation_file_path = f"reservation_{customer.customer_id.lower().replace(' ', '_')}_data.json"
        self.assertTrue(os.path.exists(reservation_file_path))  # Asegurarse de que el archivo exista

    def test_cancel_reservation(self):
        # Crear una instancia de Hotel para la reserva
        hotel = Hotel(name="Hotel2", location="City2", rooms=15)
        hotel.create_hotel()

        # Crear una instancia de Customer para la reserva
        customer = Customer(customer_id="2", name="Jane Doe", email="jane@example.com", phone="987654321")
        customer.create_customer()

        # Crear una reserva
        reservation = Reservation(reservation_id="2", customer=customer, hotel=hotel, check_in="2024-02-21", check_out="2024-02-23")
        reservation.create_reservation()

        # Llamar a cancel_reservation y verificar que el archivo ya no existe después de llamar al método
        reservation.cancel_reservation()
        reservation_file_path = f"reservation_{customer.customer_id.lower().replace(' ', '_')}_data.json"
        self.assertFalse(os.path.exists(reservation_file_path))  # Asegurarse de que el archivo ya no exista

if __name__ == '__main__':
    unittest.main()
