import pytest
from product import Product


# --- Fixture ---

@pytest.fixture
def product():
    """Tworzy instancje Product do testow (odpowiednik setUp)."""
    # TODO: Zwroc instancje Product, np. Product("Laptop", 2999.99, 10)
    return Product("Laptop", 2999.99, 10)


# --- Testy z fixture ---

def test_is_available(product):
    """Sprawdz dostepnosc produktu."""
    # TODO: Uzyj assert product.is_available() == True
    assert product.is_available() == True


def test_total_value(product):
    """Sprawdz wartosc calkowita."""
    # TODO: Uzyj assert product.total_value() == oczekiwana_wartosc
    expected = product.price * product.quantity
    assert product.total_value() == expected


# --- Testy z parametryzacja ---

@pytest.mark.parametrize("amount, expected_quantity", [
    # TODO: Dodaj przypadki testowe jako krotki, np.:
    # (5, 15),   # dodanie 5 do poczatkowych 10 = 15
    # (0, 10),   # dodanie 0 = bez zmian
    # (100, 110),  # dodanie 100
    (5, 15),
    (0, 10),
    (100, 110),
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    """Testuje add_stock z roznymi wartosciami."""
    # TODO: Wywolaj product.add_stock(amount) i sprawdz product.quantity
    product.add_stock(amount)
    assert product.quantity == expected_quantity


# --- Testy bledow ---

def test_remove_stock_too_much_raises(product):
    """Sprawdz, czy proba usuniecia za duzej ilosci rzuca ValueError."""
    # TODO: Uzyj with pytest.raises(ValueError):
    with pytest.raises(ValueError):
        product.remove_stock(25)


def test_add_stock_negative_raises(product):
    """Sprawdz, czy ujemna wartosc w add_stock rzuca ValueError."""
    # TODO: Uzyj with pytest.raises(ValueError):
    with pytest.raises(ValueError):
        product.add_stock(-5)


@pytest.fixture
def product_100():

    return Product("Testowy", 100.0, 5)


@pytest.mark.parametrize("percent, expected_price", [
    (0,   100.0),
    (50,   50.0),
    (100,   0.0),
    (25,   75.0),
    (10,   90.0),
])
def test_apply_discount(product_100, percent, expected_price):
    
    product_100.apply_discount(percent)
    assert product_100.price == pytest.approx(expected_price)


@pytest.mark.parametrize("invalid_percent", [
    -1,
    -100,
    101,
    200,
])
def test_apply_discount_invalid_raises(product_100, invalid_percent):

    with pytest.raises(ValueError):
        product_100.apply_discount(invalid_percent)
