🐍 Sistema de Avaliação Docente (Versão Python)



* Este repositório contém a implementação em Python do sistema de recredenciamento docente para o PPGEE/UFES. O objetivo foi recriar a lógica de negócio explorando as facilidades da linguagem Python para automação e manipulação de strings.



🛠️ Diferenciais Técnicos



* Herança e Polimorfismo: Diferente da versão anterior, aqui as classes Periodico e Conferencia herdam diretamente de Publicacao, sobrescrevendo o método calcular\_pontos() de forma polimórfica.



* Tratamento de Datas: Uso da biblioteca nativa datetime para realizar cálculos complexos de idade e períodos de licença com maior precisão e código mais limpo.



* Type Hinting: Utilização de dicas de tipo (List, Dict, Any) para garantir a robustez do código e facilitar a manutenção, seguindo as PEPs do Python.



* Parsing de CSV: Implementação eficiente utilizando o módulo csv para tratar variações de delimitadores e caracteres especiais.



📂 Estrutura de Arquivos



* main.py: Ponto de entrada que gerencia o fluxo de leitura e geração de relatórios.



* docente.py: Classe principal com as regras de negócio para recredenciamento.



* publicacao.py: Estrutura de classes utilizando herança para diferentes tipos de produção científica.



* ocorrencia.py: Gerenciamento de eventos temporais (licenças, cargos).



🚀 Como Rodar



* Não é necessário compilar. Basta ter o Python 3 instalado.



Bash

&#x09;python main.py

