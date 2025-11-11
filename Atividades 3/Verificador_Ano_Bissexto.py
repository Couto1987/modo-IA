# ==========================================================
# 4. VERIFICADOR DE ANO BISSEXTO (LÓGICA BOOLEANA)
# ==========================================================
print("\n" + "=" * 40)
print("4. VERIFICADOR DE ANO BISSEXTO")
print("=" * 40)

try:
    ano = int(input("Insira um ano (ex: 2024): "))
    
    is_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    print("\n--- Resultado ---")
    if is_bissexto:
        print(f"O ano {ano} é BISSEXTO! 🎉")
    else:
        print(f"O ano {ano} NÃO é bissexto. 😔")

except ValueError:
    print("\nERRO: O ano deve ser um número inteiro.")
except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")