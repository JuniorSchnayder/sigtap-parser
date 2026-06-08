# SIGTAP Parser & Financiamento Joiner

Processador e unificador de tabelas do SIGTAP (DATASUS) usando Python e Pandas. 

O script realiza o cruzamento exato (Left Join) entre duas tabelas do SIGTAP: a de procedimentos e a de financiamento. Ele automatiza a extração posicional (FWF), une os dados e gera um .csv estruturado para auditorias e faturamento do SUS.

---

## Funcionalidades

* Leitura Posicional (FWF): Extração exata dos campos com base no layout do DATASUS.
* Conversão de Valores: Tratamento automático das casas decimais dos valores (vl_sh, vl_sa, vl_sp).
* Cruzamento de Tabelas: Integração da tb_procedimento com a tb_financiamento.
* Saída para Excel: Exportação em formato .csv (separado por ; e encoding utf-8-sig).

## Pré-requisitos

Você precisará do Python instalado e da biblioteca Pandas. Instale via terminal usando o comando: pip install pandas

## Como Usar

1. Clone o repositório para sua máquina.
2. Execute o script uma vez para que ele crie as pastas automaticamente.
3. Cole os arquivos tb_procedimento.txt e tb_financiamento.txt dentro da pasta dados_Sigtap.
4. Execute o script novamente para gerar o relatório consolidado na pasta relatorios/tabela_sigtap_completa.csv.

## Tecnologias

* Python
* Pandas