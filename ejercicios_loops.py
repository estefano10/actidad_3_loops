def ejercicio_1_for_en_vector():
    nombres = ["lucas", "franco", "luciano", "malena", "jonatan", "luciano", "rodrigo", "maria sol", "enzo", "milena"]
    for nombre in nombres:
        print(nombre)


ejercicio_1_for_en_vector()


def ejercicio_2_for_en_vector():
    nombres = ["lucas", "franco", "luciano", "malena", "jonatan", "luciano", "rodrigo", "maria sol", "enzo", "milena"]
    size = len(nombres)
    for i in range(0, size):
        print(f'el nombre en la posicion {i} es: {nombres[i]} ')


ejercicio_2_for_en_vector()


def ejercicio_3_for_en_vector():
    nombres = ["lucas", "franco", "luciano", "malena", "jonatan", "luciano", "rodrigo", "maria sol", "enzo", "milena"]
    size = len(nombres)
    for i in range(4, size):
        print(nombres[i])
    print(f'el valor en la posicion 1 es: {nombres[1]}')


ejercicio_3_for_en_vector()


def ejercicio_4_while():
    nota = float(int(input('ingrese una nota o presione 0 para finalizar: ')))
    acum = 0
    contador = 0
    while nota != 0:
        acum = acum + nota
        contador = contador + 1
        nota = float(int(input('ingrese una nota o presione 0 para finalizar: ')))

    print(acum / contador)

    if contador != 0:
        print(f'el promedio general del curso es: {acum / contador}')
    else:
        print('no se ha ingresado ninguna nota')



ejercicio_4_while()
