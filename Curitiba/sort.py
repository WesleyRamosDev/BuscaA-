"""
Módulo que ordena os valores dos adjacentes de cada vértice do mapa.
"""

import numpy as np


class Sort:
    def __init__(self, size):
        self.size = size
        self.cities = np.empty(self.size, dtype=object)
        self.last_position = -1

    def list(self):
        if self.last_position == -1:
            print("Nenhuma cidade na lista.")
        else:
            print("Cidades ordenadas por heurística:")
            for index in range(self.last_position + 1):
                print(f"{index} -> {self.cities[index].label} (h: {self.cities[index].target_distance})")

    def insert(self, value):
        if self.last_position == (self.size - 1):
            print("Capacidade máxima atingida.")
            return

        position = 0
        while position <= self.last_position and self.cities[position].target_distance <= value.target_distance:
            position += 1

        for i in range(self.last_position, position - 1, -1):
            self.cities[i + 1] = self.cities[i]

        self.cities[position] = value
        self.last_position += 1
