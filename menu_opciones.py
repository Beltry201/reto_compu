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
    
    es_profe_o_alumno = input('     ===>')
    
    #Divisor para empezar menu
    print("="*20,"MENÚ","="*20,'\n')

    #Menu opciones
    for char in "Seleccione una opción porfavor\n \n":
        #sleep(0.05)
        print(char,end='')

    menu = ['1)   Tomar examen','2)   Simulacro de examen', '3)   Ver historial de examenes','4)  Repasar temas', '5)  Cerrar Sesión']

    for opcion in menu:
        print(opcion, '\n')
menu_opciones()