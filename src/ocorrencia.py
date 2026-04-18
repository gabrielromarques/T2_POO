"""
Autor: Gabriel de Resende Oliveira Marques
Professor: Brono Légora
Programação Orientada a Objetos - POO
Data: 24/08/2025
"""

# -*- coding: utf-8 -*-
from __future__ import annotations
from datetime import datetime

class Ocorrencia:
    def __init__(self, codigo_docente: str, evento: str, data_inicio: str, data_fim: str):
        #Construtor da classe Ocorrencia. Armazena os dados de um evento na vida do docente.
        self.codigo_docente = int(codigo_docente)
        self.evento = evento
        self.data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y').date()
        self.data_fim = datetime.strptime(data_fim, '%d/%m/%Y').date() if data_fim else None
