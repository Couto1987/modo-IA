import pandas as pd
import numpy as np 

def analisar_tempo_execucao(nome_arquivo):
    """
    Lê um arquivo CSV usando pandas, calcula a média e a mediana da coluna 
    'tempo_execucao', e trata erros de arquivo ou leitura.
    """
    print(f"\nTentando ler o arquivo: {nome_arquivo}...")
    
    try:
        # 1. Tenta ler o arquivo CSV
        df = pd.read_csv(nome_arquivo)
        
        coluna = 'tempo_execucao'

        # 2. Verificação de Segurança
        if coluna not in df.columns:
            print(f"\n❌ Erro de Leitura: A coluna '{coluna}' não foi encontrada no arquivo CSV.")
            print(f"Colunas disponíveis: {list(df.columns)}")
            return

        # 3. Calcula a média e a mediana
        media = df[coluna].mean()
        mediana = df[coluna].median()
        
        # 4. Exibe os resultados
        print("\n✅ Sucesso! Estatísticas da Execução:")
        print("---")
        print(f"📈 **Média (Tempo Médio):** {media:.2f} segundos")
        print(f"📊 **Mediana (Valor Central):** {mediana:.2f} segundos")
        print("---")
        
    except FileNotFoundError:
        # 🚨 Tratamento de Erro: Arquivo não Encontrado
        print("\n🚨 **ERRO! Arquivo não Encontrado.**")
        print(f"Não foi possível localizar o arquivo '{nome_arquivo}'.")
        print("Verifique se o nome do arquivo está correto e se ele está no mesmo diretório do programa.")
        
    except Exception as e:
        # ⚠️ Tratamento de Erro: Qualquer outro problema
        print("\n⚠️ **ERRO NA LEITURA OU PROCESSAMENTO DO ARQUIVO.**")
        print(f"Ocorreu um erro inesperado ao processar o arquivo: {e}")


