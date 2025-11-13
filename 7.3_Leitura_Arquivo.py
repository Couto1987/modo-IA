import os

def ler_arquivo_e_exibir():
    """
    Pede o nome de um arquivo ao usuário, tenta lê-lo linha por linha 
    e exibe o conteúdo, tratando o erro de arquivo não encontrado.
    """
    
    print("📖 Leitor de Arquivos de Texto 🚀")
    print("---")
    
    # 1. Pede o nome do arquivo ao usuário
    nome_arquivo = input("Digite o **nome do arquivo** que você quer ler (ex: meu_texto.txt): ").strip()
    
    # 2. Tratamento de Erros: A chave para um programa robusto
    try:
        print(f"\nTentando abrir e ler o arquivo '{nome_arquivo}'...")
        print("--- Conteúdo do Arquivo ---")
        
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            
            # 3. Percorrendo cada linha do arquivo
            for numero_linha, linha in enumerate(arquivo, 1):
                # O 'strip()' remove quebras de linha e espaços em branco desnecessários
                print(f"[{numero_linha:02d}] {linha.strip()}")
        
        print("--- Fim do Arquivo ---")
        print("\n✅ Leitura concluída com sucesso!")
        
    except FileNotFoundError:
        # 🚨 Captura o erro específico de arquivo não encontrado
        print("\n🚨 **ERRO! Arquivo Não Encontrado.**")
        print(f"Não foi possível localizar o arquivo '{nome_arquivo}'.")
        print("Certifique-se de que o arquivo está na mesma pasta do programa e que o nome foi digitado corretamente.")
        
    except Exception as e:
        # ⚠️ Captura qualquer outro erro que possa ocorrer durante a leitura (ex: erro de permissão)
        print("\n⚠️ **OCORREU UM ERRO INESPERADO NA LEITURA.**")
        print(f"Detalhe do erro: {e}")

# --- Execução do Programa ---
ler_arquivo_e_exibir()