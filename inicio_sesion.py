from time import sleep# Esta libreria sirve para pausar operaciones por x cantidad de tiempo en segundos

def iniciar_sesion_estudiante(nombre, matricula):

    #Variable global para confirmar que el usuario esta verificado
    global estudianteVerificado
    estudianteVerificado = False

    '''
    Lee el txt de sesiones_estudiantes y agrega cada matricual 
    a una lista (matriculas) para poder comparar el input del 
    usuario con las matricuals existentes.
    '''

    matriculas = []
    with open('sesiones_estudiantes.txt') as sesiones_estudiantes:
        for i in sesiones_estudiantes:
            # Descomentar para debbuguear
            # print('ENTRO AL CICLO QUE AGREGA MATRICULAS A LA LISTA')
            # print('ESTARÁ AGREGANDO ESTA MATRICULA --->{}   '.format(i.lower()))

            '''Se usa el metodo .replace() para evitar que la matricula 
            entre a la lista con el caracter reservado de nueva linea \n'''
            matriculas.append(i.lower().replace("\n","")) 
        # print(matriculas)
    # Descomentar para debbuguear
    # print(matriculas)

    #Si la matricula que puso está dentro de la lista, entonces se verifica
    if matricula.lower() in matriculas:
        print('\n¡Hola, {}!'.format(nombre))
        return not estudianteVerificado
    
    #Si no pudo encontrar un usuario en la lista matriculas, entonces crea un usuario nuevo
    else:
        registro = input('¿Desea crear un usuario para {}? si/no\n    ===>  '.format(matricula))
        if registro.lower() == 'si':
            with open ('sesiones_estudiantes.txt','a+') as sesiones_estudiantes:
                #Mover el cursor en el inicio del archivo
                sesiones_estudiantes.seek(0)
                #Si la lista con las matricualas del txt no está vacia (es decir si hay matricualas) entonces insertar una linea
                if len(matriculas) > 0:
                    sesiones_estudiantes.write('\n')

                sesiones_estudiantes.write(matricula.lower())
                # print('MATRICULA A AGREGAR')
                # print(i.lower())
                print('¡Bienvenido, {}\n'.format(nombre))

                return not estudianteVerificado
        elif registro.lower() == 'no':
            print('='*40,'\nRedirigiendo\n','='*40)
                
        else:
            print('='*40,'\n¡Ups! Algo salió mal, intente de nuevo\n','='*40)
            
    return estudianteVerificado

def iniciar_sesion_profesor(matricula, contraseña):

    #Variable global para confirmar que el usuario esta verificado
    global profesorVerificado
    profesorVerificado = False

    '''
    Lee el txt de sesiones_profesores y agrega cada matricual 
    a una lista (matriculas) para poder comparar el input del 
    usuario con las matricuals existentes.
    '''
    matriculas = []
    contraseñas = []
    with open('sesiones_profesores.txt') as sesiones_profesores:

        for i in sesiones_profesores:

            #Si empieza en a00 entonces se agregar a la lista de matriculas
            if i[:3].lower() == 'a00':
                matriculas.append(i.lower().replace("\n",""))
                # print('MATRICULA A AGREGAR')

            #Si no empieza en a00 entonces se agregara a lista de contraseñas
            elif i[:3].lower() != 'a00':
                contraseñas.append(i.replace("\n",""))

    '''Para registrar un profesor nuevo, accede a super usuario.
    Debe ingresar admin como matricula y contraseña.   '''
    if matricula.lower() == 'admin' and contraseña.lower() == 'admin':
        print('Accedió al modo super usuario')
        super_usuario = input('¿Desea agregar a un profesor nuevo si/no?\n    ===>  ')

        if super_usuario.lower() == 'si':
            matricula_super = input('Matricula nueva:    ')
            contraseña_super = input('Contraseña:     ')

            #Abre el archivo de sessiones_profesores en modo append +
            with open ('sesiones_profesores.txt','a+') as sesiones_profesores:
                #Mover el cursor en el inicio del archivo
                sesiones_profesores.seek(0)
                #Si la lista con las matricualas del txt no está vacia (es decir si hay matricualas) entonces insertar una linea
                if len(matriculas) > 0:
                    sesiones_profesores.write('\n')

                sesiones_profesores.write(matricula_super.lower())
                sesiones_profesores.write('\n')
                sesiones_profesores.write(contraseña_super)
        elif super_usuario.lower() == 'no':
            print('='*40,'\nRedirigiendo\n','='*40)

        else:
            pass


    #Si la matricula y contraseña que puso está dentro de la lista, entonces se verifica
    if matricula.lower() in matriculas:
        for i in 'Verificando contraseña...\n':
            sleep(0.05)
            print(i,end='')

        if contraseña in contraseñas and contraseña != "":
            print('\n¡Bienvenido profesor!')
        return not profesorVerificado
    
    #Si no pudo encontrar un usuario en la lista matriculas, entonces crea un usuario nuevo
    else:
        print('='*40,'\n¡Ups! Algo salió mal, intente de nuevo\n','='*40)

    return profesorVerificado
