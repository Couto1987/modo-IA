import random
import string

def gerar_senha_segura():
    """
    Gera uma senha aleatória com letras, números e símbolos,
    onde o usuário define o tamanho.
    """
    # 1. Combina todos os caracteres possíveis em um único conjunto
    caracteres_possiveis = string.ascii_letters + string.digits + string.punctuation
    
    # 2. Pede o tamanho da senha ao usuário e garante que é um número
    while True:
        try:
            tamanho = int(input("Qual o **tamanho** da senha que você deseja (ex: 12, 16)? "))
            
            if tamanho <= 0:
                print("O tamanho da senha deve ser um número inteiro **positivo**! Tente de novo.")
            else:
                break 
                
        except ValueError:
            
            print("Entrada inválida! Por favor, digite um **número** para o tamanho.")

    # 3. Gera a senha
    senha_lista = [random.choice(caracteres_possiveis) for _ in range(tamanho)]
    
    # 4. Mistura e Junta os caracteres
    random.shuffle(senha_lista)
    
    senha_final = "".join(senha_lista)
    
    return senha_final

# --- Execução do Programa ---
print("\n🔑 Gerador de Senhas Super Seguras! 🔑")
print("---")


nova_senha = gerar_senha_segura()


print("\n✨ Senha Gerada com Sucesso! ✨")
print(f"Sua nova senha de {len(nova_senha)} caracteres é: **{nova_senha}**")
print("Lembre-se de guardar essa belezinha em um lugar seguro (tipo um gerenciador de senhas)! 😉")