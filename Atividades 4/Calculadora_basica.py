# --- 1. Definindo as Funções das Operações ---

def adicionar(x, y):
    """Retorna a soma de x e y"""
    return x + y

def subtrair(x, y):
    """Retorna a subtração de y de x"""
    return x - y

def multiplicar(x, y):
    """Retorna o produto de x e y"""
    return x * y

def dividir(x, y):
    """
    Retorna a divisão de x por y.
    Inclui uma verificação para evitar a divisão por zero.
    """
    if y == 0:
        return "Erro: Divisão por zero não é permitida!"
    return x / y

# --- 2. Interface e Entrada de Dados ---

print("Selecione a operação que deseja fazer:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")


escolha = input("Digite sua escolha (1/2/3/4): ")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
except ValueError:
    print("🚨 Erro: Entrada inválida. Por favor, digite apenas números.")
    exit()

# --- 3. Executando a Operação Escolhida ---

if escolha == '1':
    resultado = adicionar(num1, num2)
    operacao_simbolo = '+'
elif escolha == '2':
    resultado = subtrair(num1, num2)
    operacao_simbolo = '-'
elif escolha == '3':
    resultado = multiplicar(num1, num2)
    operacao_simbolo = '*'
elif escolha == '4':
    resultado = dividir(num1, num2)
    operacao_simbolo = '/'
else:
    
    print("🚫 Opção inválida. Tente rodar o programa novamente e escolha 1, 2, 3 ou 4.")
    
    exit()

# --- 4. Imprimindo o Resultado ---

if operacao_simbolo != '/': 
    print(f"\n{num1} {operacao_simbolo} {num2} = {resultado}")
elif num2 != 0:
    print(f"\n{num1} {operacao_simbolo} {num2} = {resultado}")
else:
   
    print(f"\n{resultado}")


print("\nValeu por usar a nossa calculadora! 😉")