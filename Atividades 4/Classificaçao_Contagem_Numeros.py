# ==========================================================
# Script Python para Classificação e Contagem de Números
# ==========================================================

def analisar_numeros():
    """
    Permite ao usuário digitar números continuamente,
    classifica cada um como par ou ímpar e conta o total de cada tipo.
    """
    print("✨ ANALISADOR DE NÚMEROS PARES E ÍMPARES ✨")
    print("---------------------------------------------------------")
    print("Digite números um por um. Digite 'fim' para ver o resultado.")
    print("---------------------------------------------------------")
    
    total_pares = 0
    total_impares = 0
    
    while True:
        entrada = input("Digite um número inteiro (ou 'fim'): ").lower().strip()
        
        
        if entrada == 'fim':
            break
            
        try:

            numero = int(entrada)
            
            # --- Lógica de Classificação ---
            
            if numero % 2 == 0:
                print(f"  -> O número {numero} é PAR.")
                total_pares += 1 
            
            else:
                print(f"  -> O número {numero} é ÍMPAR.")
                total_impares += 1 
                
        except ValueError:
            
            print("🚨 Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")
    total_geral = total_pares + total_impares
    
    print("\n" + "=" * 30)
    
    if total_geral == 0:
        print("Nenhum número válido foi inserido para análise.")
    else:
        print("📊 RESULTADO DA ANÁLISE 📊")
        print(f"Total de números analisados: {total_geral}")
        print("-" * 30)
        print(f"Contagem de PARES: {total_pares}")
        print(f"Contagem de ÍMPARES: {total_impares}")  
    print("=" * 30)
    print("Análise concluída!")

if __name__ == "__main__":
    analisar_numeros()