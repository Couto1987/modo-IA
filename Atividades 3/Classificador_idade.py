print("=========================================")
print("1. CLASSIFICADOR DE IDADE")
print("=========================================")

try:
    # Solicita a idade do usuário e garante que seja um número inteiro
    idade = int(input("Por favor, insira sua idade: "))

    # Lógica de Classificação usando condicionais (if/elif/else)
    if idade < 0:
        classificacao = "Idade inválida. Por favor, insira um número positivo."
    elif idade <= 12:
        classificacao = "Criança"
    elif idade <= 17:
        classificacao = "Adolescente"
    elif idade <= 59:
        classificacao = "Adulto"
    else:
        # Se não caiu em nenhuma das categorias acima, só pode ser 60 ou mais
        classificacao = "Idoso"

    print(f"\nSua classificação de idade é: {classificacao}")

except ValueError:
    print("\nERRO: Idade deve ser um número inteiro. Tente novamente.")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")