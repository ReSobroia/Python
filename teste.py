# Comparação simples entre dois números
num1 = 10
num2 = 20

if num1 < num2:
    print(f"{num1} é menor que {num2}")
elif num1 > num2:
    print(f"{num1} é maior que {num2}")
else:
    print(f"{num1} é igual a {num2}")

print("\n--- Operadores de Comparação ---")
print(f"{num1} == {num2}: {num1 == num2}")  # Igual
print(f"{num1} != {num2}: {num1 != num2}")  # Diferente
print(f"{num1} < {num2}: {num1 < num2}")    # Menor
print(f"{num1} > {num2}: {num1 > num2}")    # Maior
print(f"{num1} <= {num2}: {num1 <= num2}")  # Menor ou igual
print(f"{num1} >= {num2}: {num1 >= num2}")  # Maior ou igual

# Comparando múltiplos números
print("\n--- Comparar 3 números ---")
a, b, c = 5, 15, 10

maior = max(a, b, c)
menor = min(a, b, c)

print(f"Maior: {maior}")
print(f"Menor: {menor}")

# Comparar com intervalo
print("\n--- Verificar intervalo ---")
numero = 25
if 10 <= numero <= 50:
    print(f"{numero} está entre 10 e 50")
else:
    print(f"{numero} está fora do intervalo")