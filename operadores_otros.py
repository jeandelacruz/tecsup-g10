# Asignación multiple
n_uno, n_dos = 10, 20

## Operadores de comparación
# ==, es igual que
# !=, diferente a
# <, menor a
# <=, menor igual a
# >, mayor a
# >=, mayor igual a

print(f'Son iguales: {n_uno == n_dos}')
print(f'Son diferentes: {n_uno != n_dos}')

## Operadores logicos
# && -> and
# || -> or
# ! -> not
print(not(n_uno > n_dos) and n_dos == 20)

## Operadores de identidad
# is -> es
# is not -> no es
frutas = None
print(frutas is None)

## Ejercicios
# Crear un archivo llamado temperatura.py y dentro vamos
# a convertir Farenheit a Celsius
# Formula:
# celsius = (farenheit - 32) / 1.8
