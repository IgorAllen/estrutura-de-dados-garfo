# Sistema de Rotas de Delivery com Grafos

Projeto acadêmico desenvolvido para a disciplina de **Estrutura de Dados**.

## 1. Descrição

O projeto simula um sistema simples de rotas para um serviço de delivery. Ele utiliza um grafo para representar os locais e os caminhos possíveis entre eles, permitindo encontrar uma rota de menor distância entre um ponto de partida e um destino.

## 2. Tipo de grafo utilizado

Foi utilizado um **grafo direcionado e ponderado**:

- **Direcionado:** uma conexão possui sentido definido, representado por uma seta (origem → destino).
- **Ponderado:** cada conexão possui um valor associado, neste exemplo a distância em quilômetros.
- **Vértices (nós):** representam os locais do mapa.
- **Arestas:** representam os caminhos entre os locais.
- **Peso:** representa a distância entre dois locais conectados.

## 3. Cenário de exemplo

Os vértices representam:

| Vértice | Local |
|---|---|
| A | Restaurante |
| B | Cruzamento A |
| C | Cruzamento B |
| D | Cliente |
| E | Cruzamento C |
| F | Cruzamento D |

As conexões do exemplo são:

| Origem | Destino | Distância |
|---|---|---:|
| Restaurante | Cruzamento A | 2 km |
| Cruzamento A | Cruzamento B | 3 km |
| Cruzamento B | Cliente | 2 km |
| Cliente | Cruzamento C | 4 km |
| Cruzamento C | Cruzamento D | 1 km |
| Cruzamento D | Restaurante | 5 km |

> Os valores são fictícios e servem apenas para demonstrar a estrutura.

## 4. Estrutura de dados

O grafo foi implementado usando **lista de adjacência** com um dicionário Python. Cada chave representa um vértice, e seu valor contém os destinos alcançáveis e os respectivos pesos.

Exemplo:

```python
grafo = {
    "Restaurante": {"Cruzamento A": 2},
    "Cruzamento A": {"Cruzamento B": 3}
}
```

## 5. Algoritmo utilizado

O projeto utiliza o **algoritmo de Dijkstra** para encontrar o caminho de menor distância entre dois vértices.

O algoritmo considera os pesos das arestas e atualiza as menores distâncias conhecidas até encontrar a melhor rota.

## 6. Como executar

### Requisitos

- Python 3 instalado.

### Passos

1. Baixe ou clone este repositório.
2. Abra o terminal na pasta do projeto.
3. Execute:

```bash
python src/main.py
```

4. Informe o local de partida e o destino exatamente como aparecem na lista.

## 7. Exemplo de execução

Entrada:

```text
Digite o local de partida: Restaurante
Digite o destino: Cliente
```

Saída esperada:

```text
Menor rota: Restaurante -> Cruzamento A -> Cruzamento B -> Cliente
Distância total: 7 km
```

## 8. Aplicações na tecnologia

Grafos são utilizados em diferentes sistemas, por exemplo:

- Aplicativos de mapas e navegação.
- Aplicativos de delivery.
- Sistemas de transporte e logística.
- Planejamento de rotas.

## 9. Conclusão

O exemplo demonstra como grafos podem representar conexões entre locais e como um algoritmo pode utilizar essa estrutura para encontrar caminhos de menor custo. Em um sistema real, os pesos poderiam representar distância, tempo de deslocamento ou custo da viagem.

---

**Disciplina:** Estrutura de Dados  
**Tema:** Grafos — grafo direcionado e ponderado  
**Linguagem:** Python
