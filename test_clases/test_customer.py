import unittest
import json
from io import StringIO
import sys
import os
from unittest.mock import patch
sys.path.append('/Users/luis/Downloads/A01273286_A6.2-main')
from Customer.customer import Customer

class TestCustomer(unittest.TestCase):

    def test_create_customer(self):
        # Crear un cliente
        customer = Customer(customer_id="1", name="John Doe", email="john@example.com", phone="123456789")
        customer.create_customer()
        self.assertTrue(os.path.exists(f"customer_{customer.customer_id}_data.json"))  # Asegurarse de que el archivo exista

    def test_delete_customer(self):
        # Crear un cliente para que exista el archivo
        customer = Customer(customer_id="2", name="Jane Doe", email="jane@example.com", phone="987654321")
        customer.create_customer()
        self.assertTrue(os.path.exists(f"customer_{customer.customer_id}_data.json"))  # Asegurarse de que el archivo exista

        # Llamar a delete_customer y verificar que el archivo ya no existe después de llamar al método
        customer.delete_customer()
        self.assertFalse(os.path.exists(f"customer_{customer.customer_id}_data.json"))  # Asegurarse de que el archivo ya no exista

    def test_display_information(self):
        # Crear un cliente
        customer = Customer(customer_id="3", name="Alice Doe", email="alice@example.com", phone="111222333")

        # Capturar la salida estándar para asertar sobre ella
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            customer.display_information()
            output = mock_stdout.getvalue().strip()

        # Aserciones sobre la salida capturada
        self.assertIn("Customer ID: 3", output)
        self.assertIn("Name: Alice Doe", output)
        self.assertIn("Email: alice@example.com", output)
        self.assertIn("Phone: 111222333", output)

    def test_modify_information(self):
        # Crear un cliente para que exista el archivo
        customer = Customer(customer_id="4", name="Bob Doe", email="bob@example.com", phone="444555666")
        customer.create_customer()
        self.assertTrue(os.path.exists(f"customer_{customer.customer_id}_data.json"))  # Asegurarse de que el archivo exista

        # Llamar a modify_information para cambiar la información del cliente
        customer.modify_information(name="Bob Updated", email="updated@example.com", phone="777888999")

        # Cargar el cliente modificado y verificar que la información se haya actualizado
        modified_customer = Customer.load_from_file(customer.customer_id)
        self.assertEqual(modified_customer.name, "Bob Updated")
        self.assertEqual(modified_customer.email, "updated@example.com")
        self.assertEqual(modified_customer.phone, "777888999")

if __name__ == '__main__':
    unittest.main()
