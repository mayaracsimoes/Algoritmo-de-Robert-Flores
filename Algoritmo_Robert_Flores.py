import networkx as nx
import matplotlib.pyplot as plt

def robert_flores_todos_ciclos(G, vertice_inicial):
    """
    Implementa o algoritmo de Robert e Flores para encontrar todos os ciclos Hamiltonianos
    em um grafo dirigido.
    
    Args:
        G: Grafo (objeto NetworkX, DiGraph para grafo dirigido)
        vertice_inicial: Vértice inicial para iniciar os ciclos.
    
    Returns:
        Uma lista contendo todos os ciclos Hamiltonianos encontrados.
    """
    caminho = [vertice_inicial]  # Caminho inicial S = {v1}
    ciclos = []  # Lista para armazenar todos os ciclos Hamiltonianos

    def busca(v_atual):
        # Verificar se o ciclo está completo
        if len(caminho) == len(G.nodes):
            if caminho[0] in G.neighbors(v_atual):  # Verificar se há aresta de retorno
                caminho.append(caminho[0])  # Fecha o ciclo Hamiltoniano
                ciclos.append(caminho[:])  # Armazena uma cópia do ciclo
                caminho.pop()  # Remove o vértice inicial para continuar explorando
            return

        # Tentar adicionar um vértice viável
        for vizinho in G.neighbors(v_atual):
            if vizinho not in caminho:  # Verifica se o vértice ainda não foi visitado
                caminho.append(vizinho)
                busca(vizinho)  # Continuar a busca
                caminho.pop()  # Backtracking: remover o vértice

    # Iniciar a busca a partir do vértice inicial
    busca(vertice_inicial)
    return ciclos


def desenhar_ciclo(G, ciclo, titulo):
    """
    Desenha o grafo com destaque para o ciclo Hamiltoniano em um grafo dirigido.
    
    Args:
        G: Grafo (objeto NetworkX, DiGraph)
        ciclo: Lista de vértices representando o ciclo Hamiltoniano.
        titulo: Título do gráfico.
    """
    pos = nx.spring_layout(G)  # Layout dos nós
    plt.figure(figsize=(8, 6))
    
    # Desenhar o grafo completo (com direção nas arestas)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=800, font_weight='bold', arrows=True)
    
    # Destacar o ciclo Hamiltoniano
    edges = [(ciclo[i], ciclo[i + 1]) for i in range(len(ciclo) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2.5, arrows=True)
    
    # Título do gráfico
    plt.title(titulo, fontsize=14)
    plt.show()


if __name__ == "__main__":
    # Criar o grafo dirigido com base nas adjacências fornecidas
    G = nx.DiGraph()
    G.add_edges_from([
        ('v1', 'v2'), ('v1', 'v3'),('v1', 'v4'),
        ('v2', 'v6'),
        ('v3', 'v2'), ('v3', 'v4'),('v3', 'v7'),
        ('v4', 'v2'), ('v4', 'v7'),
        ('v5', 'v3'), ('v5', 'v4'),('v5', 'v6'),
        ('v6', 'v3'), ('v6', 'v5'), 
        ('v7', 'v1'), ('v7', 'v6')
    ])

    # Vértice inicial
    vertice_inicial = 'v2'

    # Executar o algoritmo
    ciclos = robert_flores_todos_ciclos(G, vertice_inicial)

    # Exibir os resultados e desenhar os ciclos
    if ciclos:
        print(f"Todos os ciclos Hamiltonianos encontrados a partir de {vertice_inicial}:")
        for i, ciclo in enumerate(ciclos, start=1):
            print(f"Ciclo {i}: {ciclo}")
            #desenhar_ciclo(G, ciclo, f"Ciclo Hamiltoniano {i}")
    else:
        print(f"Nenhum ciclo Hamiltoniano foi encontrado a partir de {vertice_inicial}.")
