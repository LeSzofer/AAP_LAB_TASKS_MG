# -*- coding: utf-8 -*-
"""Testy unittest dla klasy Product -- uzupelnij metody testowe!

Uruchomienie: python -m unittest test_product_unittest -v
"""

import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Przygotuj instancje Product do testow."""
        # TODO: Stworz instancje Product, np. Product("Laptop", 2999.99, 10)
        self.product = Product("Laptop", 2999.99, 10)

    # --- Testy add_stock ---

    def test_add_stock_positive(self):
        """Sprawdz, czy dodanie towaru zwieksza quantity."""
        # TODO: Wywolaj add_stock i sprawdz nowa wartosc quantity
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_add_stock_negative_raises(self):
        """Sprawdz, czy ujemna wartosc rzuca ValueError."""
        # TODO: Uzyj self.assertRaises(ValueError) i wywolaj add_stock z ujemna wartoscia
        with self.assertRaises(ValueError):
            self.product.add_stock(-5)

    # --- Testy remove_stock ---

    def test_remove_stock_positive(self):
        """Sprawdz, czy usuniecie towaru zmniejsza quantity."""
        # TODO: Wywolaj remove_stock i sprawdz nowa wartosc quantity
        self.product.remove_stock(5)
        self.assertEqual(self.product.quantity, 5)

    def test_remove_stock_too_much_raises(self):
        """Sprawdz, czy proba usuniecia wiecej niz jest dostepne rzuca ValueError."""
        # TODO: Uzyj self.assertRaises(ValueError)
        self.assertRaises(ValueError, self.product.remove_stock, 15)

    def test_remove_stock_negative_raises(self):
        """Sprawdz, czy ujemna wartosc rzuca ValueError."""
        # TODO: Uzyj self.assertRaises(ValueError)
        self.assertRaises(ValueError, self.product.remove_stock, -5)

    # --- Testy is_available ---

    def test_is_available_when_in_stock(self):
        """Sprawdz, czy produkt z quantity > 0 jest dostepny."""
        # TODO: Uzyj self.assertTrue
        self.assertTrue(self.product.is_available())

    def test_is_not_available_when_empty(self):
        """Sprawdz, czy produkt z quantity == 0 nie jest dostepny."""
        # TODO: Stworz produkt z quantity=0 i uzyj self.assertFalse
        self.product = Product("Laptop", 2999.99, 0)
        self.assertFalse(self.product.is_available())

    # --- Testy total_value ---

    def test_total_value(self):
        """Sprawdz, czy total_value zwraca price * quantity."""
        # TODO: Uzyj self.assertEqual
        expected = self.product.price * self.product.quantity
        self.assertAlmostEqual(self.product.total_value(), expected)


if __name__ == "__main__":
    unittest.main()
