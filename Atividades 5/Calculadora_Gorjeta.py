# ==========================================================
# Função para calcular o valor da gorjeta
# ==========================================================

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta a ser deixada em um restaurante.

    Parâmetros:
        valor_conta (float): O valor total da conta.
        porcentagem_gorjeta (float): A porcentagem da gorjeta desejada (ex: 10 para 10%).

    Retorna:
        float: O valor da gorjeta calculada.
    """
    
    # 1. Converter a porcentagem para um valor decimal.
    
    fator_multiplicador = porcentagem_gorjeta / 100
    
    # 2. Multiplicar o valor da conta pelo fator.
    valor_gorjeta = valor_conta * fator_multiplicador
    
    return valor_gorjeta

# ==========================================================
# Exemplo de Uso Prático
# ==========================================================

if __name__ == "__main__":
    print("🍽️ CALCULADORA DE GORJETA 💸")
    
    # Valores de exemplo
    conta = 78.50
    gorjeta_desejada = 15.0 
    
    # Chamada da função
    valor_a_dar = calcular_gorjeta(conta, gorjeta_desejada)
    
    # Exibição do resultado
    print("-" * 35)
    print(f"Valor total da conta: R$ {conta:.2f}")
    print(f"Porcentagem de gorjeta: {gorjeta_desejada:.0f}%")
    print("-" * 35)
    print(f"O valor da gorjeta a ser pago é: R$ {valor_a_dar:.2f}")
    
    # Calculando o total final (apenas para completar o exemplo)
    total_final = conta + valor_a_dar
    print(f"Total a pagar (Conta + Gorjeta): R$ {total_final:.2f}")
    print("-" * 35)
    
    # Outro exemplo
    conta_2 = 120.00
    gorjeta_2 = 10.0
    valor_a_dar_2 = calcular_gorjeta(conta_2, gorjeta_2)
    print(f"\nExemplo 2: Gorjeta de {gorjeta_2:.0f}% em R$ {conta_2:.2f} é R$ {valor_a_dar_2:.2f}")