import unittest
import json
from io import StringIO
import sys
import os
sys.path.append('/Users/luis/Downloads/A01273286_A6.2-main')

from Hotel.hotel import Hotel
from Reservation.reservation import Reservation
from Customer.customer import Customer

class TestHotel(unittest.TestCase):

    def test_create_hotel(self):
        hotel = Hotel(name="Hotel1", location="City1", rooms=10)
        hotel.create_hotel()
        self.assertTrue(os.path.exists("hotel1_data.json"))

    def test_delete_hotel(self):
        hotel = Hotel(name="Hotel2", location="City2", rooms=15)
        with self.assertRaises(FileNotFoundError):
            hotel.delete_hotel()

    def test_create_reservation(self):
        hotel = Hotel(name="Hotel3", location="City3", rooms=5)
        customer = Customer(customer_id="1", name="Customer1", email="customer1@example.com", phone="123456789")
        check_in = "2024-02-18"
        check_out = "2024-02-20"
        hotel.create_reservation(customer, check_in, check_out)
        reservation_file_path = f"reservation_{customer.customer_id.lower().replace(' ', '_')}_data.json"
        self.assertTrue(os.path.exists(reservation_file_path))

    def test_cancel_reservation(self):
        hotel = Hotel(name="Hotel4", location="City4", rooms=8)
        customer = Customer(customer_id="2", name="Customer2", email="customer2@example.com", phone="987654321")
        hotel.create_reservation(customer, "2024-02-21", "2024-02-23")
        hotel.cancel_reservation(customer)
        reservation_file_path = f"reservation_{customer.customer_id.lower().replace(' ', '_')}_data.json"
        self.assertFalse(os.path.exists(reservation_file_path))

    def test_display_information(self):
        hotel = Hotel(name="Hotel5", location="City5", rooms=12)

        # Capturamos la salida estándar para asertar sobre ella
        with StringIO() as captured_output:
            sys.stdout = captured_output
            hotel.display_information()
            sys.stdout = sys.__stdout__  # Restauramos la salida estándar

            # Aserciones sobre la salida capturada
            output = captured_output.getvalue().strip()
            self.assertIn("Hotel: Hotel5", output)
            self.assertIn("Location: City5", output)
            self.assertIn("Available rooms: 12", output)

# Los casos de prueba para Reservation y Customer continúan de manera similar

if __name__ == '__main__':
    unittest.main()
