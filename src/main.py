"""
Autor: Gabriel de Resende Oliveira Marques
Professor: Brono Légora
Programação Orientada a Objetos - POO
Data: 24/08/2025
"""

# -*- coding: utf-8 -*-
from __future__ import annotations
import os
import csv
from docente import Docente
from publicacao import Publicacao, Conferencia, Periodico
from ocorrencia import Ocorrencia
from typing import Dict, List, Any

# Classe principal para controlar a execução do programa.

class SistemaAvaliacao:
    def __init__(self):
        #Construtor da classe principal. Inicializa as listas para armazenar todos os dados lidos.
        self.docentes: List[Docente] = []
        self.ocorrencias: List[Ocorrencia] = []
        self.publicacoes: List[Publicacao] = []
        # Um dicionário para encontrar docentes pelo código rapidamente.
        self.mapa_docentes: Dict[int, Docente] = {} 

    def ler_dados(self, pasta_entrada: str) -> bool:
        #Lê os dados dos arquivos CSV da pasta especificada.
        
        # Leitura sem tratamento de erros para simplificar o código.
        with open(os.path.join(pasta_entrada, "docentes.csv"), 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)
            for row in reader:
                docente = Docente(row[0], row[1], row[2], row[3])
                self.docentes.append(docente)
                self.mapa_docentes[docente.codigo] = docente

        with open(os.path.join(pasta_entrada, "ocorrencias.csv"), 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)
            for row in reader:
                ocorrencia = Ocorrencia(row[0], row[1], row[2], row[3])
                self.ocorrencias.append(ocorrencia)

        with open(os.path.join(pasta_entrada, "publicacoes.csv"), 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)
            for row in reader:
                if row[6] == '':
                    publicacao = Periodico(row[0], row[1], row[2], row[3], row[4], row[5], None, row[7], row[8], row[9])
                else:
                    publicacao = Conferencia(row[0], row[1], row[2], row[3], row[4], None, row[6], row[7], row[8], row[9])
                self.publicacoes.append(publicacao)

        return True

    def associar_dados(self):
        #Associa as ocorrências e publicações aos seus respectivos docentes.
        
        for ocorrencia in self.ocorrencias:
            if ocorrencia.codigo_docente in self.mapa_docentes:
                self.mapa_docentes[ocorrencia.codigo_docente].ocorrencias.append(ocorrencia)
        
        for publicacao in self.publicacoes:
            for codigo_autor in publicacao.autores_codigos:
                if codigo_autor in self.mapa_docentes:
                    docente = self.mapa_docentes[codigo_autor]
                    docente.publicacoes.append(publicacao)
                    publicacao.autores.append(docente)
        

    def gerar_relatorios(self, pasta_saida: str, ano_avaliacao: int):
        #Gera os dois arquivos de relatório na pasta de saída.
        
        if not os.path.exists(pasta_saida):
            os.makedirs(pasta_saida)
            
        with open(os.path.join(pasta_saida, "1-recredenciamento.csv"), 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["nome do docente", "pontuação alcançada", "recredenciado?"])
            
            docentes_ordenados = sorted(self.docentes, key=lambda d: list(self.mapa_docentes.keys()).index(d.codigo))
            
            for docente in docentes_ordenados:
                docente.calcular_pontuacao(ano_avaliacao)
                recredenciado = docente.verificar_recredenciamento(ano_avaliacao)
                writer.writerow([docente.nome, f"{docente.pontuacao:.3f}".replace('.', ','), recredenciado])
        
        with open(os.path.join(pasta_saida, "2-publicacoes.csv"), 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(["ano", "nome conferência/periódico", "fator de impacto", "título da publicação", "nomes dos docentes", "tipo", "número de pontos"])
            
            anos_validos = [ano_avaliacao - 1, ano_avaliacao - 2]
            for publicacao in self.publicacoes:
                if publicacao.ano in anos_validos:
                    nomes_autores = ", ".join([d.nome for d in publicacao.autores])
                    tipo = "Periódico" if isinstance(publicacao, Periodico) else "Conferência"
                    pontos = publicacao.calcular_pontos()
                    
                    fator_impacto_str = f"{publicacao.fator_impacto:.3f}".replace('.', ',')
                    pontos_str = f"{pontos:.3f}".replace('.', ',')
                    
                    writer.writerow([
                        publicacao.ano,
                        publicacao.nome_pub,
                        fator_impacto_str,
                        publicacao.titulo,
                        nomes_autores,
                        tipo,
                        pontos_str
                    ])
        
        print("Relatórios gerados com sucesso na pasta 'saida'!")
        
if __name__ == "__main__":
    sistema = SistemaAvaliacao()
    
    pasta = input("Digite a pasta dos arquivos de entrada (ex: 01): ")
    ano = int(input("Digite o ano para avaliação (ex: 2025): "))
    
    sistema.ler_dados(pasta)
    sistema.associar_dados()
    sistema.gerar_relatorios("saida", ano)

