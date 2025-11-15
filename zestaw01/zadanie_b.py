import random
import matplotlib.pyplot as plt

def plot_graph(graph):
    x = [point[0] for point in graph]
    y = [point[1] for point in graph]

    plt.bar(x, y, width=0.015, color='steelblue', edgecolor='black')

    plt.xlabel('Prawdopodobieństwo wygrania tury przez gracza A')
    plt.ylabel('Prawdopodobieństwo ruiny gracza A')
    plt.title('Prawdopodobieństwo ruiny gracza A')

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

def game_a(a: int, b: int, p_a: float):
    if not 0.0 <= p_a <= 1.0:
        raise ValueError("Prawdopodobieństwo musi być w zakresie od 0 do 1.")

    while a != 0 and b != 0:
        value = random.random()
        if value < p_a:
            a += 1
            b -= 1
        else:
            a -= 1
            b += 1

    if a == 0:
        return "A"
    if b == 0:
        return "B"

    return "NaN"

NUMBER_OF_GAMES = 1000
graph = []
graph_a = []

if __name__ == "__main__":
    for i in range(1, 100):
        a = i
        b = 100 - a

        ruined_a = 0
        for _ in range(NUMBER_OF_GAMES):
            if game_a(a, b, 0.5) == "A":
                ruined_a += 1

        p_ra = ruined_a / NUMBER_OF_GAMES
        graph.append((a, p_ra))

    for pair in graph:
        graph_a.append((pair[0], r_i_equals(pair[0], 100)))
    plot_graph_line(graph, "symulacja")
    plot_graph_line(graph_a, "analitycznie")



