# ==========================================================
# Script Python para Registro de Notas e Cálculo da Média
# ==========================================================

def calcular_media_turma():
    """
    Função principal que coleta as notas e calcula a média.
    """
    print("🎓 CALCULADORA DE MÉDIA DA TURMA 🎓")

    
    notas = []
    
   
    while True:
        try:
            
            num_alunos = int(input("\nQuantos alunos (notas) você deseja registrar? "))
            
            if num_alunos <= 0:
                print("O número de alunos deve ser maior que zero. Tente novamente.")
                continue  
            break 
            
        except ValueError:
            
            print("🚨 Entrada inválida. Por favor, digite um número inteiro.")

    print("-" * 30)

    
    for i in range(num_alunos):
        while True:
            try:
               
                nota_aluno = float(input(f"Digite a nota do aluno {i + 1}: "))
                
               
                if nota_aluno < 0 or nota_aluno > 10:
                    print("Nota fora do intervalo esperado (0 a 10). Por favor, corrija.")
                    continue
                    
               
                notas.append(nota_aluno)
                break
                
            except ValueError:
                
                print("🚨 Entrada inválida. Por favor, digite um valor numérico para a nota.")

    # Verifica se há notas para calcular
    if not notas:
        print("\nNenhuma nota foi registrada. Não é possível calcular a média.")
        return 
        
    # --- Cálculo da Média ---
    
    # 1. Soma todas as notas da lista
    soma_das_notas = sum(notas)
    
    # 2. Obtém o número total de notas
    total_alunos = len(notas)
    
    
    media_turma = soma_das_notas / total_alunos
    
    
    
    print("\n" + "=" * 30)
    print("✅ RESULTADO DO CÁLCULO")
    print(f"Total de notas registradas: {total_alunos}")
    print(f"Soma total das notas: {soma_das_notas:.2f}")
    
    print(f"Média da turma: {media_turma:.2f}") 
    print("=" * 30)

if __name__ == "__main__":
    calcular_media_turma()