import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def histogram_normalizowany(tablica, n):
    tablica = np.array(tablica)

    # tworzymy 10 równych pojemników między min a max
    bins = np.linspace(tablica.min(), tablica.max(), 11)

    # przypisanie wartości do pojemników
    pojemniki = pd.cut(tablica, bins=bins)

    # zliczenie i normalizacja
    liczby = pojemniki.value_counts().sort_index()
    udzialy = liczby / liczby.sum()

    plt.figure(figsize=(8, 4))
    plt.bar(udzialy.index.astype(str), udzialy.values, color="skyblue", edgecolor="black")

    plt.xticks(rotation=45, ha='right')
    
    plt.ylabel("P(k)")
    plt.xlabel("k")
    plt.title(f"Kapitał (k) gracza A po {n} turach")
    plt.tight_layout()
    plt.show()


def plot_graph(graph, text):
    x = [point[0] for point in graph]
    y = [point[1] for point in graph]

    plt.bar(x, y, width=0.015, color='steelblue', edgecolor='black')

    plt.xlabel('Prawdopodobieństwo wygrania tury przez gracza A')
    plt.ylabel('Prawdopodobieństwo ruiny gracza A')
    plt.title('Prawdopodobieństwo ruiny gracza A ' + text)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

def plot_graph_line(graph, text):
    x = [point[0] for point in graph]
    y = [point[1] for point in graph]

    plt.plot(x, y, linestyle='-', color='steelblue')

    plt.xlabel('Prawdopodobieństwo wygrania tury przez gracza A')
    plt.ylabel('Prawdopodobieństwo ruiny gracza A')
    plt.title('Prawdopodobieństwo ruiny gracza A ' + text)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

# Ruina gdzie p != q
def r_i(p, q, i, M):
    return ((q/p)**i - (q/p)**M) / (1 - (q/p)**M)

# Ruina gdzie p == q
def r_i_equals(i, M):
    return 1 - (i / M)

def game_a(a: int, b: int, p_a: float, max_steps: int):
    if not 0.0 <= p_a <= 1.0:
        raise ValueError("Prawdopodobieństwo musi być w zakresie od 0 do 1.")

    turns = 0
    while a != 0 and b != 0:
        turns += 1
        value = random.random()
        if value < p_a:
            a += 1
            b -= 1
        else:
            a -= 1
            b += 1
        if (turns >= max_steps):
            break

    return a

NUMBER_OF_GAMES = 1000000
graph = []
graph_a = []

N = [1, 10, 50, 60, 70, 80]

if __name__ == "__main__":
    for n in N:
        a = 50
        b = 50
        p_a = 0.2

        for _ in range(NUMBER_OF_GAMES):
            k_a = game_a(a, b, p_a, n)
            graph.append(k_a)

        histogram_normalizowany(graph, str(n))
        graph.clear()

    # for pair in graph:
    #     graph_a.append((pair[0], r_i_equals(pair[0], 100)))
    # plot_graph_line(graph, "symulacja")
    # plot_graph_line(graph_a, "analitycznie")



