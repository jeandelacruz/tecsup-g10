# Asignar variables
n_uno = 10
n_dos = 20

# Suma (+)
suma = n_uno + n_dos
print(f'La suma de {n_uno} y {n_dos} es igual a: {suma}')

# Resta (-)
resta = n_dos - n_uno
print(f'La resta de {n_dos} y {n_uno} es igual a: {resta}')

# Multiplicación (*)
multiplicacion = n_uno * n_dos
print(f'La multiplicación de {n_uno} y {n_dos} es igual a: {multiplicacion}')

# Potencia (**)
potencia = n_uno ** n_dos
print(f'La potencia de {n_uno} y {n_dos} es igual a: {potencia}')

# División (/)
division = n_dos / n_uno
print(f'La división de {n_dos} y {n_uno} es igual a: {division}')

# División Exacta (// - divmod(p, p_dos))
# Si el resultado por ejemplo es: 1.8, retornara 1 (como entero)
## 1ª Forma
# division_exacta = n_dos // n_uno

## 2ª Forma
division_exacta, residuo = divmod(n_dos, n_uno)
print(f'La división exacta de {n_dos} y {n_uno} es igual a: {division_exacta}')

# Residuo | Modulo (%)
## 1ª Forma
# residuo = n_dos % n_uno

## 2ª Forma
print(f'El residuo de {n_dos} entre {n_uno} es igual a: {residuo}')
