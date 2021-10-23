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

#Banco preguntas lectura comprensiva
lectura1 = """CÓMO CEPILLARSE LOS DIENTES
¿Se vuelven nuestros dientes más y más blancos cuanto más tiempo y más fuerte los
cepillamos?
Los investigadores británicos responden que no. De hecho, han probado muchas
alternativas distintas y al final han descubierto la manera perfecta de cepillarse los dientes. Un
cepillado de dos minutos, sin cepillar demasiado fuerte, proporciona el mejor resultado. Si uno
cepilla fuerte, daña el esmalte de los dientes y las encías sin quitar los restos de comida o la
placa dental.
Bente Hansen, experta en el cepillado de los dientes, señala dice que es una buena idea
sujetar el cepillo de dientes como se sujeta un bolígrafo. “Comience por una esquina y continúe
cepillándose a lo largo de toda la hilera”, dice. “¡Tampoco olvide la lengua! De hecho, ésta
puede contener miles de bacterias que pueden causar mal aliento”.
“Cómo cepillarse los dientes” es un artículo de una revista noruega."""
pregunta_L1_1= {'Pregunta:' : '¿De qué trata el artículo?', 'Respuestas:' : '\nA-De la mejor manera de cepillarse los dientes.\nB-Del mejor tipo de cepillo de dientes a utilizar.\nC-De la importancia de una buena dentadura.\nD-De la manera en que las distintas personas se cepillan los dientes.', 'RespuestaCorrecta' : 'A'}
pregunta_L1_2= {'Pregunta:' : '¿Qué recomiendan los investigadores británicos?', 'Respuestas:' : '\nA-Cepillarse los dientes tanto como sea posible.\nB-No intentar cepillarse la lengua.\nC-No cepillarse los dientes demasiado fuerte.\nD-Cepillarse la lengua con más frecuencia que los dientes.', 'RespuestaCorrecta' : 'C'}
pregunta_L1_3= {'Pregunta:' : '¿Por qué se menciona un bolígrafo en el texto?', 'Respuestas:' : '\nA-Para ayudarte a comprender cómo se sujeta un cepillo de dientes.\nB-Porque comienzas por una esquina tanto con un bolígrafo como con un cepillo de dientes.\nC-Para mostrarte que puedes cepillarte los dientes de muchas formas diferentes.\nD-Porque debes tomarte el cepillado de los dientes tan en serio como la escritura.', 'RespuestaCorrecta' : 'A'}


lectura2 = """El camino del futuro
¡Imagina lo maravilloso que sería “teletrabajar”
, trabajar en la autopista electrónica,
haciendo todo tu trabajo a través del ordenador o por teléfono! Ya no tendrías que
apretujarte en autobuses o trenes abarrotados, ni perder horas y horas viajando de casa al
trabajo y viceversa. Podrías trabajar donde quisieras, ¡piensa en todas las oportunidades
laborales que se abrirían ante ti!
María
Desastre a la vista
La reducción de desplazamientos y la disminución del consumo de energía que esto supone
es, obviamente, una buena idea. Pero dicho objetivo debe lograrse mejorando el transporte
público o garantizando que el lugar de trabajo esté situado cerca del lugar de residencial. La
ambiciosa idea de que el teletrabajo debería formar parte del estilo de vida de todo el
mundo sólo conduciría a que las personas se encerrasen más y más en sí mismas. ¿De
verdad queremos que nuestro sentido de pertenencia a una comunidad se deteriore
todavía más?
Ricardo
"""

pregunta_L2_1= {'Pregunta:' : '¿Qué relación existe entre “El camino del futuro” y “Desastre a la vista”?', 'Respuestas:' : '\nA-Los dos utilizan distintos argumentos para llegar a la misma conclusión general.\nB-Los dos están escritos en el mismo estilo pero tratan temas completamente diferentes.\nC-Los dos expresan la misma opinión, pero llegan a conclusiones diferentes.\nD-Los dos expresan opiniones contrarias acerca del mismo tema.', 'RespuestaCorrecta' : 'D'}
pregunta_L2_2= {'Pregunta:' : '¿Qué da a entender el autor con la palabra "Teletrabajar"?', 'Respuestas:' : '\nA- situación en la que los empleados trabajan con un ordenador lejos de la oficina central (por ejemplo, en casa) .\nB-Trabajar en las oficinas como comunmente.\nC-Trabajar en la television.\nD-Encontrarse en estado de retiro.', 'RespuestaCorrecta' : 'A'}

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

global banco_preguntas_lectura1
banco_preguntas_lectura1 = [pregunta_L1_1,pregunta_L1_2,pregunta_L1_3]
global banco_preguntas_lectura2
banco_preguntas_lectura2 = [pregunta_L2_1,pregunta_L2_2]

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

def examen_lectura(banco_preguntas_lectura1,banco_preguntas_lectura2):
    print("\n"*3)     
    calificacion1 = 0
    calificacion2 = 0
    examen = []
    examen2 = []
    respuestasCorrectasL1 = []
    respuestasIncorrectasL1 = []
    respuestasCorrectasL2 = []
    respuestasIncorrectasL2 = []
    print(lectura1)
    for numero in range(0,3):
        examen.append(banco_preguntas_lectura1[numero]['Pregunta:'])
        pregunta = banco_preguntas_lectura1[numero]['Pregunta:']
        respuestasPosibles = banco_preguntas_lectura1[numero]['Respuestas:']
        print(pregunta + '\n',respuestasPosibles)
        respuesta = input('Respuesta:')
        if respuesta.upper() == banco_preguntas_lectura1[numero]['RespuestaCorrecta']:
            calificacion1 = calificacion1 + 100/3
            respuestasCorrectasL1.append(banco_preguntas_lectura1[numero]['Pregunta:'])    
            respuestasCorrectasL1.append(banco_preguntas_lectura1[numero]['RespuestaCorrecta'])
                
        else:
            respuestasIncorrectasL1.append(banco_preguntas_lectura1[numero]['Pregunta:'])    
            respuestasIncorrectasL1.append(banco_preguntas_lectura1[numero]['RespuestaCorrecta'])
    print("\n"*3)     
    print(f'\nTu calificacion de la primera lectura es de {calificacion1} de 100 \n')  
    print('*'*70)
    print('Resumen del examen primera lectura :')
    print('Respuestas correctas:')
    for i in respuestasCorrectasL1:
        print(i)
        print("\n")
    print('Respuestas incorrectas:')
    for i in respuestasIncorrectasL1:
        print(i)
        print("\n") 
    print('Segunda lectura')
    print("\n"*5)     
    print(lectura2)
    for numero in range(0,2):
        examen2.append(banco_preguntas_lectura2[numero]['Pregunta:'])
        pregunta = banco_preguntas_lectura2[numero]['Pregunta:']
        respuestasPosibles = banco_preguntas_lectura2[numero]['Respuestas:']
        print(pregunta + '\n',respuestasPosibles)
        respuesta = input('Respuesta:')
        if respuesta.upper() == banco_preguntas_lectura2[numero]['RespuestaCorrecta']:
            calificacion2 = calificacion2 + 100/2
            respuestasCorrectasL2.append(banco_preguntas_lectura2[numero]['Pregunta:'])    
            respuestasCorrectasL2.append(banco_preguntas_lectura2[numero]['RespuestaCorrecta'])
                
        else:
            respuestasIncorrectasL2.append(banco_preguntas_lectura2[numero]['Pregunta:'])    
            respuestasIncorrectasL2.append(banco_preguntas_lectura2[numero]['RespuestaCorrecta'])
    print("\n"*3)     
    print(f'\nTu calificacion de la segunda lectura es de {calificacion2} de 100 \n')  
    print('*'*70)
    print('Resumen del examen segunda lectura :')
    print('Respuestas correctas:')
    for i in respuestasCorrectasL2:
        print(i)
        print("\n")
    print('Respuestas incorrectas:')
    for i in respuestasIncorrectasL2:
        print(i)
        print("\n")      
    print("\n"*5)     



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

