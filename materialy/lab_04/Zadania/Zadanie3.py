import numpy as np

# Baza filmów z embeddingami (wektory 3-wymiarowe)
filmy = {
    "Incepcja":          np.array([0.8, 0.3, 0.9]),
    "Matrix":            np.array([0.75, 0.35, 0.85]),
    "Toy Story":         np.array([0.2, 0.9, 0.1]),
    "Shrek":             np.array([0.25, 0.85, 0.15]),
    "Szeregowiec Ryan":  np.array([0.6, 0.1, 0.7]),
}


def cosine_similarity(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    """Zwraca podobieństwo kosinusowe między dwoma wektorami."""
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(np.dot(vec_a, vec_b) / (norm_a * norm_b))


def semantic_search(query_vec: np.ndarray, database: dict, top_k: int = 3):
    """
    Znajduje top_k najbardziej podobnych filmów do zapytania.

    Args:
        query_vec: wektor zapytania (np. [0.7, 0.3, 0.8])
        database: dict {tytuł: np.array}
        top_k: liczba wyników do zwrócenia

    Returns:
        lista krotek [(tytuł, podobieństwo), ...], posortowana malejąco
    """
    scores = []
    for title, embedding in database.items():
        sim = cosine_similarity(query_vec, embedding)
        scores.append((title, sim))

    # Sortowanie po podobieństwie (malejąco)
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_k]


# Przykład użycia:
query = np.array([0.7, 0.3, 0.8])  # "cos jak sci-fi / akcja"
print("🔍 Zapytanie: 'sci-fi/akcja' → wektor [0.7, 0.3, 0.8]\n")
results = semantic_search(query, filmy, top_k=3)

for i, (title, sim) in enumerate(results, start=1):
    print(f"{i}. {title}: {sim:.3f}")

# Opcjonalnie: wizualizacja (czytelniejsza)
print("\n📊 Wyniki:")
print("-" * 30)
for title, sim in results:
    bar = "█" * int(sim * 50)  # pasek od 0 do 50
    print(f"{title:>15}: {sim:5.3f} {bar}")
