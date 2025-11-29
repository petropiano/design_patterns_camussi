from __future__ import annotations
from abc import ABC, abstractmethod

class InputStrategy(ABC):
    @abstractmethod
    def ler_pulo(self):
        pass

    @abstractmethod
    def ler_ataque(self):
        pass

class ControleXbox(InputStrategy):
    def ler_pulo(self):
        return "Xbox: Botão 'A'"

    def ler_ataque(self):
        return "Xbox: 'X'"

class ControlePlayStation(InputStrategy):
    def ler_pulo(self):
        return "PlayStation: 'X'"

    def ler_ataque(self):
        return "PlayStation: 'Quadrado'"

class TecladoPC(InputStrategy):
    def ler_pulo(self):
        return "PC: 'ESPAÇO'"

    def ler_ataque(self):
        return "PC: Click Esquerdo do Mouse."

class GameContext:
    def __init__(self, strategy: InputStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> InputStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: InputStrategy) -> None:
        self._strategy = strategy

    def processar_input_jogador(self) -> None:
        print(f"Input: {self._strategy.__class__.__name__}")
        
        resultado_pulo = self._strategy.ler_pulo()
        resultado_ataque = self._strategy.ler_ataque()
        
        print(f" -> Pulo: {resultado_pulo}")
        print(f" -> Ataque: {resultado_ataque}")
        print("-" * 40)
