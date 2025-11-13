def calcular_preco_final():
    """
    Calcula o preço final de um produto após aplicar um desconto percentual,
    interagindo com o usuário e formatando o resultado.
    """
    print("--- 💰 Calculadora de Desconto Incrível! 💰 ---")
    
    
    # 1. Pedir o preço original
    while True:
        try:
            preco_original = float(input("Qual é o preço original do produto? R$ "))
            if preco_original <= 0:
                print("O preço deve ser um valor positivo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o preço.")

    # 2. Pedir a porcentagem de desconto
    while True:
        try:
            porcentagem_desconto = float(input("Qual é a porcentagem de desconto a aplicar (ex: 15 para 15%)? "))
            if porcentagem_desconto < 0 or porcentagem_desconto > 100:
                 print("A porcentagem deve estar entre 0 e 100. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a porcentagem.")

    #a - Cálculo de desconto: Calculando o valor
    
    valor_desconto = preco_original * (porcentagem_desconto / 100)
    
    #c - Formatação (intermediária): Arredondando o valor do desconto

    valor_desconto_formatado = round(valor_desconto, 2)
    
    #b - Preço final: Determinando o novo preço ---
    
    preco_final = preco_original - valor_desconto
    
    #c - Formatação: Arredondando o resultado final para 2 casas decimais ---
    preco_final_formatado = round(preco_final, 2)
    
    #d - Interação com usuário: Mostrando o resultado formatado ---
    
    print("\n--- ✅ Detalhes do Seu Desconto ---")
    print(f"Preço Original: R$ {preco_original:.2f}") # Formata o original também
    print(f"Desconto ({porcentagem_desconto}%) Aplicado: R$ {valor_desconto_formatado:.2f}")
    print(f"==========================================")
    print(f"**PREÇO FINAL A PAGAR: R$ {preco_final_formatado:.2f}**")
    print("==========================================")

# Chamando a função para rodar o programa
calcular_preco_final()