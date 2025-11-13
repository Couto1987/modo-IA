import datetime

def calcular_dias_de_vida():
    """
    Calcula quantos dias um indivíduo está vivo,
    com base na data de nascimento fornecida e na data atual.
    """
    print("--- 🎂 Calculadora de Idade em Dias 🎂 ---")
    print("Vamos descobrir quantos dias de aventuras você já viveu!")
    
    data_nascimento = None

    while data_nascimento is None:
        data_input = input("Por favor, digite sua data de nascimento (no formato DD/MM/AAAA): ")
        
        try:
            data_nascimento = datetime.datetime.strptime(data_input, "%d/%m/%Y").date()
        
        except ValueError:
            print(f"Ops! O formato '{data_input}' não é válido.")
            print("Tente novamente, use o formato DD/MM/AAAA (ex: 15/05/1990).")

    # 1. Obter a data atual do sistema
    data_hoje = datetime.date.today()

    if data_nascimento > data_hoje:
        print("\n🤔 Hã? Sua data de nascimento está no futuro!")
        print("Você ainda não nasceu. Tente novamente com uma data válida. 😅")
        return

    # 2. Calcular a diferença entre as datas
    diferenca = data_hoje - data_nascimento

    # 3. Extrair o número total de dias
    dias_vivos = diferenca.days
    
    # 4. Mostrar o resultado
    print("\n=======================================================")
    print(f"Data de Nascimento: {data_nascimento.strftime('%d/%m/%Y')}")
    print(f"Data de Hoje:       {data_hoje.strftime('%d/%m/%Y')}")
    print(f"-------------------------------------------------------")
    print(f"Você está vivo há um total de...")
    print(f"🎉 **{dias_vivos:,} dias** 🎉")
    print(f"=======================================================")

# Roda a função principal
if __name__ == "__main__":
    calcular_dias_de_vida()