# ==========================================================
# 3. CONVERSOR DE TEMPERATURA (LÓGICA MAIS COMPLEXA)
# ==========================================================
print("\n" + "=" * 40)
print("3. CONVERSOR DE TEMPERATURA")
print("=" * 40)

def converter_temperatura():
    """Função para realizar a conversão de temperatura."""
    try:
        temp = float(input("Insira o valor da temperatura: "))
        origem = input("Unidade de origem (C, F ou K): ").upper()
        destino = input("Unidade de destino (C, F ou K): ").upper()

        unidades_validas = ['C', 'F', 'K']

        if origem not in unidades_validas or destino not in unidades_validas:
            print("\nERRO: Unidade de origem/destino inválida. Use apenas C, F ou K.")
            return

        if origem == destino:
            print(f"\nResultado: {temp:.2f} {origem} é igual a {temp:.2f} {destino}.")
            return
        temp_celsius = 0.0
        if origem == 'C':
            temp_celsius = temp
        elif origem == 'F':
            # F -> C: (F - 32) / 1.8
            temp_celsius = (temp - 32) / 1.8
        elif origem == 'K':
            # K -> C: K - 273.15
            temp_celsius = temp - 273.15
        temp_final = 0.0
        if destino == 'C':
            temp_final = temp_celsius
        elif destino == 'F':
            # C -> F: C * 1.8 + 32
            temp_final = temp_celsius * 1.8 + 32
        elif destino == 'K':
            # C -> K: C + 273.15
            temp_final = temp_celsius + 273.15

        print("\n--- Resultado da Conversão ---")
        print(f"Temperatura Convertida: {temp_final:.2f} {destino}")

    except ValueError:
        print("\nERRO: O valor da temperatura deve ser um número.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

converter_temperatura()