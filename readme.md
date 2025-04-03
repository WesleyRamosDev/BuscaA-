# 🗺️ Busca Gulosa e Busca A* - Mapa de Curitiba  

Aluno: **Wesley Santos Ramos**  
RA: **010623062**  

Este projeto implementa os algoritmos de **Busca Gulosa** e **Busca A*** para encontrar a menor rota entre cidades do Paraná, utilizando um grafo ponderado.  

## 🧠 Pesquisa: Busca Gulosa vs. Busca A*  

### 🔹 Busca Gulosa  
A Busca Gulosa escolhe sempre o caminho que parece mais promissor no momento, sem considerar o custo total. Seu critério de escolha é baseado apenas na **distância heurística** até o destino.  

**Vantagens:**  
✔️ Rápida execução  
✔️ Simples de implementar  

**Desvantagens:**  
❌ Pode levar a soluções não ótimas  
❌ Não considera o custo total do caminho  

### 🔹 Busca A*  
O algoritmo A* equilibra eficiência e otimalidade, combinando a distância percorrida até o momento (**g(n)**) com a estimativa heurística do custo restante (**h(n)**). Ele busca sempre o caminho com o menor custo total estimado:  

> **f(n) = g(n) + h(n)**  

**Vantagens:**  
✔️ Garante encontrar o caminho mais curto  
✔️ Considera o custo real e a heurística  

**Desvantagens:**  
❌ Maior uso de memória e processamento  
❌ Pode ser mais lento dependendo do problema  

## 🚀 Tecnologias Utilizadas  
- Python 🐍  
- Algoritmos de Busca 🤖  
- Estruturas de Dados (Grafos) 🌐  

## 📌 Como Usar  

### 1️⃣ Clone este repositório  
```sh
