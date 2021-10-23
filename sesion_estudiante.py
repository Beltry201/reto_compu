import random
import webbrowser
        

#Banco preguntas español
pregunta_E_1 = {'Pregunta:' : '¿Qué palabra es la correcta?', 'Respuestas:' : '\nA-Hervir\nB-Herbir\nC-Erbir\nD-Ervir', 'RespuestaCorrecta' : 'B'}
pregunta_E_2 = {'Pregunta:' : '¿Qué oracion es la correcta?', 'Respuestas:' : '\nA-Que no vaya\nB-Que no vayya\nC-Que no valla\nD-Que no vayia', 'RespuestaCorrecta' : 'A'}
pregunta_E_3 = {'Pregunta:' : '¿Qué oracion es la correcta?', 'Respuestas:' : '\nA-Hasta que la muerte nos separe\nB-Asta que la muerte nos separe\nC-Hazta que la muerte nos separe\nD-Azta que la muerte nos separe', 'RespuestaCorrecta' : 'A'}
pregunta_E_4 = {'Pregunta:' : '¿Cuál no es un adjetivo calificativo?', 'Respuestas:' : '\nA-Alto\nB-Bueno\nC-Grande\nD-Comida', 'RespuestaCorrecta' : 'D'}
pregunta_E_5 = {'Pregunta:' : 'Completa la oracion: __! Que dolor!', 'Respuestas:' : '\nA-Ay\nB-Hay\nC-Ahi\nD-Alli', 'RespuestaCorrecta' : 'A'}
pregunta_E_6 = {'Pregunta:' : '¿Qué palabra es la correcta?', 'Respuestas:' : '\nA-Hormiga\nB-Órmiga\nC-Hórmiga\nD-Ormiga', 'RespuestaCorrecta' : 'A'}
pregunta_E_7 = {'Pregunta:' : '¿Cuál es un pronombre?', 'Respuestas:' : '\nA-Estar\nB-Abrir\nC-Ella\nD-¿Quién?', 'RespuestaCorrecta' : 'C'}
pregunta_E_8 = {'Pregunta:' : '¿Cuál es un verbo?', 'Respuestas:' : '\nA-Comida\nB-Carro\nC-Alto\nD-Correr', 'RespuestaCorrecta' : 'D'}
pregunta_E_9 = {'Pregunta:' : '¿Qué palabra esta bien escrita?', 'Respuestas:' : '\nA-Camión\nB-Camion\nC-Kamión\nD-Kamion', 'RespuestaCorrecta' : 'A'}
pregunta_E_10 = {'Pregunta:' : '¿Qué palabra es un sustantivo?', 'Respuestas:' : '\nA-Ella\nB-Nosotros\nC-Juan\nD-Yo', 'RespuestaCorrecta' : 'C'}
#Banco preguntas ciencias
pregunta_C_1 = {'Pregunta:' : '¿Cuáles son las funciones vitales del ser humano?', 'Respuestas:' : '\nA-Nutricion y reproduccion\nB-Nacer,crecer y morir\nC-Reproduccion,relacion y nutricion\nD-Desayuno, Comida y Cena', 'RespuestaCorrecta' : 'C'}
pregunta_C_2 = {'Pregunta:' : '¿Para qué sirven los sentidos?', 'Respuestas:' : '\nA-Para sobrevivir\nB-Para relacionarnos con el mundo que nos rodea\nC-Para mejorar el rendimiento del cuerpo humano.\nD-Para poder comer cualquier cosa', 'RespuestaCorrecta' : 'B'}
pregunta_C_3 = {'Pregunta:' : '¿Cómo se denomina la parte del cuerpo donde se juntan dos o más huesos?', 'Respuestas:' : '\nA-Cartilagos\nB-Tendones\nC-Articulaciones\nD-Conectores', 'RespuestaCorrecta' : 'C'}
pregunta_C_4 = {'Pregunta:' : '¿Cómo se clasifican los animales según tengan columna vertebral o no?', 'Respuestas:' : '\nA-Animales ovíparos o vivíparos\nB-Animales vertebrados y animales invertebrados\nC-Animales carnívoros, herbívoros u omnívoros\nD-Aracnidos,mamiferos.', 'RespuestaCorrecta' : 'B'}
pregunta_C_5 = {'Pregunta:' : '¿Qué utilizan los peces para respirar?', 'Respuestas:' : '\nA-Pulmones\nB-La Boca\nC-Nariz\nD-Branquias', 'RespuestaCorrecta' : 'D'}
pregunta_C_6 = {'Pregunta:' : '¿Puedes nombrar a un animal mamífero que vuela?', 'Respuestas:' : '\nA-Hormiga voladora\nB-Murcielago\nC-Pajaro carpintero\nD-No existe', 'RespuestaCorrecta' : 'B'}
pregunta_C_7 = {'Pregunta:' : '¿Cuál es el animal más veloz del mundo?', 'Respuestas:' : '\nA-León\nB-Venado\nC-Guepardo\nD-Panera', 'RespuestaCorrecta' : 'C'}
pregunta_C_8 = {'Pregunta:' : '¿Para qué sirve la raíz de las plantas?', 'Respuestas:' : '\nA-Para absorber agua de la tierra\nB-Para poder reproducirse\nC-Para hacer la fotosíntesis\nD-Para ser felices', 'RespuestaCorrecta' : 'A'}
pregunta_C_9 = {'Pregunta:' : '¿Qué absorbe la planta a través de sus hojas?', 'Respuestas:' : '\nA-Oxigeno\nB-Dioxido de carbono\nC-Gases\nD-Humo', 'RespuestaCorrecta' : 'B'}
pregunta_C_10 = {'Pregunta:' : '¿En qué tres estados puede presentarse la materia?', 'Respuestas:' : '\nA-En estado sólido, líquido o gaseoso\nB-Estable o inestable\nC- Renovable o no renovable\nD-Vivo o muerto', 'RespuestaCorrecta' : 'A'}

global banco_preguntas_español
banco_preguntas_español = [pregunta_E_1,pregunta_E_2,pregunta_E_3,pregunta_E_4,pregunta_E_5,pregunta_E_6,pregunta_E_7,pregunta_E_8,pregunta_E_9,pregunta_E_10]
global banco_preguntas_ciencias
banco_preguntas_ciencias = [pregunta_C_1,pregunta_C_2,pregunta_C_3,pregunta_C_4,pregunta_C_5,pregunta_C_6,pregunta_C_7,pregunta_C_8,pregunta_C_9,pregunta_C_10]

#Funcion que crea el examen de español
def examen_español(banco_preguntas_español,n):  
    calificacion = 0
    examen = []
    respuestasCorrectas = []
    respuestasIncorrectas = []
    for i in range(0,n):
        numero = random.randint(0,9)
        examen.append(banco_preguntas_español[numero]['Pregunta:'])
        pregunta = banco_preguntas_español[numero]['Pregunta:']
        respuestasPosibles = banco_preguntas_español[numero]['Respuestas:']
        print(pregunta + '\n',respuestasPosibles)
        respuesta = input('Respuesta:')       
        if respuesta.upper() == banco_preguntas_español[numero]['RespuestaCorrecta']:
            calificacion = calificacion + 100/n
            respuestasCorrectas.append(banco_preguntas_español[numero]['Pregunta:'])    
            respuestasCorrectas.append(banco_preguntas_español[numero]['RespuestaCorrecta'])
                
        else:
            respuestasIncorrectas.append(banco_preguntas_español[numero]['Pregunta:'])    
            respuestasIncorrectas.append(banco_preguntas_español[numero]['RespuestaCorrecta'])
    print(f'\nTu calificacion es de {calificacion} de 100 \n')  
    print('*'*70)
    print('Resumen del examen:')
    print('Respuestas correctas:')
    for i in respuestasCorrectas:
        print(i)
        print("\n")
    print('Respuestas incorrectas:')
    for i in respuestasIncorrectas:
        print(i)
        print("\n")
    return calificacion
    
#Funcion que crea el examen de matematicas
def examen_matematicas(n):
    calificacion = 0
    examen = []
    respuestaCorrecta=-40000
    respuestasCorrectasM = []
    respuestasIncorrectasM = []
    for i in range(0,n):
        numero = random.randint(1,1001)
        numero2 = random.randint(1,101)
        numero3 = random.randint(1,10)
        tipoPregunta = random.randint(0,100)
        
        if tipoPregunta > 33: #sumas
            pregunta = f'Cuanto es {numero} + {numero2}'
            examen.append(pregunta)
            respuestaCorrecta = numero + numero2
            print(pregunta)
            print('\n')
        elif tipoPregunta > 66: #sumas
            pregunta = f'Cuanto es {numero} - {numero2}'
            examen.append(pregunta)
            respuestaCorrecta = numero - numero2
            print(pregunta)
            print('\n')
        else: #sumas
            pregunta = f'Cuanto es {numero2} X {numero3}'
            examen.append(pregunta)
            respuestaCorrecta = numero2 * numero3
            print(pregunta)
            print('\n')
        
        respuesta = int(input('Respuesta:'))
        if respuesta == respuestaCorrecta:
            calificacion = calificacion + 100/n
            respuestasCorrectasM.append(pregunta)    
            respuestasCorrectasM.append(respuestaCorrecta)
        else:
            respuestasIncorrectasM.append(pregunta)    
            respuestasIncorrectasM.append(respuestaCorrecta)
    print(f'\nTu calificacion es de {calificacion} de 100 \n')  
    print('*'*70)
    print('Resumen del examen:')
    print('Respuestas correctas:')
    for i in respuestasCorrectasM:
        print(i)
        print("\n")
    print('Respuestas incorrectas:')
    for i in respuestasIncorrectasM:
        print(i)
        print("\n")        
    return calificacion



#Funcion que crea el examen de ciencias
def examen_ciencias(banco_preguntas_ciencias,n):
    calificacion = 0
    examen = []
    respuestasCorrectasC = []
    respuestasIncorrectasC = []
    for i in range(0,n):
        numero = random.randint(0,9)
        examen.append(banco_preguntas_ciencias[numero]['Pregunta:'])
        pregunta = banco_preguntas_ciencias[numero]['Pregunta:']
        respuestasPosibles = banco_preguntas_ciencias[numero]['Respuestas:']
        print(pregunta + '\n',respuestasPosibles)
        respuesta = input('Respuesta:')
        if respuesta.upper() == banco_preguntas_ciencias[numero]['RespuestaCorrecta']:
            calificacion = calificacion + 100/n
            respuestasCorrectasC.append(banco_preguntas_ciencias[numero]['Pregunta:'])    
            respuestasCorrectasC.append(banco_preguntas_ciencias[numero]['RespuestaCorrecta'])
                
        else:
            respuestasIncorrectasC.append(banco_preguntas_ciencias[numero]['Pregunta:'])    
            respuestasIncorrectasC.append(banco_preguntas_ciencias[numero]['RespuestaCorrecta'])
    print(f'\nTu calificacion es de {calificacion} de 100 \n')  
    print('*'*70)
    print('Resumen del examen:')
    print('Respuestas correctas:')
    for i in respuestasCorrectasC:
        print(i)
        print("\n")
    print('Respuestas incorrectas:')
    for i in respuestasIncorrectasC:
        print(i)
        print("\n")        
    return calificacion


#Funciones para despliegar videos de categorias de español
def practicaLectura():
    webbrowser.open("https://www.youtube.com/watch?v=SDHWfmF6hGY")
def practicaOrtografia():
    webbrowser.open("https://www.youtube.com/watch?v=mc5nGgpKuPM")

#Funciones para despliegar videos de categorias de matematicas
def practicaSumas():
    webbrowser.open("https://www.youtube.com/watch?v=oF-rZLIShC8")
def practicaRestas():
    webbrowser.open("https://www.youtube.com/watch?v=L6NOkLq6kHk")
def practicaMultiplicacion():
    webbrowser.open("https://www.youtube.com/watch?v=AE4B0hgnz0E")

#Funciones para despliegar videos de categorias de ciencias
def practicaCuerpoHumano():
    webbrowser.open("https://www.youtube.com/watch?v=S3jJj68dBxw")
def practicaPartesCuerpo():
    webbrowser.open("https://www.youtube.com/watch?v=-iDZ5tuH2fs")

