"""
Autor: Gabriel de Resende Oliveira Marques
Professor: Brono Légora
Programação Orientada a Objetos - POO
Data: 24/08/2025
"""

# -*- coding: utf-8 -*-
from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

# Usado apenas para checagem de tipo, evita importações circulares.
if TYPE_CHECKING:
    from publicacao import Publicacao
    from ocorrencia import Ocorrencia

class Docente:
    def __init__(self, codigo: str, nome: str, data_nascimento: str, data_ingresso: str):
        #Construtor da classe Docente. Armazena os dados do docente e listas para suas publicações e ocorrências.
        self.codigo = int(codigo)
        self.nome = nome
        self.data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
        self.data_ingresso = datetime.strptime(data_ingresso, '%d/%m/%Y').date()
        self.publicacoes: list[Publicacao] = [] # Lista para armazenar objetos Publicacao
        self.ocorrencias: list[Ocorrencia] = [] # Lista para armazenar objetos Ocorrencia
        self.pontuacao = 0.0

    def calcular_pontuacao(self, ano_avaliacao: int) -> float:
        #Calcula a pontuação do docente com base em suas publicações dos dois anos anteriores.
        pontuacao_total = 0.0
        anos_validos = [ano_avaliacao - 1, ano_avaliacao - 2]
        
        for publicacao in self.publicacoes:
            if publicacao.ano in anos_validos:
                pontuacao_total += publicacao.calcular_pontos()
        
        self.pontuacao = pontuacao_total
        return self.pontuacao

    def verificar_recredenciamento(self, ano_avaliacao: int) -> str:
        #Verifica se o docente atende aos critérios para recredenciamento.
        data_referencia = datetime(ano_avaliacao, 1, 1).date()
        
        # Critério 1: Coordenador
        for ocorrencia in self.ocorrencias:
            if ocorrencia.evento == "Coordenador" and ocorrencia.data_inicio <= data_referencia and \
               (ocorrencia.data_fim is None or ocorrencia.data_fim >= data_referencia):
                return "Coordenador"

        # Critério 2: Licença Maternidade
        ano_anterior = ano_avaliacao - 1
        for ocorrencia in self.ocorrencias:
            if ocorrencia.evento == "Licença Maternidade":
                if ocorrencia.data_inicio <= data_referencia and \
                   (ocorrencia.data_fim is None or ocorrencia.data_fim >= data_referencia):
                    return "Licença Maternidade"
                if ocorrencia.data_inicio.year == ano_anterior or \
                   (ocorrencia.data_fim and ocorrencia.data_fim.year == ano_anterior):
                    return "Licença Maternidade"

        # Critério 3: Entrou no programa nos dois anos anteriores
        data_dois_anos_atras = datetime(ano_avaliacao - 2, 1, 1).date()
        if self.data_ingresso >= data_dois_anos_atras:
            return "PPJ"
            
        # Critério 4: Mais de 60 anos
        idade = data_referencia.year - self.data_nascimento.year
        if idade > 60:
            if data_referencia.month < self.data_nascimento.month or \
               (data_referencia.month == self.data_nascimento.month and data_referencia.day < self.data_nascimento.day):
                idade -= 1
            if idade > 60:
                return "PPS"

        # Critério 5: Pontuação mínima
        if self.pontuacao >= 2.0:
            return "Sim"
        
        return "Não"
