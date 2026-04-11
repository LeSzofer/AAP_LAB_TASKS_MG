# ========================================
# Szkielet pliku: product.py
# Uzupelnij implementacje!
# ========================================

class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
        # TODO: Zapisz atrybuty name, price, quantity
        # Pamietaj o walidacji: price >= 0, quantity >= 0
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative")

    def add_stock(self, amount: int):
        # TODO: Dodaj ilosc do magazynu. Rzuc ValueError jesli amount < 0
        if amount < 0:
            raise ValueError("Amount must be non-negative")
        self.quantity += amount

    def remove_stock(self, amount: int):
        # TODO: Usun ilosc z magazynu.
        # Rzuc ValueError jesli amount < 0 lub amount > quantity
        if amount < 0 or amount > self.quantity:
            raise ValueError("Amount must be non-negative and less than or equal to quantity")
        self.quantity -= amount

    def is_available(self) -> bool:
        # TODO: Zwroc True jesli quantity > 0
        return self.quantity > 0

    def total_value(self) -> float:
        # TODO: Zwroc price * quantity
        return self.price * self.quantity