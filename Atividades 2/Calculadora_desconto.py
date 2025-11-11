nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

#Cálculo do desconto
fator_desconto = porcentagem_desconto / 100
valor_desconto = preco_original * fator_desconto

# Cálculo final
preco_final = preco_original * valor_desconto

# Exibindo todos os detalhes
print(f"\nProduto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto Aplicado: {porcentagem_desconto}%")
print("-" * 30)
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final (com desconto): R$ {preco_final:.2f}")