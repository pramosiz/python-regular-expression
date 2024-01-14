import re 

# Resumen de las expresiones regulares:
# https://cheatography.com/davechild/cheat-sheets/regular-expressions/

regex = r"m" # Busca exactamente la letra m
result = re.findall(regex, "Mi nombre es Pablo Ramos")  # findall: busca en toda la cadena
print("Prueba 1: ", result)  # Ha encontrado 1 coincidencia

result = re.match(regex, "Mi nombre es Pablo Ramos")  # match: busca al principio
print("Prueba 2: ", result)  # No ha encontrado ninguna coincidencia

regex = r"(P|p)ablo+" # Busca la palabra "Pablo" o "pablo" o "Pabloooo" o "Pabloooooo" o "Pabloooooooooooooo"   
result = re.findall(regex, "Mi nombre es Pablo Ramos") 
print("Prueba 3: ", result)  # Ha encontrado 1 coincidencia (P)

regex = r"(M|m)mmm+"   
result = re.search(regex, "La comida estaba mmmmmmuy rica") # search: busca en toda la cadena
print("Prueba 4: ", result)  # Ha encontrado 1 coincidencia (mmmmmm) y de qué posición a qué posición

regex = r"(M|m)+" # + es para que busque 1 o más veces
result = re.search(regex, "mmmmmmMMMMmmmmMMm")
print("Prueba 5: ", result)  # Ha encontrado 1 coincidencia (mmmmmmMMMMmmmmMMm) y de qué posición a qué posición

regex = r"(M|m)+$" # $ es para que busque al final de la cadena
result = re.search(regex, "mmmmmmMMMMmmmmMMm Pablo mmmMMMmmM")
print("Prueba 6: ", result)  # Sólo encuentra las M y m que están al final de la cadena

regex = r"^(M|m)+" # ^ es para que busque al principio de la cadena
result = re.search(regex, "mmmmmmMMMMmmmmMMm Pablo mmmMMMmmM")
print("Prueba 7: ", result)  # Sólo encuentra las M y m que están al principio de la cadena

regex = r"a..o" # . es para que busque cualquier caracter
result = re.search(regex, "mmmmmmMMMMmmmmMMm Pablo mmmMMMmmM")
print("Prueba 8: ", result)

regex = r"((M|m)+ .{5} (M|m)+)" # .{5} es para que busque cualquier caracter 5 veces
result = re.search(regex, "mmmmmmMMMMmmmmMMm Pablo mmmMMMmmM")
print("Prueba 9: ", result)

regex = r"((M|m)+ [a-z]{5,8} (M|m)+)" # [a-z] es para que busque cualquier caracter de la a a la z
result = re.search(regex, "mmmmmmMMMMmmmmMMm pablo mmmMMMmmM")
print("Prueba 10: ", result)

regex = r"((M|m)+ [a-zA-Z]{5,8} (M|m)+)" # [a-zA-Z] es para que busque cualquier caracter de la a a la z y de la A a la Z
result = re.search(regex, "mmmmmmMMMMmmmmMMm Pablo mmmMMMmmM")
print("Prueba 11: ", result)

regex = r"((M|m)+ [a-zA-Z0-9]{5,8} (M|m)+)" # [0-9] es para que busque cualquier caracter de la 0 a la 9
result = re.search(regex, "mmmmmmMMMMmmmmMMm Pablo12 mmmMMMmmM")
print("Prueba 12: ", result)

regex = r"((http(s?)://(www\.)?)|www\.)\w{3,}\.[a-z]{2,3}$"
result = re.search(regex, "https://www.google.es")
print("Prueba 13: ", result)

regexEmail = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
# Busca desde el principio hasta el final
# [a-zA-Z0-9._%+-]+: busca cualquier caracter de la a a la z, de la A a la Z, del 0 al 9, el punto, el guión bajo, el porcentaje, el signo más y el guión
# + es para que busque 1 o más veces
# @: busca la arroba
# [a-zA-Z0-9.-]+: busca cualquier caracter de la a a la z, de la A a la Z, del 0 al 9, el punto y el guión
# \.: busca el punto
# [a-zA-Z]{2,}: busca cualquier caracter de la a a la z y de la A a la Z, 2 o más veces

regexIBAN = r"^[A-Z]{2}\d{2}[A-Z0-9]{4}\d{7}([A-Z0-9]?){0,16}$"
# Busca desde el principio hasta el final
# [A-Z]{2}: busca cualquier caracter de la A a la Z, 2 veces
# \d{2}: busca cualquier caracter del 0 al 9, 2 veces
# [A-Z0-9]{4}: busca cualquier caracter de la A a la Z y del 0 al 9, 4 veces
# \d{7}: busca cualquier caracter del 0 al 9, 7 veces
# ([A-Z0-9]?){0,16}: busca cualquier caracter de la A a la Z y del 0 al 9, 0 o 16 veces

