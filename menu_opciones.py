from time import sleep # Esta libreria sirve para pausar operaciones por x cantidad de tiempo en segundos

def menu_opciones():   

    #Saludo
    for char in "¡Bienvenid@ a tu asesor de estudio! \n        ¿Estas list@?\n \n":
        #sleep(0.05)
        print(char, end='')

    #Para acceder a la sesion correspondiente
    for char in "¿Eres estudiante o profesor?\n":
        sleep(0.05)
        print(char,end='')
    for opcion in ['1. Estudiante\n', '2. Profesor\n']:
        sleep (0.05)
        print(opcion, end='')

    es_profe_o_alumno = input('     ===>')

    #Para decirle a las demas funciones en que sesion estamos 
    global sesionProfesor
    global sesionEstudiante

    sesionProfesor = False
    sesionEstudiante = False

    if es_profe_o_alumno.lower() == 'estudiante':
  
        sesionEstudiante = True
        #Divisor para empezar menu
        print("="*20,"MENÚ","="*20,'\n')

        #Menu opciones
        for char in "Seleccione una opción porfavor\n \n":
            #sleep(0.05)
            print(char,end='')

        menu = ['1)   Tomar examen','2)   Simulacro de examen', '3)   Ver historial de examenes','4)  Repasar temas', '5)  Cerrar Sesión']

        for opcion in menu:
            print(opcion, '\n')

        global opcionEstudiante
        opcionEstudiante = input("  ===>")
    else: 

        sesionProfesor = True
        for char in "Seleccione una opción porfavor\n \n":
            #sleep(0.05)
            print(char,end='')

        menu = ['1)   Editar banco de preguntas en ambas materias.','2)   Ver historial de examanes de alumnos.', '3)   Ver notas de alumnos.','4)  Hacer examenes.', '5)  Cerrar Sesión']

        for opcion in menu:
            print(opcion, '\n')
        
        global opcionProfesor
        opcionProfesor = input("  ===>")


menu_opciones()