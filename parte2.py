columnSort = int(input())

first = open("first.csv", 'r')
firstLines = first.read().splitlines() # Lista de cada renglon en first.csv
headers = firstLines[0] + "\n" # Me guardo los headers para incluirlos en el output, agrego \n porque write() no lo agrega
firstLines = firstLines[1:] # Saco los headers de firstLines para que solo contenga entradas de la tabla

second = open("second.csv", 'r') # Lista de cada renglon en second.csv
secondLines = second.read().splitlines()[1:] # Como ya tengo los headers hago todo en un paso

output = open("out.csv", 'w')
personas = firstLines + secondLines # Junto todas las entradas de la tabla en una lista
output.write(headers) 
personas.sort(key=lambda persona: persona.split(',')[columnSort].strip()) # Ordeno la lista en base a la columna especificada por el usuario, uso strip() por si hay espacios entre las comas
output.write("\n".join(personas))

#Cierro los archivos
first.close()
second.close()
output.close()