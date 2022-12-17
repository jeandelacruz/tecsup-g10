# for -> for in

meses = ["Enero", "Febrero", "Marzo", "Abril"]

## Obtener el valor
# for mes in meses: # for (const mes in meses) {}
#     print(mes)

## Obtener el indice y el valor
# print(list(enumerate(meses)))
# for indice, mes in enumerate(meses): # [(0, Enero), (1, Febrero)]
#     print(indice, mes)

# for(let i=0; i<10; i++) {} -> Javascript
# range -> recibi 3 argumentos (parametros)
# 1ª Desde donde empieza
# 2ª Hasta donde finaliza - Se toma por defecto si solo se ingresa un argumento
# 3ª De cuanto en cuanto incrementara

# for numero in range(1, 5, 2):
#     print(numero)

persona = {
    "nombres": "Nixon Guevara",
    "edad": 20,
    "hobbies": ["Futbol", "Nadar", "Jugar"]
}

# 1ª Forma
# for index in persona:
#     print(index, persona[index])

# 2º Forma
#for value in persona.values():
#    print(value)

# 3º Forma
#for index in persona.keys():
#    print(index)

#for key, value in persona.items():
#    print(key, value)

## Ejercicio 1
# Hallar cuantos son multiplos de 3 y de 5, de una lista.
# Si existe un  multiplo que sea de 3 y 5 a la vez, no se debe contabilizar.

#numeros = [1, 2, 5, 9, 12, 15, 10, 34, 67]
#
#multiplo_tres = 0
#multiplo_cinco = 0
### for - if - operador de asignación (+=) - operador aritmetico (%)
#
#for numero in numeros:
#    if numero % 3 == 0 and numero % 5 == 0:
#        continue
#    elif numero % 3 == 0:
#        multiplo_tres += 1
#    elif numero % 5 == 0:
#        multiplo_cinco += 1
#
#print(multiplo_tres, multiplo_cinco)

# While (Mientras)
edad = 28

#while edad > 18:
#    print(edad)
#    edad -= 1
#    
#    if edad == 21:
#        break

while True:
    print(edad)
    edad -= 1
    
    if edad <= 18:
        break

