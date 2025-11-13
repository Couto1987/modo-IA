import re

def verificar_seguranca_senha(senha):
    """
    Verifica se a senha atende aos critérios básicos de segurança:
    1. Pelo menos 8 caracteres.
    2. Contém pelo menos um número.

    Args:
        senha (str): A string da senha a ser verificada.

    Returns:
        tuple: (bool, str) - Onde o bool indica se é segura e o str é a mensagem de feedback.
    """
    
    # ----------------------------------------------------
    # Variáveis para armazenar o resultado de cada critério
    # ----------------------------------------------------
    
    # a) Critério de Comprimento (mínimo 8 caracteres)
    tem_oito_caracteres = len(senha) >= 8
    
    # b) Critério de Número (deve conter pelo menos um dígito de 0 a 9)
    tem_numero = re.search(r'\d', senha) is not None
    
    if tem_oito_caracteres and tem_numero:
        return True, "✅ Sucesso! A senha atende a todos os critérios de segurança básicos."
    
    
    else:
        mensagem_erro = "🚫 Falha de Segurança. A senha não atende aos seguintes critérios:\n"
        
        if not tem_oito_caracteres:
            
            mensagem_erro += f"  - Deve ter pelo menos 8 caracteres (encontrado: {len(senha)}).\n"
            
        if not tem_numero:
            mensagem_erro += "  - Deve conter pelo menos um número (0-9).\n"
            
        return False, mensagem_erro

# ==========================================================
# Exemplo de Uso Interativo
# ==========================================================

if __name__ == "__main__":
    
    print("--------------------------------------------------")
    print("           VALIDADOR DE SENHA SIMPLES")
    print("Critérios: >= 8 caracteres e pelo menos 1 número.")
    print("--------------------------------------------------")
    
    
    while True:
        try:
            
            senha_digitada = input("\nDigite a senha para verificar (ou 'sair' para encerrar): ")
            
            if senha_digitada.lower() == 'sair':
                print("\nEncerrando o validador. Até mais!")
                break
            segura, feedback = verificar_seguranca_senha(senha_digitada)
            
            print("\n--- Resultado ---")
            print(feedback)
            
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            break