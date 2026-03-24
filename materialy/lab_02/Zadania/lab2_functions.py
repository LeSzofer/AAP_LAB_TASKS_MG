def calculate_power_sum(n):
    """
    Dla danego n oblicza sumę: 1^1 + 2^2 + 3^3 + ... + 100^100
    n jest tutaj tylko numerem zadania - każda liczba
    dostaje ten sam ciężki rachunek do wykonania.
    """
    total = 0
    for i in range(1, 301):
        total += i ** i
    return total