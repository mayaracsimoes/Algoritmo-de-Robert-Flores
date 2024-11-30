# Algoritmo de Robert e Flores para Ciclos Hamiltonianos

Este repositório contém a implementação do **Algoritmo de Robert e Flores** para encontrar **ciclos Hamiltonianos** em um grafo, com o objetivo de encontrar o menor caminho que passe por todos os vértices de um grafo e retorne ao vértice inicial (ciclo Hamiltoniano).
Este trabalho foi desenvolvido como parte da disciplina Teoria dos Grafos na FURB (Universidade Regional de Blumenau), durante o segundo semestre de 2024.

## Descrição

O algoritmo de Robert e Flores é utilizado para encontrar ciclos Hamiltonianos em grafos, que são caminhos que visitam todos os vértices de um grafo exatamente uma vez e retornam ao vértice inicial. O algoritmo utiliza uma abordagem de **backtracking** para explorar todas as possibilidades de caminhos entre os vértices e, quando necessário, volta atrás para tentar outras opções.

Neste trabalho, a partir de um grafo direcionado e ponderado, implementamos o algoritmo de Robert e Flores para explorar todos os ciclos Hamiltonianos possíveis. O algoritmo também realiza a visualização do grafo para facilitar a compreensão dos ciclos encontrados.

## Objetivo

O objetivo deste projeto é implementar uma solução utilizando o algoritmo de Robert e Flores para:
- Encontrar e listar todos os ciclos Hamiltonianos de um grafo.
- Visualizar o grafo e os caminhos encontrados.

## Algoritmo

### Passos do Algoritmo

1. **Escolher um vértice inicial** `vi`.
2. **Incluir `vi` no conjunto de vértices visitados**: `S = {vi}`.
3. **Adicionar o primeiro vértice viável** do próximo vértice de `S` à sequência `S`, e continuar adicionando até que todos os vértices sejam visitados.
4. Se um ciclo Hamiltoniano for encontrado (isto é, todos os vértices foram visitados e há uma aresta que retorna ao vértice inicial), o ciclo é registrado.
5. Se não for possível adicionar mais vértices, realiza-se um processo de **backtracking**, removendo o último vértice adicionado e tentando novas possibilidades.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
