import multiprocessing
import time
from lab2_functions import calculate_power_sum

if __name__ == "__main__":
    cores = multiprocessing.cpu_count()
    print(f"Dostępne rdzenie procesora: {cores}")
    
    numbers = list(range(1, 10_001))
    print(f"Liczba zadań: {len(numbers)}")
    
    # --- SEKWENCYJNIE ---
    print("\n=== Wersja SEKWENCYJNA ===")
    start = time.time()
    results_seq = [calculate_power_sum(n) for n in numbers]
    elapsed_seq = time.time() - start
    print(f"Czas: {elapsed_seq:.2f}s")
    
    # --- WIELOPROCESOWO ---
    print("\n=== Wersja WIELOPROCESOWA ===")
    start = time.time()
    with multiprocessing.Pool(processes=cores) as pool:
        results_mp = pool.map(calculate_power_sum, numbers)
    elapsed_mp = time.time() - start
    print(f"Czas: {elapsed_mp:.2f}s")
    
    # --- PORÓWNANIE ---
    print("\n=== PORÓWNANIE ===")
    print(f"Wyniki identyczne: {results_seq == results_mp}")
    print(f"Przyspieszenie: {elapsed_seq / elapsed_mp:.1f}x szybciej")