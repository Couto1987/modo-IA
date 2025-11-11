# Dados fornecidos
valor_reais = 100.00
taxa_dolar = 5.27
taxa_euro = 6.11

# Calculo da conversão
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

# Exibindo os resultados
print(f"\nValor Original: R$ {valor_reais:.2f}")
print("-" * 30)
print(f"Taxa Dólar: R$ {taxa_dolar:.2f}")
print(f"Taxa Euro: R$ {taxa_euro:.2f}")
print("-" * 30)
print(f"Conversão para Dólar: $ {valor_dolar:.2f}")
print(f"Conversão para Euro: € {valor_euro:.2f}")