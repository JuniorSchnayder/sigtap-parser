import pandas as pd
import os

# ==============================================================
# 1. CONFIGURAÇÃO DE CAMINHOS (Caminhos Relativos para o GitHub)
# ==============================================================
# Define o diretório atual baseado na localização deste script
diretorio_atual = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'

# Pasta onde os arquivos TXT extraídos do SIGTAP devem ser colocados
pasta_origem = os.path.join(diretorio_atual, 'dados_Sigtap') 

# Onde o CSV final será criado
pasta_destino = os.path.join(diretorio_atual, 'relatorios')

# Montando os caminhos completos dos arquivos
arq_procedimento = os.path.join(pasta_origem, 'tb_procedimento.txt')
arq_financiamento = os.path.join(pasta_origem, 'tb_financiamento.txt')
arq_final = os.path.join(pasta_destino, 'tabela_sigtap_completa.csv')

# Cria as pastas automaticamente caso não existam no diretório
os.makedirs(pasta_origem, exist_ok=True)
os.makedirs(pasta_destino, exist_ok=True)

# ==============================================================
# 2. PROCESSAMENTO DA TABELA DE PROCEDIMENTOS
# ==============================================================

# Definição exata conforme o layout de tb_procedimento
specs_proc = [
    (0, 10),    # CO_PROCEDIMENTO (1-10)
    (10, 260),  # NO_PROCEDIMENTO (11-260)
    (282, 294), # VL_SH (283-294)
    (294, 306), # VL_SA (295-306)
    (306, 318), # VL_SP (307-318)
    (318, 320), # CO_FINANCIAMENTO (319-320)
    (330, 336)  # DT_COMPETENCIA (331-336)
]

cols_proc = ['co_procedimento', 'no_procedimento', 'vl_sh', 'vl_sa', 'vl_sp', 'co_financiamento', 'dt_competencia']

print("Verificando arquivos...")
if not os.path.exists(arq_procedimento) or not os.path.exists(arq_financiamento):
    print(f"\n[AVISO] Arquivos brutos não encontrados!")
    print(f"Por favor, coloque 'tb_procedimento.txt' e 'tb_financiamento.txt' dentro da pasta: {pasta_origem}")
    exit()

print("Lendo procedimentos...")
df_proc = pd.read_fwf(arq_procedimento, colspecs=specs_proc, names=cols_proc, encoding='latin1', dtype=str)

# Conversão de valores monetários (dividir por 100 para ter as casas decimais corretas)
for col in ['vl_sh', 'vl_sa', 'vl_sp']:
    df_proc[col] = df_proc[col].astype(float) / 100

# ==============================================================
# 3. PROCESSAMENTO DA TABELA DE FINANCIAMENTO
# ==============================================================

# Definição exata conforme o layout de tb_financiamento
specs_fin = [
    (0, 2),    # CO_FINANCIAMENTO (1-2)
    (2, 102),  # NO_FINANCIAMENTO (3-102) -> Ajustado para 100 caracteres
]

cols_fin = ['co_financiamento', 'no_financiamento']

print("Lendo financiamentos...")
df_fin = pd.read_fwf(arq_financiamento, colspecs=specs_fin, names=cols_fin, encoding='latin1', dtype=str)

# ==============================================================
# 4. CRUZAMENTO E EXPORTAÇÃO
# ==============================================================

print("Cruzando dados...")
# O merge garante que o nome do financiamento apareça ao lado do procedimento
df_final = pd.merge(df_proc, df_fin, on='co_financiamento', how='left')

# Salvar em CSV (formato excelente para Excel e auditorias)
df_final.to_csv(arq_final, index=False, sep=';', encoding='utf-8-sig')

print(f"\nConcluído com sucesso! Arquivo gerado em: {arq_final}")