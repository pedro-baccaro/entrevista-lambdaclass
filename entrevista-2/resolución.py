import re

# Recibe un string de letras mayusculas y separa los grupos consecutivos de letras iguales ("AAABB" -> ["AAA", "BB"])
def split_letters(string):
    pattern = re.compile(r"(([A-Z])\2*)") # La expresión regular matchea con una letra mayúscula seguida por una cantidad arbitraria (o 0) de letras iguales, capturando la secuencia entera en un primer grupo y la primera letra en un grupo 2
    return [match[0] for match in pattern.findall(string)] # Nos interesa solo el primer grupo capturado de cada match, el 2do solo se usa dentro de la expresión

def run_length_encode(string):
    output = ""
    groups = split_letters(string) 
    for group in groups: output += group[0] + str(len(group)) # Si tengo groups = ["AAA", "BB"], en cada uno me quedo con la primera letra y la longitud (A3, B2)
    return output

string = input("Input a string: ").upper()
print(run_length_encode(string))