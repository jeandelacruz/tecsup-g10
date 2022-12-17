# Importación de modulos
# Siempre definir lo que se va a usar
# import variables

from variables import nombre, apellido_paterno
from camelcase import CamelCase as ClaseCamel

instancia = ClaseCamel()

print(instancia.hump("julio martin"))
print(nombre)
print(apellido_paterno)
