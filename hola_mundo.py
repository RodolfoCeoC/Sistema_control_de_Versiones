#Imprimiendo "hola mundo" en forma de lista y palabra por palabra

hi_world = input("Escribe 'hola mundo': ")

if hi_world != "hola mundo":
    print("!No escribiste la palabra correcta!","\nPrograma Terminado")
else:
    for hi in hi_world:
        print(hi)