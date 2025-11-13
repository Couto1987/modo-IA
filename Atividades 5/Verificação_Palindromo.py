import re 

def verificar_palindromo(frase: str) -> str:
    """
    Verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente),
    ignorando espaços, pontuação e acentuação.

    Parâmetros:
        frase (str): A palavra ou frase a ser verificada.

    Retorna:
        str: "Sim" se for palíndromo, "Não" caso contrário.
    """
    
    # 1. Normalização e Limpeza do Texto
    
    frase_min = frase.lower()
    
    texto_limpo = re.sub(r'[^a-z0-9]', '', frase_min)
    
    # 2. Inversão do Texto
    
    texto_reverso = texto_limpo[::-1]
    
    # 3. Comparação e Retorno
    
    if texto_limpo == texto_reverso:
        return "Sim"
    else:
        return "Não"

# ==========================================================
# Exemplos de Teste (Testando a função com diferentes casos)
# ==========================================================

if __name__ == "__main__":
    
    print("✨ VERIFICADOR DE PALÍNDROMOS ✨\n")
    print("--- Exemplos de Palíndromos (Deve retornar 'Sim') ---")
    print(f"1. 'ovo' -> Resultado: {verificar_palindromo('ovo')}")
    print(f"2. 'A gorda, droga!' -> Resultado: {verificar_palindromo('A gorda, droga!')}")
    print(f"3. 'A diva em Argel alegra-me a vida.' -> Resultado: {verificar_palindromo('A diva em Argel alegra-me a vida.')}")
    print(f"4. 'Roma me tem amor' -> Resultado: {verificar_palindromo('Roma me tem amor')}")
    
    print("\n--- Exemplos que NÃO são Palíndromos (Deve retornar 'Não') ---")
    print(f"5. 'Python' -> Resultado: {verificar_palindromo('Python')}")
    print(f"6. 'Socorram-me, subi no ônibus em Marrocos' -> Resultado: {verificar_palindromo('Socorram-me, subi no ônibus em Marrocos')}")
    
    print("\n-------------------------------------------------------------")
    frase_usuario = input("Digite uma palavra ou frase para verificar: ")
    resultado_usuario = verificar_palindromo(frase_usuario)
    print(f"\n'{frase_usuario}' é um palíndromo? -> {resultado_usuario}")