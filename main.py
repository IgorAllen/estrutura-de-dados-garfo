"""
Projeto: Sistema de Rotas de Delivery
Estrutura de Dados: Grafo direcionado e ponderado

Os vértices representam locais e as arestas representam caminhos.
O peso de cada aresta representa a distância em quilômetros.
"""

from math import inf
import heapq


# Lista de adjacência: origem -> {destino: distância em km}
grafo = {
    "Restaurante": {"Cruzamento A": 2},
    "Cruzamento A": {"Cruzamento B": 3},
    "Cruzamento B": {"Cliente": 2},
    "Cliente": {"Cruzamento C": 4},
    "Cruzamento C": {"Cruzamento D": 1},
    "Cruzamento D": {"Restaurante": 5},
}


def exibir_grafo(grafo):
    """Mostra os vértices e suas conexões."""
    print("\n=== MAPA DE ROTAS ===")
    for origem, destinos in grafo.items():
        if not destinos:
            print(f"{origem} -> sem saídas")
            continue

        caminhos = ", ".join(
            f"{destino} ({distancia} km)"
            for destino, distancia in destinos.items()
        )
        print(f"{origem} -> {caminhos}")


def menor_rota(grafo, inicio, destino):
    """
    Encontra a rota de menor distância usando o algoritmo de Dijkstra.
    Retorna (distância_total, caminho).
    """
    distancias = {vertice: inf for vertice in grafo}
    anteriores = {vertice: None for vertice in grafo}

    if inicio not in grafo or destino not in grafo:
        return inf, []

    distancias[inicio] = 0
    fila = [(0, inicio)]

    while fila:
        distancia_atual, atual = heapq.heappop(fila)

        if distancia_atual > distancias[atual]:
            continue

        if atual == destino:
            break

        for vizinho, peso in grafo[atual].items():
            nova_distancia = distancia_atual + peso

            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                anteriores[vizinho] = atual
                heapq.heappush(fila, (nova_distancia, vizinho))

    if distancias[destino] == inf:
        return inf, []

    caminho = []
    atual = destino
    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]

    caminho.reverse()
    return distancias[destino], caminho


def main():
    print("SISTEMA DE ROTAS DE DELIVERY")
    print("Exemplo acadêmico de grafo direcionado e ponderado")

    exibir_grafo(grafo)

    print("\nLocais disponíveis:")
    for local in grafo:
        print(f"- {local}")

    inicio = input("\nDigite o local de partida: ").strip()
    destino = input("Digite o destino: ").strip()

    distancia, caminho = menor_rota(grafo, inicio, destino)

    if not caminho:
        print("\nNão foi possível encontrar uma rota.")
        print("Confira os nomes dos locais e tente novamente.")
        return

    print("\n=== RESULTADO ===")
    print("Menor rota:", " -> ".join(caminho))
    print(f"Distância total: {distancia} km")


if __name__ == "__main__":
    main()
