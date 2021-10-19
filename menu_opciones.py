from time import sleep# Esta libreria sirve para pausar operaciones por x cantidad de tiempo en segundos
from inicio_sesion import iniciar_sesion_estudiante, iniciar_sesion_profesor
from tabulate import tabulate

def menu_opciones():   

    #Saludo
    for i in "¡Bienvenid@ a tu asesor de estudio! \n \n       ¿Estas list@?\n \n":
        #sleep(0.05)
        print(i, end='')

    #Para acceder a la sesion coerrespondiente
    for i in "¿Eres estudiante o profesor?\n":
        sleep(0.05)
        print(i,end='')
    
    tipo_usuario = [['1) Estudiante'],['2) Profesor']]
    print(tabulate(tipo_usuario))

    es_profe_o_alumno = input('     ===> ')

    if es_profe_o_alumno == '1':

        print('Porfavor inicie sesión')

        #Variables de nombre y matricula son globales para que ../inicio_sesion.py pueda usar los parametros
        nombre = input('Porfavor ingrese su nombre:     ')
        matricula = input('Porfavor ingrese su matricula:       ') 

        #Pide al usuario iniciar sesion 
        #Revisa si la verificacion fue exitosa
        if iniciar_sesion_estudiante(nombre, matricula) == True:

            #Divisor para empezar menu
            print("="*20,"MENÚ","="*20,'\n')

            #Menu opciones
            for i in "Seleccione una opción porfavor\n \n":
                #sleep(0.05)        
                print(i,end='')

            menu = [['1)  Tomar examen'],['2)  Simulacro de examen'], ['3)  Ver historial de examenes'],['4)  Repasar temas'], ['5)  Cerrar Sesión']]

            print(tabulate(menu))

            #Hace el input global para hacer la logica de las opciones en la funcion ../sesion_estudiantes.py
            global opcionEstudiante
            opcionEstudiante = input("  ===>")
        else:
            menu_opciones()

    elif es_profe_o_alumno == '2': 

        matricula = input('Porfavor ingrese su matricula:       ') 
        contraseña = input('Porfavor ingrese su contraseña:     ')

        if iniciar_sesion_profesor(matricula,contraseña) == True:

            for i in "Seleccione una opción porfavor\n \n":
                #sleep(0.05)
                print(i,end='')

            menu = [['1)  Editar banco de preguntas.'],['2)  Ver historial de examanes de alumnos.'], ['3)  Ver notas de alumnos.'],['4)  Tomar examen.'], ['5)  Cerrar Sesión']]

            print(tabulate(menu))
            
            #Hace el input global para hacer la logica de las opciones en la funcion ../sesion_Profesores.py
            global opcionProfesor
            opcionProfesor = input("  ===>")

        else:
            menu_opciones()

    else:
        menu_opciones()


menu_opciones()