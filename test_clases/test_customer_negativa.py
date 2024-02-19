import unittest
import json
import sys
import os
sys.path.append('/Users/luis/Downloads/A01273286_A6.2-main')
from Customer.customer import Customer
class TestCustomer(unittest.TestCase):

    def test_create_customer_negative_existing_file(self):
        # Crear una instancia de Customer
        customer = Customer(customer_id="1", name="John Doe", email="john@example.com", phone="123456789")
        # Intentar crear un cliente con el mismo ID (archivo ya existente)
        with self.assertRaises(FileExistsError):
            customer.create_customer()

    def test_delete_customer_negative_nonexistent_file(self):
        # Crear una instancia de Customer
        customer = Customer(customer_id="2", name="Jane Doe", email="jane@example.com", phone="987654321")

        # Intentar eliminar un cliente que no existe (archivo no existente)
        with self.assertRaises(FileNotFoundError):
            customer.delete_customer()

    def test_modify_information_negative_nonexistent_customer(self):
        # Crear una instancia de Customer
        customer = Customer(customer_id="3", name="Alice Doe", email="alice@example.com", phone="111222333")

        # Intentar modificar la información de un cliente que no existe (archivo no existente)
        with self.assertRaises(FileNotFoundError):
            customer.modify_information(name="Updated Name", email="updated@example.com", phone="999888777")

if __name__ == '__main__':
    unittest.main()