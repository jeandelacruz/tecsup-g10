# Try Except

try:
    dividendo = int(input("Ingresa el dividendo: "))
    division = 5 / dividendo
    print(division)
except (TypeError, ValueError):
    print('El valor de dividendo no se esta formateando a numero')
except ZeroDivisionError:
    print('El valor ingresado en dividendo no puede ser cero')
except Exception as e: # alias
    print(e.__class__)
    print('Ocurrio un error, contacte con soporte.')
