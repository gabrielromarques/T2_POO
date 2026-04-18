"""
Autor: Gabriel de Resende Oliveira Marques
Professor: Brono Légora
Programação Orientada a Objetos - POO
Data: 24/08/2025
"""

# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import List

class Publicacao:
    def __init__(self, ano: str, nome_pub: str, titulo: str, autores_codigos: str, edicao: str, volume: str, local: str, pag_ini: str, pag_fim: str, fator_impacto: str):       
        #Construtor da classe Publicacao. Armazena todos os dados de uma publicação lida do arquivo CSV.
        self.ano = int(ano)
        self.nome_pub = nome_pub
        self.titulo = titulo
        self.autores_codigos: List[int] = [int(c.strip()) for c in autores_codigos.split(',')]
        self.edicao = int(edicao) if edicao else None
        self.volume = int(volume) if volume else None
        self.local = local
        self.pag_ini = int(pag_ini) if pag_ini else None
        self.pag_fim = int(pag_fim) if pag_fim else None
        self.fator_impacto = float(fator_impacto.replace(',', '.'))
        self.autores: list[any] = [] # Lista de objetos Docente.

    def calcular_pontos(self) -> float:     #Método base para calcular os pontos. Subclasses irão sobrescrever este método.
        return 0.0

class Conferencia(Publicacao):
    def calcular_pontos(self) -> float:     #Calcula os pontos para uma publicação em conferência. Contribuição: 0.5x o fator de impacto.
        return self.fator_impacto * 0.5

class Periodico(Publicacao):
    def calcular_pontos(self) -> float:     #Calcula os pontos para uma publicação em periódico. Contribuição: 1.0x o fator de impacto.
        return self.fator_impacto * 1.0
