from time import sleep# Esta libreria sirve para pausar operaciones por x cantidad de tiempo en segundos
from inicio_sesion import iniciar_sesion_estudiante, iniciar_sesion_profesor
from tabulate import tabulate
from sesion_estudiante import *



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
#tabulate(tipo_usuario)
    es_profe_o_alumno = input('     ===> ')

    if es_profe_o_alumno == '1':

        print('Porfavor inicie sesión')

        #Pide al usuario iniciar sesion 

        nombre = input('Porfavor ingrese su nombre:     ')
        matricula = input('Porfavor ingrese su matricula:       ') 

        #Revisa si la verificacion fue exitosa
        if iniciar_sesion_estudiante(nombre,matricula) == True:

            #Divisor para empezar menu
            print("="*20,"MENÚ","="*20,'\n')

            #Menu opciones
            for i in "Seleccione una opción porfavor\n \n":
                #sleep(0.05)        
                print(i,end='')

            menu = [['1)  Tomar examen'],['2)  Repasar materia'], ['3)  Ver historial de examenes'], ['5)  Cerrar Sesión']]
#tabulate(menu)
            print(tabulate(menu))

            #Hace el input global para hacer la logica de las opciones en la funcion ../sesion_estudiantes.py
            global opcionEstudiante
            opcionEstudiante = input("  ===>")

            #Empieza seleccion de menu
            
            if opcionEstudiante == '1':
                salida = True
                while salida != False:
                    print('De que materia desea realizar su examen? \n')
                    materias_disponibles = [['1)    Español'],['2)  Matemáticas'],['3)  Ciencias']]
                    #tabulate(materias_disponibles)
                    print(tabulate(materias_disponibles))
                    selecciona_materia = int(input('===>    '))

                    if selecciona_materia == 1:
                        examen_español(banco_preguntas_español, int(input('Cuantas preguntas sera el examen? ')),matricula)
                        print('*'*70)
                        print('Comienza prueba de lectura')
                        examen_lectura(banco_preguntas_lectura1,banco_preguntas_lectura2,matricula)

                    elif selecciona_materia == 2:
                        examen_matematicas(int(input('Cuantas preguntas quiere en su examen? ')),matricula)

                    elif selecciona_materia == 3:
                        examen_ciencias(banco_preguntas_ciencias, int(input('Cuantas preguntas sera el examen? ')),matricula)
                    elif selecciona_materia == 4:
                        examen_lectura(banco_preguntas_lectura1,banco_preguntas_lectura2,matricula)
                    
                    seguir = int(input('Continuar? 1-Si 2-Salir '))
                    if seguir == 2:
                        salida = False
                        menu_opciones()
                

            elif opcionEstudiante == '2':
                salida2 = True
                while salida2 != False:
                    print('¿Qué materia te gustaria repasar? ')
                    materias_disponibles = [['1)    Español'],['2)  Matemáticas'],['3)  Ciencias']]
                    #tabulate(materias_disponibles)
                    print(tabulate(materias_disponibles))
                    selecciona_materia = int(input('===>    '))

                    if selecciona_materia == 1:
                        print('De que categoria te gustaria realizar tu repaso? ')
                        categoria_disponibles = [['1)    Lectura Comprensiva'],['2) Ortografia']]
                    # tabulate(categoria_disponibles)
                        print(tabulate(categoria_disponibles))
                        seleccion_disponibles = int(input('===>    '))

                        if seleccion_disponibles == 1:
                            practicaLectura()  

                        elif seleccion_disponibles == 2:
                            practicaOrtografia()
                                            
                    elif selecciona_materia == 2:
                        print('De que categoria te gustaria realizar tu repaso? ')
                        categoria_disponiblesM = [['1)    Sumas'],['2) Restas'],['3)  Multiplicacion']]
                        print(categoria_disponiblesM)
                        seleccion_disponiblesM = int(input('===>    '))
                        if seleccion_disponiblesM == 1:
                            practicaSumas() 
                        elif seleccion_disponiblesM == 2:
                            practicaRestas()
                        elif seleccion_disponiblesM == 3:
                            practicaMultiplicacion()
                    elif selecciona_materia == 3:
                        print('De que categoria te gustaria realizar tu repaso? ')
                        categoria_disponiblesC = [['1)    Sistemas del Cuerpo'],['2) Partes del cuerpo']]
                        print(categoria_disponiblesC)
                        seleccion_disponiblesC = int(input('===>    '))
                        if seleccion_disponiblesC == 1:
                            practicaCuerpoHumano()  
                        elif seleccion_disponiblesC == 2:
                            practicaPartesCuerpo()
                    seguir2 = int(input('Continuar? 1-Si 2-Salir '))
                    if seguir2 == 2:
                        salida2 = False
                        menu_opciones()

            elif opcionEstudiante == '3':

                with open(str(matricula),'r') as historial_estudiante:
                    print(historial_estudiante.read())   

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
            #tabulate(menu)
            print(tabulate(menu))
            
            #Hace el input global para hacer la logica de las opciones en la funcion ../sesion_Profesores.py
            global opcionProfesor
            opcionProfesor = input("  ===>")

        else:
            menu_opciones()

    else:
        menu_opciones()


menu_opciones()