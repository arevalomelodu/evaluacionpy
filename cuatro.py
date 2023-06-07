#Haga uso de la librería de expresiones regulares re
#Haciendo uso del método re.compile, establezca un patrón de búsqueda para los primeros 3 dígitos continuos dentro de
#una cadena de búsqueda
#Haciendo uso del método ex.search, establezca la cadena en la cual se realizará la búsqueda "PYTHON 3S UN L3NGU4J3 D3 PROGR4M4C1ÓN
#4MPL14M3NT3 UT1L1Z4DO 3N L4S 4PL1C4C1ON3S W3B, 3N D354RROLLO"
#Imprima el resultado= los tres dígitos consecutivos
import re

# Definir el patrón de búsqueda para encontrar los primeros 3 dígitos consecutivos
pattern = re.compile(r'\d{3}')

# Definir la cadena en la que se realizará la búsqueda
cadena = "PYTHON 3S UN L3NGU4J3 D3 PROGR4M4C1ÓN4MPL14M3NT3 UT1L1Z4DO 3N L4S 4PL1C4C1ÓN3S W3B, 3N D354RROLLO"

# Realizar la búsqueda utilizando el patrón de búsqueda
resultados = pattern.findall(cadena)

# Imprimir los resultados
print(resultados)