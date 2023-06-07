#Haga uso de la librería de expresiones regulares re
#import re
#Haciendo uso del método re.search, busque en la cadena "Esta es una lista de instrumentos musicales:piano, guitarra, xilofono", el
#patrón de búsqueda "x"
#imprima la posición del patrón de búsqueda y la coincidencia (match)
import re

cadena = "Esta es una lista de instrumentos musicales:piano, guitarra, xilofono"
patron = "x"

# Buscar el patrón en la cadena
result = re.search(patron, cadena)

# Verificar si se encontró un match
if result:
    # Mostrar la posición del patrón de búsqueda y la coincidencia
    print(f"Posición del patrón de búsqueda: {result.start()} - Coincidencia: {result.group()}")
else:
    print("No se encontró el patrón.")
    