# IF - ELSE

# numero = 10
# 
# if numero == 10:
#     pass
# elif numero < 5:
#     pass
# else:
#     pass

edad = int(input("Ingresa tu edad: "))

# if edad >= 18:
#     print('Eres mayor de edad')
# else:
#     print('Eres menor de edad')

# Operador ternario
## edad >= 18 ? 'Eres mayor de edad' : 'Eres menor de edad' -> Javascript
print('Eres mayor de edad' if edad >= 18 else 'Eres menor de edad')
