import sqlite3
import requests

# 1. Pobierz dane z API
response = requests.get("https://randomuser.me/api/?results=30")
users = response.json()["results"]

# 2. Stwórz połączenie z bazą danych SQLite (lub pamięć podręczną: ':memory:')
conn = sqlite3.connect(':memory:')  # lub 'users.db'
cursor = conn.cursor()

# 3. Utwórz tabelę Users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        gender TEXT NOT NULL,
        country TEXT NOT NULL
    )
''')

# 4. Wstaw dane (parametryzacja: `?` – bez f-stringów!)
insert_query = '''
    INSERT INTO Users (first_name, last_name, email, age, gender, country)
    VALUES (?, ?, ?, ?, ?, ?)
'''

for user in users:
    name = user['name']
    location = user['location']
    data = (
        name['first'],
        name['last'],
        user['email'],
        # wiek jest jako string lub float, więc konwertujemy na int
        int(user['dob']['age']),
        user['gender'],
        location['country']
    )
    cursor.execute(insert_query, data)

# Zatwierdź zmiany
conn.commit()

# 5. Zapytania analityczne

# A. Ile jest mężczyzn, a ile kobiet?
print("Liczba mężczyzn i kobiet:")
cursor.execute("SELECT gender, COUNT(*) AS count FROM Users GROUP BY gender")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]}")

# B. Jaki jest średni wiek?
print("\nŚredni wiek:")
cursor.execute("SELECT AVG(age) AS avg_age FROM Users")
avg_age = cursor.fetchone()[0]
print(f"  Średni wiek: {avg_age:.2f}")

# C. W ilu krajach mieszkają użytkownicy? (czyli ile różnych krajów)
print("\nLiczba różnych krajów:")
cursor.execute("SELECT COUNT(DISTINCT country) AS num_countries FROM Users")
num_countries = cursor.fetchone()[0]
print(f"  Użytkownicy pochodzą z {num_countries} krajów.")

# Opcjonalnie: podsumowanie per kraj (czyli ile użytkowników z każdego kraju)
print("\nRozkład użytkowników wg krajów:")
cursor.execute(
    "SELECT country, COUNT(*) AS count FROM Users GROUP BY country ORDER BY count DESC")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]}")

# Zamknij połączenie
conn.close()
