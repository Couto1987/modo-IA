import csv
import os

def criar_e_salvar_csv():
    """
    Cria dados de pessoas (nome, idade, cidade) e salva em um arquivo CSV 
    com o nome escolhido pelo usuário. Trata erros ao salvar o arquivo.
    """
    
    # Dados de exemplo no formato tabular
    dados_pessoas = [
        ['Nome', 'Idade', 'Cidade'],
        ['Alice Souza', 28, 'São Paulo'],
        ['Bruno Costa', 35, 'Rio de Janeiro'],
        ['Carla Lima', 22, 'Rio de Janeiro'],
        ['Daniel Santos', 41, 'Porto Alegre']
    ]
    
    print("💾 Gerador de Arquivos CSV de Pessoas 👩‍💻")
    print("---")
    
    # 1. Pede o nome do arquivo ao usuário
    nome_arquivo = input("Digite o nome do arquivo CSV para salvar (ex: pessoas.csv): ").strip()

    # Adiciona a extensão .csv se o usuário não a colocou
    if not nome_arquivo.lower().endswith('.csv'):
        nome_arquivo += '.csv'
        
    print(f"\nTentando salvar os dados em: {nome_arquivo}...")

    # 2. Tratamento de Erros: A função principal da sua requisição
    try:
        # Abrindo o arquivo para escrita ('w') com o gerenciador de contexto 'with'
        # O 'with' garante que o arquivo será fechado automaticamente, mesmo se ocorrer um erro.
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            
            # Cria o objeto de escrita CSV
            escritor = csv.writer(arquivo_csv)
            
            # Escreve todas as linhas dos dados no formato tabular
            escritor.writerows(dados_pessoas)
        
        # 3. Mensagem de Sucesso
        print(f"\n✅ Sucesso!")
        print(f"O arquivo '{nome_arquivo}' foi criado e salvo com sucesso na pasta atual.")
        
    except IOError as e:
        # Captura erros de I/O, que incluem problemas de permissão 
        print("\n🚨 **FALHA AO SALVAR O ARQUIVO!**")
        print("Ocorreu um erro ao tentar escrever no disco.")
        print("Verifique se você tem permissão de escrita para este local ou se o nome do arquivo é válido.")
        print(f"Detalhe do erro: {e}")
        
    except Exception as e:
        # Captura qualquer outro erro inesperado
        print("\n⚠️ **OCORREU UM ERRO INESPERADO.**")
        print(f"Detalhe do erro: {e}")

# --- Execução do Programa ---
criar_e_salvar_csv()