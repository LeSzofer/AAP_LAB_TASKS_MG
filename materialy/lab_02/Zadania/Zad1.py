import requests
import time
import concurrent.futures

CAT_API_URL = "https://catfact.ninja/fact"

def get_cat_fact(_):
    """Pobiera jeden fakt o kocie."""
    response = requests.get(CAT_API_URL)
    return response.json().get('fact')

# --- WERSJA SEKWENCYJNA ---
print("=== Sekwencyjnie ===")
start = time.time()

facts = []
for i in range(20):
    facts.append(get_cat_fact(i))

print(f"Pobrano {len(facts)} faktów w {time.time() - start:.2f}s")
print("Przykład:", facts[0])

# --- WERSJA WIELOWĄTKOWA ---
print("\n=== Wielowątkowo ===")
start = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    facts_threaded = list(executor.map(get_cat_fact, range(20)))

print(f"Pobrano {len(facts_threaded)} faktów w {time.time() - start:.2f}s")
print("Przykład:", facts_threaded[0])