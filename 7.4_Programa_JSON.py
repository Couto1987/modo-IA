import json
import os

# 1. Dados que serão salvos no arquivo JSON
dados_pessoa = {
    "nome": "João da Silva",
    "idade": 30,
    "cidade": "Florianópolis",
    "hobbies": ["programar", "caminhar", "ler"]
}

def salvar_dados_json(dados, nome_arquivo="dados_pessoa.json"):
    """
    Salva um dicionário Python em um arquivo JSON.
    Trata erros de escrita/permissão.
    """
    print(f"\nTentando salvar os dados em: {nome_arquivo}...")
    
    try:
        # Abre o arquivo para escrita  com o gerenciador
        # indent=4 formata o JSON de forma legível
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4)
            
        print(f"✅ Sucesso! Dados salvos em '{nome_arquivo}'.")
        return True

    except IOError as e:
        # Captura erros de I/O (permissão, disco cheio, etc.)
        print("\n🚨 **FALHA AO SALVAR O ARQUIVO!**")
        print("Ocorreu um erro de escrita. Verifique permissões ou o nome do arquivo.")
        print(f"Detalhe do erro: {e}")
        return False
    except Exception as e:
        # Captura outros erros inesperados
        print(f"\n⚠️ **ERRO INESPERADO AO SALVAR:** {e}")
        return False


def ler_dados_json(nome_arquivo="dados_pessoa.json"):
    """
    Lê um arquivo JSON e exibe o dicionário na tela.
    Trata o erro de arquivo não encontrado.
    """
    print(f"\nTentando ler os dados de: {nome_arquivo}...")
    
    try:
        # Abre o arquivo para leitura
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            #lê o JSON e converte para um dicionário Python
            dados_lidos = json.load(arquivo)
            
        print("\n✅ Sucesso na leitura! Dados do Arquivo JSON:")
        print("---------------------------------")
        print(f"👤 Nome: {dados_lidos['nome']}")
        print(f"🎂 Idade: {dados_lidos['idade']}")
        print(f"🏙️ Cidade: {dados_lidos['cidade']}")
        print(f"Interesses: {', '.join(dados_lidos['hobbies'])}")
        print("---------------------------------")
        
    except FileNotFoundError:
        # 🚨 Tratamento de Erro: Arquivo não Encontrado
        print("\n🚨 **ERRO DE LEITURA! Arquivo não Encontrado.**")
        print(f"Não foi possível localizar o arquivo '{nome_arquivo}'. Salve-o primeiro.")
        
    except json.JSONDecodeError:
        # Captura erro se o arquivo não for um JSON válido
        print("\n⚠️ **ERRO DE DECODIFICAÇÃO JSON.**")
        print("O arquivo existe, mas está corrompido ou não está em formato JSON válido.")
        
    except Exception as e:
        # Captura outros erros
        print(f"\n⚠️ **ERRO INESPERADO AO LER:** {e}")


# --- Execução do Programa ---

nome_do_arquivo = "perfil.json"

print("--- Começando a Operação de JSON ---")

# 1. Salvar os dados (Escrita)
if salvar_dados_json(dados_pessoa, nome_do_arquivo):
    # 2. Se salvou com sucesso, tenta ler o mesmo arquivo (Leitura)
    ler_dados_json(nome_do_arquivo)
else:
    
    print("Operação de leitura cancelada devido à falha na escrita.")

print("\n--- Fim da Operação ---")