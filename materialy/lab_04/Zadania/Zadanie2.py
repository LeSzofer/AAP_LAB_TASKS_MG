from pymongo import MongoClient
import requests
import json

# 1. Połączenie z MongoDB (zmień URI, jeśli używasz Atlasa lub innego serwera)
try:
    client = MongoClient("mongodb://localhost:27017",
                         serverSelectionTimeoutMS=5000)
    client.admin.command('ping')  # test połączenia
    print("✅ Połączono z MongoDB.")
except Exception as e:
    print("❌ Błąd połączenia z MongoDB:", e)
    exit(1)

# Wybierz bazę i kolekcję
db = client.lab4
networks = db["networks"]

# Wyczyść kolekcję przed nowym załadowaniem (opcjonalnie, by unikać duplikatów przy powtórnych uruchomieniach)
networks.delete_many({})

# 2. Pobierz dane z API GeckoTerminal
try:
    response = requests.get(
        "https://api.geckoterminal.com/api/v2/networks", timeout=10)
    response.raise_for_status()  # rzuci wyjątkiem przy błędzie HTTP (np. 4xx/5xx)
    data = response.json()
except requests.RequestException as e:
    print("❌ Błąd pobierania danych z API:", e)
    exit(2)

# Sprawdź strukturę
if "data" not in data:
    raise KeyError("Brak klucza 'data' w odpowiedzi API. Sprawdź format JSON.")
raw_networks = data["data"]

print(f"📦 Otrzymano {len(raw_networks)} sieci z API.")

# 3. Przekształć dane — dokumenty MongoDB to dicty z polami `_id`, `attributes`, itd.
# API zwraca listę dokumentów w formacie:
# {
#   "type": "...",
#   "id": "...",
#   "attributes": { "name": ..., "type": "...", ... }
# }

documents = []
for item in raw_networks:
    doc = {
        "_id": item.get("id"),  # użyj id z API jako _id
        "type_api": item.get("type"),
        # rozpakuj atrybuty (np. name, type, native_token)
        **item.get("attributes", {})
    }
    documents.append(doc)

# Wstaw dokumenty do MongoDB
if documents:
    result = networks.insert_many(documents)
    print(f"✅ Wstawiono {len(result.inserted_ids)} dokumentów.")
else:
    print("⚠️ Brak danych do wstawienia.")

# 4. Agregacja: ile sieci per typ (z pola `type`, nie `attributes.type` — sprawdźmy najpierw strukturę)
print("\n📊 Liczba sieci per typ (agregacja MongoDB):")

# Sprawdź przykładowy dokument, by upewnić się, gdzie jest pole `type`
sample = networks.find_one()
if sample:
    print("Przykładowy dokument:", json.dumps(sample, default=str, indent=2))

# Prawdopodobnie typ to pole `type` (na poziomie najwyższym), nie w attributes
pipeline = [
    {"$group": {"_id": "$type", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
]

try:
    results = list(networks.aggregate(pipeline))
    for doc in results:
        print(f"  {doc['_id'] or '<brak typu>'}: {doc['count']} sieci")
except Exception as e:
    print("Błąd agregacji:", e)
