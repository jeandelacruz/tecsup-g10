# function nombre(parametros) { }

# Función en python
# def nombreFuncion():
#    pass

# Función usando parametros (argumentos)
# def saludar(nombre):
#     print(f'Hola {nombre}, como estas?')
#
# saludar("Carlos")

# Función usando parametros con valores por defecto
def saludar(apellidos, nombre="Alfredo", edad=20):
    print(f'Hola {nombre} {apellidos} {edad}')

# saludar(apellidos="Rocca", edad=21)

# Ejercicio 1
# Crea una función que reciba 2 números, donde el primer número tenga un valor: 10 por defecto
# si la suma de dichos numeros es par, mostrar la mitad de la suma
# y si no lo es, mostrar la suma


def ejercicioUno(n_dos, n_uno=10):
    suma = n_uno + n_dos
    if suma % 2 == 0:
        print(suma / 2)
    else:
        print(suma)

# ejercicioUno(11)

# Funciones con multiparametros
# *args -> nos ayuda a recibir valores infinitos como argumentos,
# retornara o se obtendra una tupla con todos los valores
# Ejm: nombreFuncion("Valor1", "Valor2", ..... , "ValorX")


def alumnosInscritos(*args):
    for arg in args:
        print(arg)

# alumnosInscritos("Alfredo", "Arnold", "Carlos", "Cristian", "Diego", "Elvia")

# **kwargs -> nombreFuncion(valoruno=1, valordos=2, .... , valorx=x)


def cursosDeAlumnos(**kwargs):
    print(kwargs)


cursosDeAlumnos(curso_uno="Algebra", curso_dos="Aritmetica",
                curso_tres="Comunicación")
