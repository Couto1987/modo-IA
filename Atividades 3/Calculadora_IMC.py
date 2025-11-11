# ==========================================================
# 2. CALCULADORA E CLASSIFICADOR DE IMC
# ==========================================================
print("\n" + "=" * 30)
print("2. CALCULADORA DE IMC")
print("=" * 30)

try:
    # Solicita o peso e a altura
    peso = float(input("Insira seu peso (em kg, ex: 75.5): "))
    altura = float(input("Insira sua altura (em metros, ex: 1.75): "))

    if peso <= 0 or altura <= 0:
        print("\nERRO: Peso e altura devem ser valores positivos.")
    else:
        # Fórmula do IMC: Peso / (Altura * Altura)
        imc = peso / (altura ** 2)

        # Lógica de Classificação do IMC
        if imc < 18.5:
            classificacao_imc = "Abaixo do peso"
        elif imc < 25:
            classificacao_imc = "Peso normal"
        elif imc < 30:
            classificacao_imc = "Sobrepeso"
        else:
            classificacao_imc = "Obeso"

        # Exibe o resultado, arredondado para duas casas decimais
        print("\n--- Resultado ---")
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao_imc}")

except ValueError:
    print("\nERRO: Por favor, insira apenas números válidos para peso e altura.")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")