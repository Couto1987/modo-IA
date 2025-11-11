# Dados da viagem
distancia_percorrida = 300  # em km
combustivel_gasto = 25      # em litros

# Cálculo do Consumo Médio (km/l)
consumo_medio = distancia_percorrida / combustivel_gasto

# Exibindo os dados
print(f"\nDistância Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} litros")
print("-" * 30)
# Resultado formatado com duas casas decimais
print(f"CONSUMO MÉDIO: {consumo_medio:.2f} km/l")