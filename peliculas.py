# Función para agregar una pelicula a la lista
def agregar_pelicula(lista_peliculas, nombre_pelicula, calificaciones):
    lista_peliculas.append(nombre_pelicula)
    calificaciones.append(0)  # Todas las peliculas inician con calificacion 0
    print(f'La pelicula "{nombre_pelicula}" ha sido agregada.')

# Función para mostrar todas las películas de la lista
def mostrar_peliculas(lista_peliculas, calificaciones):
    if not lista_peliculas:
        print('No hay peliculas en la lista.')
    else:
        print('Lista de peliculas:')
        for index, nombre_pelicula in enumerate(lista_peliculas, start=1):
            calificacion = calificaciones[index - 1]
            print(f'{index}. {nombre_pelicula} - Calificación: {calificacion}')

        # pedir al usuario que elija una película para ver detalles
        try:
            opcion = int(input('Seleccione el numero de la pelicula que desea ver o (0 para volver al menu principal): '))
            if opcion == 0:
                return  # Regresar al menu principal si el usuario elige 0
            elif 1 <= opcion <= len(lista_peliculas):
                nombre_pelicula = lista_peliculas[opcion - 1]
                print(f'Ha seleccionado ver la pelicula "{nombre_pelicula}".')
                while True: # calificacion de la pelicula si el usuario quiere hacerlo 
                    opcion_gusto = input('¿Te gusto la pelicula? (s/n): ').strip().lower()
                    if opcion_gusto == 's':
                        calificacion_nueva = float(input(f'Ingrese la nueva calificacion para "{nombre_pelicula}" (1-5): '))
                        if calificacion_nueva < 1 or calificacion_nueva > 5:
                            print('La calificacion debe estar en el rango del 1 al 5.')
                        else:
                            calificaciones[opcion - 1] = calificacion_nueva
                            print(f'Se ha actualizado la calificacion de "{nombre_pelicula}" a {calificacion_nueva}.')
                        break
                    elif opcion_gusto == 'n':
                        print('Entendido, no se ha calificado la película.')
                        break
                    else:
                        print('Error: Ingrese unicamente "s" o "n".')
            else:
                print('Opción inválida. Seleccione un número válido de película.')
        except ValueError:
            print('Error: Ingrese un número válido.')

# funcion principal del programa
def main():
    peliculas = [
        "Batman",
        "Piratas del Caribe",
        "El secreto de sus ojos",
        "Taxi Driver"
    ]
    calificaciones = [0] * len(peliculas)  #  calificaciones con 0  cada película al inicio y al agregar alguna

    while True: # menu del programa
        print('\nMENU:')
        print('1. Agregar película')
        print('2. Mostrar películas')
        print('3. Salir')

        opcion = input('Seleccione una opción: ')

        try:
            opcion = int(opcion)
        except ValueError:
            print('Error: Ingrese un número válido.')
            continue

        if opcion == 1:
            nombre_pelicula = input('Ingrese el nombre de la película a agregar: ')
            agregar_pelicula(peliculas, nombre_pelicula, calificaciones)
        elif opcion == 2:
            mostrar_peliculas(peliculas, calificaciones)
        elif opcion == 3:
            print('¡Hasta luego!')
            break
        else:
            print('Opción inválida. Por favor, seleccione una opción válida.')

if __name__ == "__main__":
    main()
