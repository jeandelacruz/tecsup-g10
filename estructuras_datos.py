## Tipos: Mutables e Inmutables
## Listas -> Array [] | Mutable -- list

# Obtener un valor de una lista, debemos hacerlo por el indice (posición)
# n - 1   1 - 1 = 0 | 2 - 1 = 1 | 3 - 1 = 2
# ["", 1, None, True, [1, 2, 3]]
alumnos = ["Arnold", "Alfredo", "Anthony"]
print(f'inicio: {alumnos}')

# Funciones
# append -> Agregar un valor mas a una lista
alumnos.append("Diego")
print(f'append: {alumnos}')

# insert -> Agrega un valor definiendo la posición
alumnos.insert(1, "Elvia")
print(f'insert: {alumnos}')

# index -> Devuelve la posición del valor a buscar
posicion_anthony = alumnos.index("Anthony")
print(f'La posición (indice) de Anthony es: {posicion_anthony}')

# extend -> Unir 2 listas
alumnos_nuevos = ["Emily", "Julio", "Ivan", "Jack"]
alumnos.extend(alumnos_nuevos)
print(f'extend: {alumnos}')

# remove -> Remover un valor de la lista, la primera que encuentra
alumnos.remove("Julio")
print(f'remove: {alumnos}')

# count -> Retorna las veces que existe el mismo valor
arnold_veces = alumnos.count("Arnold")
print(f'count: {arnold_veces}')

# pop -> Remueve el valor de una lista, segun su indice (posicion)
alumnos.pop(2)
print(f'pop: {alumnos}')

# Cuantos valores hay en una lista
print(f'Total de alumnos: {len(alumnos)}')

print("#####################################################################")

# Tupla - Inmutable -- tuple
alumnos = ("Anthony", "Arnold", "Blas", "Cristian")

# count -> Contar la cantidad de valores que hay en la tupla
blas_veces = alumnos.count("Blas")
print(f'count: {blas_veces}')

# index -> Devuelve la posición (indice) del valor a buscar
posicion_christian = alumnos.index("Cristian")
print(f'La posición (indice) de Cristian es: {posicion_christian}')

###################
# Convertimos tupla a una lista (Para añadir un valor a una tupla)
print(f'Tipo de Dato: {type(alumnos)}')
print(alumnos)
alumnos_lista = list(alumnos)
alumnos_lista.append("Emily")

alumnos = tuple(alumnos_lista)
print(f'Tipo de Dato: {type(alumnos)}')
print(alumnos)

print("#####################################################################")

###################
# Diccionario -> clave => valor (key => value)
persona = {
    "nombres": "Nixon Guevara",
    "edad": 20,
    "hobbies": ["Futbol", "Nadar", "Jugar"]
}

print(f'Nombre de la persona: {persona["nombres"]}')
print(f'Segundo Hobby: {persona["hobbies"][1]}')
# print(persona.nombres) -> Instanciar una clase - objeto

## 2º Forma
#print(persona["cursos"])
# get -> Busca el valor con la clave mencionada, y retornara el valor
print(persona.get("cursos"))
