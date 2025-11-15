import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def histogram_normalizowany(tablica, pa):
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
    
    plt.ylabel("P(L)")
    plt.xlabel("L")
    plt.title("Prawdopodobieństwo liczby tur dla pa = " + pa)
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

    plt.xlabel('P(a)')
    plt.ylabel('Lmax')
    plt.title('Maksymalna długość rozgrywki' + text)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

# Ruina gdzie p != q
def r_i(p, q, i, M):
    return ((q/p)**i - (q/p)**M) / (1 - (q/p)**M)

# Ruina gdzie p == q
def r_i_equals(i, M):
    return 1 - (i / M)

def game_a(a: int, b: int, p_a: float):
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

    return turns

NUMBER_OF_GAMES = 1000
SAMPLES = 1000
graph = []


if __name__ == "__main__":
    for k in range(1, SAMPLES + 1):
        x = 10 * k / (SAMPLES + 1)
        p_a = x / 10.0
        a = 50
        b = 50

        max_turns = 0
        for _ in range(NUMBER_OF_GAMES):
            turns = game_a(a, b, p_a)
            if turns > max_turns:
                max_turns = turns
        graph.append((p_a, max_turns))

    plot_graph_line(graph, "")



