from tda_lista_lista import nodoLista , Lista, insertar, eliminar, busqueda_lista, busqueda_lista_vec, barrido_sublista, barrido_lista, tamanio, lista_vacia, criterio
from random import randint, choice
from datetime import date
from time import sleep


lista = Lista()

def lista_numerica(lista):
    while tamanio(lista) < 10:
        dato = randint(0,10)
        insertar(lista, dato)
        print(dato)
    print('tamaño de lista comun: ' + str(tamanio(lista)))

def lista_letras(lista):
    while tamanio(lista) < 10:
        dato = chr(randint(65,122))
        insertar(lista,dato)
        print('letra: ' + dato)
    print('tamaño de lista comun: ' + str(tamanio(lista)))

# 1. Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.
'''
print(lista_numerica(lista))
def contar_nodos(lista):
    cont = 0
    aux = None
    for i in range(tamanio(lista)):
        cont += 1
        if aux == None:
            aux = lista.inicio
        else:
            aux = aux.sig

    print('nodos contados')
    return cont
print(contar_nodos(lista))
'''

#2. Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.
'''
print(lista_letras(lista))
def eliminar_vocales(lista):
    vocales = 'aAeEiIoOuU'
    aux = None
    for i in range(tamanio(lista)):
        if aux == None:
            aux = lista.inicio
        else:
            aux = aux.sig
        if aux.info in vocales:
            eliminar(lista,aux.info)
            print('se elimino la letra: ' + aux.info)
    print('lista sin vocales: ')
    print(barrido(lista))

print(eliminar_vocales(lista))
'''
#3. Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en
# dos, una que contenga los números pares y otra para los números impares.
'''
print(lista_numerica(lista))
def lista_par_impar(lista):
    lista_par = Lista()
    lista_impar = Lista()
    aux = None
    for i in range(tamanio(lista)):
        if aux == None:
            aux = lista.inicio
        else:
            aux = aux.sig
        if (aux.info % 2 == 0):
            insertar(lista_par, aux.info)
        else:
            insertar(lista_impar, aux.info)
    print('lista de pares, tamanio: ' + str(tamanio(lista_par)))
    barrido(lista_par)
    print('lista impares, tamanio: '+ str(tamanio(lista_impar)))
    barrido(lista_impar)

print(lista_par_impar(lista))
'''

#4. Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.
'''
print(lista_letras(lista))
def insertar_iesimo(lista,pos,elemento):
    nodo = nodoLista()
    nodo.info = elemento
    aux = lista.inicio
    tam = lista.tamanio
    while tam == lista.tamanio:
        if pos >= 0 and pos <= lista.tamanio:
            for i in range(1, pos):
                aux = aux.sig
            nodo.sig = aux.sig
            aux.sig = nodo
            print('- Se ha agregado el elemento en la posicion ' + str(pos))
        else:
            print('Elemento será agregado al final de la lista')
            pos = lista.tamanio
            for i in range(1, pos):
                aux = aux.sig
            nodo.sig = aux.sig
            aux.sig = nodo
    barrido_lista(lista)

pos = int(input('ingrese una posicion en la cual agregar el elemento: '))
print(insertar_iesimo(lista,pos,'objeto'))
'''
#5. Dada una lista de números enteros eliminar de estas los números primos.
'''
print(lista_numerica(lista))
def eliminar_primos(lista):
    aux = None
    for i in range(tamanio(lista)):
        div = 0
        if aux == None:
            aux = lista.inicio
        else:
            aux = aux.sig
        for j in range (0,aux.info):
            j += 1
            if (aux.info % j == 0):
                div += 1
                if div > 2:
                    break
        if div <= 2:
            print('elemento primo eliminado: ' + str(aux.info))
            eliminar(lista, aux.info)
    print('lista SIN primos: ')
    barrido(lista)
print(eliminar_primos(lista))
'''
#6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, casa de comic a la que 
# pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:
#a. eliminar el nodo que contiene la información de Linterna Verde;
#b. mostrar el año de aparición de Wolverine;
#c. cambiar la casa de Dr. Strange a Marvel;
#d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
#e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
#f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
#g. mostrar toda la información de Flash y Star-Lord;
#h. listar los superhéroes que cominezan con la letra B, M y S;
#i. determinar cuántos superhéroes hay de cada casa de comic.
'''
superheroes = ['Linterna Verde','Wolverine','Dr Strange','Capitana Marvel','Mujer Maravilla','Flash','Star-Lord','Iron Man','Thanos','Batman','Dr Doom','Ghost Rider']
comic = ['Marvel', 'DC']
biografia = ['traje','armadura','Otras palabras','mas palabras']
for i in range (10):
    dato = ['','','',0]
    dato[0] = choice(superheroes)
    dato[1] = choice(comic)
    dato[2] = choice(biografia)
    dato[3] = randint(1920,2020)
    insertar(lista,dato)
    print(dato)
def super_heroes(lista):
    print(' ')
    aux = None
    for i in range(tamanio(lista)):
        if aux == None:
            aux = lista.inicio
        else:
            aux = aux.sig
        if aux.info[0] == 'Linterna Verde':
            eliminar(lista, aux.info)
            print('Se ha eliminado a Linterna Verde')
        if aux.info[0] == 'Wolverine':
            print('Wolverine: Su año de aparicion fue en--> ' + str(aux.info[3]))
        if aux.info[0] == 'Dr Strange':
            if aux.info[1] != 'Marvel':
                aux.info[1] = 'Marvel'
            print('... Se ha cambiado la casa de "Dr Strange" a "Marvel" ...')
            print(aux)
    print(' ')

    print('personajes con la palabra traje o armadura en su biografia:')
    aux = None
    for i in range(tamanio(lista)):
        if aux == None:
            aux = lista.inicio
        else:
            aux = aux.sig
        if (aux.info[2] == 'traje') or (aux.info[2] == 'armadura'):
            print(aux.info[0] + ' - ' + aux.info[2])

    print(' ')
    print('Nombre y Casa de los superhéroes cuya fecha de aparición es anterior a 1963:')
    aux = None
    for i in range(tamanio(lista)):
        if aux == None:
            aux = lista.inicio
        else:
            aux = aux.sig
        if (aux.info[3] < 1963):
            print(' - ' + aux.info[0] + ' - ' + aux.info[1] + ' - ' + str(aux.info[3]))

    print(' ')
    print('Casa a la que pertenece Capitana Marvel y Mujer Maravilla:')
    aux = None
    for i in range(tamanio(lista)):
        if aux == None:
            aux = lista.inicio
        else:
            aux = aux.sig
        if (aux.info[0] == 'Capitana Marvel') or (aux.info[0] == 'Mujer Maravilla'):
            print(aux.info[0] + ' - ' + aux.info[1])

    print(' ')
    print('Informacion completa de Flash y Star-Lord:')
    aux = None
    cont_Marvel = 0
    cont_Dc = 0
    for i in range(tamanio(lista)):
        if aux == None:
            aux = lista.inicio
        else:
            aux = aux.sig
        if (aux.info[0] == 'Flash') or (aux.info[0] == 'Star-Lord'):
            print(aux.info[0] + ' ||| ' + aux.info[1] + ' - ' + aux.info[2] + ' - ' + str(aux.info[3]))
        if (aux.info[1] == 'Marvel'):
            cont_Marvel += 1
        else:
            cont_Dc += 1
            
    print(' ')
    print('La casa Marvel tiene ' + str(cont_Marvel) + ' Superheroes')
    print('La casa DC tiene ' + str(cont_Dc) + ' Superheroes')
print(super_heroes(lista))
'''
#7. Implementar los algoritmos necesarios para resolver las siguientes tareas:
#a. concatenar dos listas, una atrás de la otra;
#b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
#c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
#d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.
'''
lista_aux = Lista()
lista_conc = Lista()
#A
def lista_concatenada(lista,lista_aux):
    print('Lista 1')
    barrido_lista(lista)
    print('Lista 2')
    barrido_lista(lista_aux)
    aux = lista_aux.inicio
    for i in range(0,tamanio(lista_aux)):
        insertar(lista,aux.info)
        aux = aux.sig
    print('')
    print('Lista concatenada')
    barrido_lista(lista)
    print('')

#B y C
def lista_concatenada_or(lista, lista_aux):
    repetidos = 0
    lista_conc = Lista()
    aux = lista.inicio
    while(aux is not None):
        pos = busqueda_lista(lista_conc, aux.info)
        if(pos is None):
            insertar(lista_conc, aux.info)
        else:
            repetidos += 1
        aux = aux.sig
    print("Lista concatenada sin repetidos")
    barrido_lista(lista_conc)
    print('Cantidad de elementos repetidos: ' + str(repetidos))
    print('')

#D
def eliminar_nodos(lista):
    aux = lista.inicio
    while aux is not None:
        eliminar(lista, aux.info)
        print('Se ha eliminado el nodo:' + str(aux.info))
        aux = aux.sig

print(lista_letras(lista))
print(lista_letras(lista_aux))
print(lista_concatenada(lista,lista_aux))
print(lista_concatenada_or(lista,lista_aux))
print(eliminar_nodos(lista))
'''
#8. Utilizando una lista doblemente enlazada, cargar una palabra carácter a carácter, y
# determinar si la misma es un palíndromo, sin utilizar ninguna estructura auxiliar.
'''  NO SE HACE  '''

#9. Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo.
#Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos
#con la siguiente información: materia que rindió, nota obtenida y fecha de parcial.
#Desarrollar un algoritmo que permita realizar la siguientes actividades:
#a. mostrar los alumnos ordenados alfabéticamente por apellido;
#b. indicar los alumnos que no desaprobaron ningún parcial;
#c. determinar los alumnos que tienen promedio mayor a 8,89;
#d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
#e. mostrar el promedio de cada uno de los alumnos;
#f. debe modificar el TDA para implmentar lista de lista.
'''
alumnos = ['Fernando', 'Cynthia', 'Tomas', 'Joaquin', 'Julieta', 'Walter']
apellidos = ['Picart','Carmona','Bide','Lopez','Gutierrez','Lauren']
materias = ['Algebra','Calculo','Algoritmos']

class Alumno(object):
    def __init__(self,nombre,apellido,legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo

    def __str__(self):
        return '<<<    ' + self.nombre + ' - ' + self.apellido + ' - ' + str(self.legajo) + '    >>>'

class Parcial(object):
    def __init__(self,materia,nota,fecha):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha

    def __str__(self):
        return '' + self.materia + '|| Nota = '+ str(self.nota) + '|| fecha = ' + str(self.fecha)

def parciales_alumnos(lista):
    print('Alumnos ordenados por apellido')
    for i in range(len(alumnos)):
        legajo = i+1
        dato = Alumno(alumnos[i],apellidos[i],legajo)
        insertar(lista, dato, 'apellido')
    barrido_lista(lista)
    print(' ')

    for i in range(tamanio(lista)):
        i += 1
        for j in range(3):
            pos = busqueda_lista(lista,i,'legajo')
            dato = Parcial(materias[j],randint(4,10),date(2020,randint(1,12),randint(1,30)))
            insertar(pos.sublista, dato, 'materia')
    barrido_sublista(lista)
    print(' ')

    aux = lista.inicio
    p = 0
    while aux != None:
        aprobado = True
        c = 0
        prom = 0
        pos = aux.sublista.inicio
        while pos != None:
            c += 1
            if pos.info.nota < 7:
                aprobado = False
            prom += pos.info.nota
            pos = pos.sig
        
        if aprobado == True:
            print(aux.info.nombre + ' ' + aux.info.apellido + ' Ha aprobado todas las materias')
        if ((prom / c) > 8.89):
            p += 1
            print(aux.info.nombre + ' ' + aux.info.apellido + ' Tiene promedio mayor a 8,89, su promedio es: ' + str(round(prom/c,2)))
        aux = aux.sig
    if (p < 1):
        print('Ningun alumno tiene promedio mayor a 8,89.')
    print('')

    print('Alumnos con apellido que comienza con L')
    aux = lista.inicio
    while aux != None:
        if aux.info.apellido[0] == 'L':
            print(aux.info.nombre + ' ' + aux.info.apellido + ';  legajo ' + str(aux.info.legajo))
        aux = aux.sig

    print('')
    print('Promedio de todos los alumnos:')
    aux = lista.inicio
    while aux != None:
        suma_notas = 0
        c = 0
        pos = aux.sublista.inicio
        while pos != None:
            suma_notas += pos.info.nota
            c += 1
            pos = pos.sig
        prom = (suma_notas / c)
        print('El promedio de el alumno ' + aux.info.nombre + ' ' + aux.info.apellido + ' es ' + str(round(prom,2)))
        aux = aux.sig

print(parciales_alumnos(lista))
'''

#10. Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o
#artista, duración y cantidad de reproducciones durante el último mes. Desarrollar un
#algoritmo que permita realizar las siguientes actividades:
#a. obtener la información de la canción más larga;
#b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
#c. obtener todas las canciones de la banda Arctic Monkeys;
#d. mostrar los nombres de las bandas o artistas que solo son de una palabra.
'''
TENGO QUE ARREGLAR LA PARTE DEL TOP 5

canciones = ['In the end','505','Smoke on the wather','Marinero','Hoja en blanco','Habia una vez','Give me power','Do I wanna know']
bandas = ['Linkin Park','Arctic Monkeys','Deep Purple','Maluma','Dread Mar I','Indio Solari','Molotov','Arctic Monkeys']
duraciones = [3.37 , 4.10 , 5.40 , 4.48 , 4.48 , 4.29 , 4.08 , 4.26]

class Cancion(object):
    def __init__(self, nombre,banda,duracion,reprod):
        self.nombre = nombre
        self.banda = banda
        self.duracion = duracion
        self.reprod = reprod

    def __str__(self):
        return self.nombre + ' | ' + self.banda + ' | ' + str(self.duracion) + ' | ' + str(self.reprod)

def spotify(lista):
    for i in range(len(canciones)):
        reproducciones = randint(1,60)
        dato = Cancion(canciones[i],bandas[i],duraciones[i],reproducciones)
        insertar(lista,dato,'reprod')
    aux = lista.inicio
    m_dur = 0
    while aux != None:
        if aux.info.duracion > m_dur:
            m_dur = aux.info.duracion
            pos = aux
        aux = aux.sig
    print('la cancion de mayor duracion es ' + pos.info.nombre + ', de ' + pos.info.banda + ' con ' + str(pos.info.duracion) + ' minutos de duracion')
    print('')

    print('Top 5 de canciones mas escuchadas')
    aux = lista.inicio
    i = 0
    while aux != None:
        if (i == tamanio(lista)-5) :
            for i in range(5):
                print(aux.info.nombre + ', de ' + aux.info.banda + '; de duracion ' + str(aux.info.duracion) + ' y ' + str(aux.info.reprod) + ' MM. cantidad de reproducciones')
                aux = aux.sig

print(spotify(lista))
'''

# 11. Dada una lista que contiene información de los personajes de la saga de Star Wars con la
# siguiente información nombre, altura, edad, género, especie, planeta natal y episodios en
# los que apareció, desarrollar los algoritmos que permitan realizar las siguientes actividades:
# a. listar todos los personajes de género femenino;
# b. listar todos los personajes de especie Droide que aparecieron en los primeros seis episodios de la saga;
# c. mostrar toda la información de Darth Vader y Han Solo;
# d. listar los personajes que aparecen en el episodio VII y en los tres anteriores (4,5,6 y 7);
# e. mostrar los personajes con edad mayor a 850 años y de ellos el mayor;
# f. eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI;
# g. listar los personajes de especie humana cuyo planeta de origen es Alderaan;
# h. mostrar toda la información de los personajes cuya altura es menor a 70 centímetros;
# i. determinar en qué episodios aparece Chewbacca y mostrar además toda su información.
'''
class Personaje(object):
    def __init__(self,nombre,altura,edad,genero,especie,planeta):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.genero = genero
        self.especie = especie
        self.planeta = planeta


    def __str__(self):
        return self.nombre+'  || Altura: ' +str(self.altura) +',    Edad: '+str(self.edad)+ ',    Genero: '+self.genero+ ',    Especie: '+self.especie+',    Planeta: '+self.planeta

class Episodios(object):
    def __init__(self,episodio):
        self.episodio = episodio

    def __str__(self):
        return 'Episodio: ' + str(self.episodio)

personajes = ['Luke Skywalker','Beru Lars', 'R2-D2', 'Han Solo', 'Maestro Yoda', 'Jar Jar Binks','Darth Vader','Chewbacca','Leia Organa']
alturas = [1.72 , 1.65 , 0.38 , 1.74 , 0.60 , 1.96 , 1.84 , 2.30 , 1.55]
edades = [47,37,853,54,917,1382,1059,987,90]
generos = ['M','F','Bot','M','M','M','M','M','F']
especies = ['Humano','Humano','Droide','Humano','Yoda','Gungan','Darth','Wookiee','Humano']
planetas = ['Tatooine','Tatooine','Naboo','Corellia','896 ABY','Naboo','Tatooine','Kashyyyk','Alderaan']
episodios = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for i in range(len(personajes)):
    dato = Personaje(personajes[i],alturas[i],edades[i],generos[i],especies[i],planetas[i])
    insertar(lista,dato,'planeta')
aux = lista.inicio
while not aux == None:
    cant = (randint(1,15))
    lista_epis = []
    for i in range(cant):
        epis = choice(episodios)
        if len(lista_epis) == 0:
            lista_epis.append(epis)
            insertar(aux.sublista,Episodios(epis),'episodio')
        if epis not in lista_epis:
            insertar(aux.sublista,Episodios(epis),'episodio')
            lista_epis.append(epis)
    aux = aux.sig
print('Lista de personajes ordenada segun Planetas Natales: ')
barrido_lista(lista)
print()
aux = lista.inicio
# A
print('Lista de personajes FEMENINOS')
while aux != None:
    if aux.info.genero == 'F':
        print(aux.info)
    aux = aux.sig
print()
# B
print('Lista de los personajes de especie Droide, que aparecieron en los primeros seis episodios de la saga:')
aux = lista.inicio
while not aux == None:
    pos = aux.sublista.inicio
    while not pos == None:
        if pos.info.episodio == 1:
            print(aux.info.nombre + ' aparecio en el capitulo 1.')
        elif pos.info.episodio == 2:
            print(aux.info.nombre + ' aparecio en el capitulo 2.')
        elif pos.info.episodio == 3:
            print(aux.info.nombre + ' aparecio en el capitulo 3.')
        elif pos.info.episodio == 4:
            print(aux.info.nombre + ' aparecio en el capitulo 4.')
        elif pos.info.episodio == 5:
            print(aux.info.nombre + ' aparecio en el capitulo 5.')
        elif pos.info.episodio == 6:
            print(aux.info.nombre + ' aparecio en el capitulo 6.')
        else:
            break
        pos = pos.sig
    aux = aux.sig
# C
print()
print('-información de Darth Vader y Han Solo')
aux = lista.inicio
while aux != None :
    if (aux.info.nombre == 'Darth Vader') or (aux.info.nombre == 'Han Solo'):
        print(aux.info)
    aux = aux.sig
# D
print()
print('Personajes que aparecen en el episodio VII y en los tres anteriores:')
aux = lista.inicio
p = 0
while aux != None:
    pos = aux.sublista.inicio
    c = 0
    while pos != None:
        if pos.info.episodio == 4:
            c += 1
        elif pos.info.episodio == 5:
            c += 1
        elif pos.info.episodio == 6:
            c +=1
        elif pos.info.episodio == 7:
            c += 1
            if c == 4:
                print(aux.info.nombre +', aparecio en los capitulos 4,5,6 y 7.')
                p += 1
        pos = pos.sig
    aux = aux.sig
if p == 0:
    print('__No hay personajes que mostrar en esta lista.')
# E
print()
print('Personajes con edad mayor a 850 años')
aux = lista.inicio
mayor = ''
ed = 0
while aux != None:
    if aux.info.edad > 850:
        print(aux.info.nombre + ': tiene ' + str(aux.info.edad) + ' años.')
    if ed < aux.info.edad:
        mayor = aux.info.nombre
        ed = aux.info.edad
    aux = aux.sig
print()
print('<<< El personaje de mayor EDAD es: '+ mayor+ ', con '+ str(ed) +' años >>>')
# F
print()
print('Se eliminaran los personajes que hayan aparecido solamente en los capitulos: 4,5 y 6')
aux = lista.inicio
p = 0
while aux != None:
    pos = aux.sublista.inicio
    c = 0
    n = 0
    while pos != None:
        if pos.info.episodio == 4:
            c += 1
        elif pos.info.episodio == 5:
            c += 1
        elif pos.info.episodio == 6:
            c += 1
        else:
            n += 1
            break
        pos = pos.sig
    if (c == 3) and (n == 0):
        eliminar(lista,aux.info.nombre,'nombre')
        print('Se ha eliminado al personaje '+ aux.info.nombre)
        p += 1
    aux = aux.sig
if p == 0:
    print('__No hay personajes que mostrar en esta lista.')
print()
# G
print('Personajes Humanos cuyo planeta de origen es Alderaan;')
aux = lista.inicio
while aux != None:
    if (aux.info.especie == 'Humano') and (aux.info.planeta == 'Alderaan'):
        print(aux.info.nombre +': es Humano y su planeta natal es: ' + aux.info.planeta) 
    aux = aux.sig
print()
# H
print('Personajes cuya altura es menor a 70 centímetros;')
aux = lista.inicio
while aux != None:
    if aux.info.altura < 0.70:
        print(aux.info)
    aux = aux.sig
print()
# I
aux = lista.inicio
while aux != None:
    if aux.info.nombre == 'Chewbacca':
        print('- Informacion de Chewbacca:')
        print(aux.info)
        print('>>> Episodios en los que aparece:')
        pos = aux.sublista.inicio
        while pos != None:
            print(pos.info.episodio)
            pos = pos.sig
    aux = aux.sig
print()
'''

#12. Desarrollar un algoritmo que elimine el anteúltimo nodo de una lista independientemente
# de la información del mismo, utilizando lista simplemente enlazada 
'''
print(lista_numerica(lista))
def elim_anteultimo(lista):
    print('---lista comun---')
    barrido_lista(lista)
    aux = lista.inicio
    i = 0
    while aux != None:
        if (i == tamanio(lista)-1) :
            eliminar(lista,aux.info)
            print('')
        i+=1
        aux = aux.sig
    print('- Lista sin su anteultimo nodo:')
    barrido_lista(lista)
print(elim_anteultimo(lista))
'''

# 13. Desarrollar un algoritmo que permita visualizar el contenido de una lista de manera ascendente 
# y descendente de sus elementos, debe modificar el TDA para implementar lista doblemente enlazada.
'''   NO SE HACE    '''

# 14. Un grupo de amigos se reúnen a jugar un juego de dados, suponga que dichos jugadores están cargados 
# en una lista de acuerdo a un número asignado de manera aleatoria y su nombre. Desarrollar un algoritmo 
# que contemple las siguientes condiciones:
# a. simular la tirada de un dado –de seis lados D6– en cada turno del jugador;
# b. el orden de turno de los jugadores es el mismo en el que están cargados en la lista;
# c. después de que tira el último jugador de la lista debe seguir el primero;
# d. el juego termina cuando uno de los jugadores saca un 5, en ese caso mostrar su nombre;
'''
jug = ['Juan','Ricardo','Juliana','Rocio','Marta','Federico','Mirta']
turnos = [1,2,3,4,5,6,7]
dados = [1,2,3,4,5,6]

class Jugador(object):
    def __init__(self, nombre,turno):
        self.nombre = nombre
        self.turno = turno

    def __str__(self):
        return self.nombre +' | turno nro: ' + str(self.turno)
    
def juego_dados(lista):
    t = []
    for i in range(len(jug)):
        turno = None
        while turno == None:
            turno = randint(1,len(jug))
            if turno in t:
                turno = None
            else:
                t.append(turno)
        
        insertar(lista,Jugador(jug[i],turno),'turno')
        print(str(turno) + '.- sera la posicion de ' + jug[i])
    print('')
    print('--- Jugadores por turnos ---')
    barrido_lista(lista)
    print('')
    print('--- Empieza el juego ---')
    aux = lista.inicio
    while aux != ' ':
        dado = (choice(dados))
        sleep(1)
        print('Dado = ' + str(dado))
        if dado == 5:
            break
        else:
            print('El jugador ha sacado ' + str(dado))
            print('...Turno del siguiente jugador...')
        aux = aux.sig
        if aux == None:
            aux = lista.inicio
    print('¡¡¡¡ El jugador ' + aux.info.nombre + ' ha sacado 5 y por lo tanto ha ganado !!!!')
print(juego_dados(lista))
'''


#15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: 
# nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. 
# Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. 
# Se pide resolver las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados; 
# d. mostrar todos los datos de un entrenador y sus Pokémos; 
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo); 
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
#### i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben 
# ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;
'''
entrenadores = ['Juan','Ricardo','Juliana','Rocio','Marta','Federico','Mirta']

pokemon = { 'Bulbasaur' : ['panta','veneno'] , 'Charmander' : ['fuego','None'] , 'Squirtle': ['Agua','None'],
            'Pelipper' : ['agua','volador'] , 'Wingull' : ['agua','volador'], 'Cyndaquil' : ['fuego','planta'],
            'Caterpie' : ['bicho','None'] , 'Pikachu' : ['electrico','None'] , 'Nidoran' : ['veneno','None'], 
            'Vulpix' : ['Fuego','None'] , 'Jigglypuff' : ['Normal','Hada'] , 'Psyduck' : ['agua','None'],
            'Abra' : ['psiquico','None'] , 'Machop' : ['lucha','None'] , 'Onix' : ['roca','tierra'], 
            'Terrakion' : ['roca','dragon'] , 'Hitmonlee' : ['lucha','None'] , 'Magikarp' : ['agua','None'] ,
            'Eevee' : ['normal','None'] ,'Snorlax' : ['normal','None'] , 'Mewtwo' : ['psiquico','None'] ,
            'Tyrantrum' : ['roca','dragon'] , 'Articuno' : ['hielo','volador']}


class Entrenador(object):
    def __init__(self,nombre,t_ganados,bat_ganadas,bat_perdidas,cant_pok):
        self.nombre = nombre
        self.t_ganados = t_ganados
        self.bat_ganadas = bat_ganadas
        self.bat_perdidas = bat_perdidas
        self.cant_pok = cant_pok
    
    def __str__(self):
        return self.nombre + ' | torneos: ' + str(self.t_ganados) + ' | gano ' + str(self.bat_ganadas) + ' batallas y perdio ' + str(self.bat_perdidas) + '| Tiene ' +str(self.cant_pok)+ ' Pokemones'

class Pokemon(object):
    def __init__(self, nombre,tipo,subtipo,nivel):
        self.nombrepok = nombre
        self.tipo = tipo
        self.subtipo = subtipo
        self.nivel = nivel

    def __str__(self):
        return self.nombrepok + ' tipo: ' + self.tipo + '/'+ self.subtipo + '. su nivel es ' + str(self.nivel)

def pokemones(lista):
    for i in range(len(entrenadores)):
        aux = Entrenador(entrenadores[i],randint(0,10),randint(0,100),randint(0,100),randint(1,10))
        insertar(lista,aux,'t_ganados')
    barrido_lista(lista)
    print('')
    aux = lista.inicio
    while not aux == None:
        print(aux.info)
        print('---- Pokemones')
        cant = aux.info.cant_pok
        for j in range (cant):
            pok = choice(list(pokemon.keys()))
            dato = Pokemon(pok, pokemon[pok][0], pokemon[pok][1], randint(1,50))
            print(dato)
            insertar(aux.sublista,dato,'nivel')
        aux = aux.sig
        print('')
    #b
    print('')
    print('<<<<< Entrenadores que han ganado MAS de 3 torneos Pokemon >>>>>')
    aux = lista.inicio
    c = 0
    while not aux == None:
        if aux.info.t_ganados > 3 :
            print(aux.info)
            c += 1
        aux = aux.sig
    print(' - Hay ' + str(c) + ' entrenadores que ganaron mas de 3 torneos Pokemon.')
    print('')
    # C
    torn = 0
    ent = None
    aux = lista.inicio
    nv = 0
    pok = None
    while not aux == None:
        if aux.info.t_ganados > torn:
            torn = aux.info.t_ganados
            max_torn = aux.info.nombre
            ent = aux.sublista.inicio
            while not ent == None:
                if nv < ent.info.nivel:
                    nv = ent.info.nivel
                    pok = ent.info.nombrepok
                ent = ent.sig
        aux = aux.sig
    print('- El entrenador que mas Torneos Pokemon ha ganado es: ' + max_torn + ', con ' + str(torn)+ ' Torneos ganados.')
    print('- Su pokemon de mayor nivel es: ' + pok + ' de nivel ' + str(nv))
    print('')
    nom = input('ingrese Entrenador a mostrar sus datos y pokemones: ')
    pos = busqueda_lista(lista,nom,'nombre')
    if not pos == None:
        print(pos.info)
        print('_____Pokemones:')
        aux = pos.sublista.inicio
        while not aux == None:
            print(aux.info)
            aux = aux.sig
    print('')
    # e
    print('- ENTRENADORES CON PORCENTAJE DE VICTORIA MAYOR A 79% :')
    aux = lista.inicio
    x = False
    while aux is not None:
        bat_tot = aux.info.bat_ganadas + aux.info.bat_perdidas
        porcentaje = (aux.info.bat_ganadas * 100)/bat_tot
        if porcentaje > 79:
            x = True
            print(aux.info.nombre +' tiene un porcentaje de ' +str(round(porcentaje,2)) + '% batalladas ganadas.')
        aux = aux.sig
    if x == False:
        print('No hay Entrenadores con un porcentaje mayor a 79.')
    print()
    # f
    aux = lista.inicio
    while aux is not None:
        sub = aux.sublista.inicio
        while sub is not None:
            if (sub.info.tipo == 'fuego'):
                if (sub.info.subtipo == 'planta'):
                    print(aux.info.nombre, ': tiene un pokemon tipo fuego y subtipo planta, ' + sub.info.nombrepok)
            if (sub.info.tipo == 'agua'):
                if (sub.info.subtipo == 'volador'):
                    print(aux.info.nombre, ': tiene un pokemon tipo agua y subtipo volador, ' + sub.info.nombrepok)
            sub = sub.sig
        aux = aux.sig
        print('-')
    print('')
    # g
    nom = input('ingrese Entrenador a sacar promedio de nivel de sus Pokemones: ')
    pos = busqueda_lista(lista,nom,'nombre')
    if not pos == None:
        print(pos.info)
        niveles = 0
        cant = 0
        sub = pos.sublista.inicio
        while sub is not None:
            cant += 1
            print(sub.info)
            niveles += sub.info.nivel
            sub = sub.sig
        prom = niveles / cant
        print('--- El promedio de nivel de sus pokemones es: '+ str(round(prom, 2)))
    print('')
    # H
    aux = lista.inicio
    cont = 0
    pok = input(str('Ingrese el nombre del pokemon a buscar: '))
    while aux is not None:
        pos = busqueda_lista(aux.sublista, pok, 'nombrepok')
        if pos is not None:
            cont += 1
            print(aux.info.nombre +' tiene a ' + pok)
        aux = aux.sig
    print(str(cont) +' entrenadores tienen al pokemon '+ pok)
    print('')
    # J
    aux = lista.inicio
    while aux is not None:
        sub = aux.sublista.inicio
        while sub is not None:
            if (sub.info.nombrepok == 'Tyrantrum') or (sub.info.nombrepok == 'Terrakion') or (sub.info.nombrepok == 'Wingull'):
                print('El entrenador ' +aux.info.nombre + ', tiene al pokemon ' + sub.info.nombrepok)
            sub = sub.sig
        aux = aux.sig
    print('')
    # K
    pos = None
    n = None
    x = None
    while ent not in entrenadores:
        ent = input('Ingrese nombre del entrenador: ')
    pos = busqueda_lista(lista,ent,'nombre')
    while n not in pokemon:
        n = input('Ingrese nombre de pokemon a buscar: ')
    if (not pos == None) and (not n == None):
        print('')
        b = False
        nom = pos.sublista.inicio
        while not nom == None:
            if (nom.info.nombrepok == n):
                b = True
                break
            nom = nom.sig
        if b == False:
            print('El entrenador '+ pos.info.nombre + ' no tiene al pokemon buscado.')
        elif b == True:
            print('Entrenador y pokemon encontrados.')
            print('Mostrando sus datos...')
            sleep(1.5)
            print(pos.info)
            sleep(0.7)
            print(nom.info)

print(pokemones(lista))
'''

# 16. Se deben administrar las actividades de un proyecto de software, de estas se conoce su
# costo, tiempo de ejecución, fecha de inicio, fecha de fin estimada, fecha de fin efectiva y
# persona a cargo. Desarrollar un algoritmo que realice las siguientes actividades:
# a. tiempo promedio de tareas;
# b. costo total del proyecto;
# c. actividades realizadas por una determinada persona;
# d. mostrar la información de las tareas a realizar entre dos fechas dadas;
# e. mostrar las tareas finalizadas en tiempo y las finalizadas fuera de tiempo;
# f. indicar cuántas tareas le quedan pendientes a una determinada persona, indicada por el usuario.
'''
def proyecto_software():
    proyectos = Lista()
    a_tiempo = Lista()
    fuera_de_tiempo = Lista()
    personal = ['Tomas', 'Flavio', 'Juan', 'Claudia', 'Guillermo', '']
    actividades = ['Recopilar informacion','Estudio de factibilidad','Planificacion','Analisar la informacion','Codificar el sistema','Probar el sistema','Instalacion Sw']
    promedio = 0
    costo_total = 0
    for i in range(len(personal)):
        costo = randint(0, 50000)
        tiempo_ejecucion = randint(1, 10)
        fecha_inicio = [ randint(1, 31), randint(1, 12),2020]
        fecha_estimada = [ randint(1, 31), randint(1, 12),2020]
        fechaF_efectiva = [ randint(1, 31), randint(1, 12),2020]
        persona_cargo = choice(personal)
        actividad = actividades[i]
        tareas = [costo,actividad, tiempo_ejecucion, fecha_inicio, fecha_estimada, fechaF_efectiva, persona_cargo]
        insertar(proyectos, tareas)
    print()
    print('Lista con actividades:')
    barrido_lista(proyectos)
    aux = proyectos.inicio
    print()
    while aux is not None:
        # A
        promedio = promedio + aux.info[2]
        # B
        costo_total = costo_total + aux.info[0]
        # C
        if aux.info[5]:
            print('Persona:',aux.info[6])
            print('Actividades que realiza:',aux.info[1])
            print('Coste de la actividad:',aux.info[0])
            print('Tiempo de ejecucion:',aux.info[2])
            print()
        if aux.info[2] < 7:
            insertar(a_tiempo,aux.info[1])
        else:
            insertar(fuera_de_tiempo,aux.info[1])
        aux = aux.sig
    # D
    fecha1 = [1,2,2020] 
    fecha2 = [25,4,2020]
    print()
    print('Actividades entre '+ str(fecha1) + ' y '+ str(fecha2))
    aux = proyectos.inicio
    while aux is not None:
        if fecha1 < aux.info[5] and fecha2 > aux.info[5]:
            print(aux.info[1])
        aux = aux.sig   
    print()
    print('Tareas que se realizaron a tiempo: ')
    barrido_lista(a_tiempo)
    print()
    print('Tareas que se realizaron fuera de tiempo: ')
    barrido_lista(fuera_de_tiempo)

print(proyecto_software())
'''
# 17. Se cuenta con los vuelos del aeropuerto de Heraklion en Creta, de estos se sabe la siguiente 
# información: empresa, número del vuelo, cantidad de asientos del avión, fecha de salida, destino, 
# kms del vuelo. Y además se conoce los datos de cantidades de asientos totales y ocupados por clase
# (primera y turista). Implemente las funciones necesarias que permitan realizar las siguiente actividades:
# a. mostrar los vuelos con destino a Atenas, Miconos y Rodas;
# b. mostrar los vuelos con asientos clase turista disponible.;
# c. mostrar el total recaudado por cada vuelo, considerando clase turista ($75 por kilómetro) 
# y primera clase ($203 por kilómetro);
# d. mostrar los vuelos programados para una determinada fecha;
# e. vender un asiento (o pasaje) para un determinado vuelo;
# f. eliminar un vuelo. Tener en cuenta que si tiene pasajes vendidos, se debe indicar la cantidad de 
# dinero a devovler;
# g. mostrar las empresas y los kilómetros de vuelos con destino a Tailandia.
'''
empresas = ['"British Airways"','"American Airlines"','"Lufthansa"','"Lion Air"']
destinos = ['Atenas','Miconos','Rodas','Argentina','China','Brasil','España','Francia','Tailandia']
asientos = [40,45,50,60,70,80]
km = [1000,2000,2500,5000,7000,10500]
clases = ['turista','primera']
tru = [False,True]

class Vuelo(object):
    def __init__(self,empresa,num_v,c_asientos,f_salida,destino,kms):
        self.empresa = empresa
        self.num_v = num_v
        self.c_asientos = c_asientos
        self.f_salida = f_salida
        self.destino = destino
        self.kms = kms

    def __str__(self):
        return 'datos: ' + self.empresa +': vuelo ' +str(self.num_v)+', asientos: ' + str(self.c_asientos)+'; Fecha: '+ str(self.f_salida)+ ', Destino: ' + self.destino+ ', kms: ' + str(self.kms) +'.'

class Asiento(object):
    def __init__(self,numero,ocupado,clase,precio):
        self.numero = numero
        self.ocupado = ocupado
        self.clase = clase
        self.precio = precio

    def __str__(self):
        return self.numero +'; Vendido = '+self.ocupado +', Clase: '+ self.clase +', Precio:'+ self.precio

def aeropuerto(lista):
    for i in range(len(destinos)):
        num_v = i+1
        d = randint(1,30)
        m = randint(1,12)
        a = randint(2020,2021)
        fecha = [d,m,a]
        kms = choice(km)
        cant = choice(asientos)
        dato = Vuelo(choice(empresas),num_v,cant,fecha,destinos[i],kms)
        insertar(lista,dato,'destino')
    aux = lista.inicio
    while aux != None:
        cant = aux.info.c_asientos
        p = cant//1.5
        precio = 0
        for i in range(cant):
            asiento = i+1
            ocupado = choice(tru)
            if asiento < p:
                clase = 'Turista'
                precio = (75*kms)
            else:
                clase = 'Primera'
                precio = (203*kms)
            dato = Asiento(asiento,ocupado,clase,precio)
            insertar(aux.sublista,dato,'numero')
        aux = aux.sig
    # A
    aux = lista.inicio
    while not aux == None:
        if aux.info.destino == 'Atenas':
            print('Destino a Atenas: ')
            print(aux.info)
        if aux.info.destino == 'Miconos':
            print('Destino a Miconos: ')
            print(aux.info)
        if aux.info.destino == 'Rodas':
            print('Destino a Rodas: ')
            print(aux.info)
        aux = aux.sig
    print('')
    # B
    aux = lista.inicio
    while not aux == None:
        print()
        s_n = input('Desea ver los asientos libres de la clase turista del destino '+ aux.info.destino + ': ')
        if (s_n == 'S') or (s_n == 's'):
            pos = aux.sublista.inicio
            while not pos == None:
                if pos.info.clase == 'Turista' and pos.info.ocupado == False:
                    print('El asiento '+ str(pos.info.numero) + ' esta desocupado')
                pos = pos.sig
        aux = aux.sig
    # C
    print()
    print('Total recaudado por cada vuelo')
    aux = lista.inicio
    while not aux == None:
        recaudado = 0
        pos = aux.sublista.inicio
        while pos != None:
            if pos.info.ocupado == True:
                recaudado += pos.info.precio
            pos = pos.sig
        print('El vuelo nro '+str(aux.info.num_v)+', a '+ aux.info.destino +' recaudo: '+ str(recaudado)+ ' dinero.')
        aux = aux.sig
    print()
    # E
    s_n = None
    while (s_n != 'n') and (s_n != 'N'):
        s_n = input('Quiere comprar un nuevo pasaje? S/N: ')
        if (s_n == 'S') or (s_n == 's'):
            destino = input('Indique su destino: ')
            bus = None
            bus = busqueda_lista(lista,destino,'destino')
            if bus != None:
                compra = False
                while compra == False:
                    pas = int(input('Elija numero de pasaje: (1/'+ str(bus.info.c_asientos) +') : '))
                    pos = bus.sublista.inicio
                    while pos != None:
                        if pos.info.numero == pas:
                            if pos.info.ocupado == False:
                                pos.info.ocupado = True
                                print('Compra de pasaje exitosa.')
                                print()
                                compra = True
                                break
                            else:
                                print('Lo siento, ese pasaje esta ocupado.')
                                print()
                                break
                        pos = pos.sig
    # F
    print()
    elim = None
    while (elim != 'n') and (elim != 'N'):
        elim = input('Desea eliminar algun vuelo? S/N: ')
        if (elim == 's') or (elim == 'S'):
            vuelo = int(input('Indique con numero, el Nro de vuelo a eliminar: '))
            bus = None
            bus = busqueda_lista(lista,vuelo,'num_v')
            if bus != None:
                b = input('- Seguro que desea eliminar el vuelo con destino a '+ bus.info.destino+' ? S/N: ')
                if (b == 's') or (b == 'S'):
                    eliminar(lista,bus.info.num_v,'num_v')
                    print('>>> Se ha eliminado el vuelo Nro: '+str(bus.info.num_v)+', con destino a '+ bus.info.destino )
                    pos= bus.sublista.inicio
                    recaudado = 0
                    while pos != None:
                        if pos.info.ocupado == True:
                            recaudado += pos.info.precio
                        pos = pos.sig
                    print('>>> La cantidad de dinero a devolver es igual a: ' + str(recaudado))
                    print()
    # G
    print()
    print('Empresas y kilómetros de vuelos con destino a Tailandia:')
    aux = lista.inicio
    while aux != None:
        if aux.info.destino == 'Tailandia':
            print('__ La empresa '+aux.info.empresa + ' tiene un viaje a Tailandia de '+str(aux.info.kms)+' KMs.')
        aux = aux.sig

print(aeropuerto(lista))
'''

# 18. Se tienen los usuarios colaboradores de un lista de GitHub y de cada uno de estos
# se tiene una lista de los commit realizados, de los cuales se cuenta con su timestamp (en
# formato fecha y hora), mensaje de commit, nombre de archivo modificado, cantidad de
# líneas agregadas/eliminadas (puede ser positivo o negativo) –suponga que solo puede
# modificar un archivo en cada commit que se haga–. Desarrollar un algoritmo que permita
# realizar las siguientes actividades:
# a. obtener el usuario con mayor cantidad de commits –podría llegar a ser más de uno–;
# b. obtener el usuario que haya agregado en total mayor cantidad de líneas y el que
# haya eliminado menor cantidad de líneas;
# c.mostrar los usuarios que realizaron cambios sobre el archivo test.py después delas 19:45 sin importar la fecha;
# d. indicar los usuarios que hayan realizado al menos un commit con cero líneas agregados o eliminadas;
# e. determinar el nombre del usuario que realizó el último commit sobre el archivo app.py indicando 
# toda la información de dicho commit;
# f. deberá utilizar el TDA lista de lista.
'''
class Usuario():
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Commit():
    def __init__(self, archivo, timestamp, mensaje, cant_lineas):
        self.archivo = archivo
        self.timestamp = timestamp
        self.mensaje = mensaje
        self.cant_lineas = cant_lineas

    def __str__(self):
        return 'Archivo: '+ self.archivo +'; Timestamp: '+ self.timestamp + ', Mensaje: ' + self.mensaje + ', Modificó: ' + str(self.cant_lineas)+ ' lineas'


def github(lista):
    lista = Lista()
    user = Usuario('Camilo')
    insertar(lista, user, 'nombre')
    user = Usuario('Federico')
    insertar(lista, user, 'nombre')
    user = Usuario('Flavia')
    insertar(lista, user, 'nombre')
    user = Usuario('Anastacia')
    insertar(lista, user, 'nombre')
    commit = Commit('test.py', '11-11-20 19:00', 'testeo de la app', 46)
    pos = busqueda_lista(lista, 'Camilo', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('data.py', '11-11-20 19:00', 'correccion error', 12)
    pos = busqueda_lista(lista, 'Camilo', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('object.java', '11-11-20 19:00', 'modelado del objeto', -37)
    pos = busqueda_lista(lista, 'Federico', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('app.py', '11-11-20 19:00', 'basta chicos', 34)
    pos = busqueda_lista(lista, 'Flavia', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('front.html', '11-11-20 19:00', 'update', 47)
    pos = busqueda_lista(lista, 'Anastacia', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('vista.css', '11-11-20 19:00', 'update', -2)
    pos = busqueda_lista(lista, 'Anastacia', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    print('Lista de colaboradores: ')
    barrido_lista(lista)
    print()
    # a
    aux = lista.inicio
    mayor = 0
    while aux is not None:
        if tamanio(aux.sublista) > mayor:
            mayor = tamanio(aux.sublista)
        aux = aux.sig
    aux = lista.inicio
    while aux is not None:
        if tamanio(aux.sublista) == mayor:
            print('Colaborador con mayor cantidad de commits: ' + aux.info.nombre)
            print('Cantidad de commits: '+ str(mayor))
        aux = aux.sig
    print()
    # b
    mayor = 0
    usuario = ''
    aux = lista.inicio
    while aux is not None:
        pos = aux.sublista.inicio
        mayor_aux = 0
        while pos is not None:
            mayor_aux += pos.info.cant_lineas
            pos = pos.sig
        if mayor_aux > mayor:
            mayor = mayor_aux
            usuario = aux.info.nombre
        aux = aux.sig
    print(usuario +', agrego la mayor cantidad de lineas: ' +str(mayor))
    menor = 0
    usuario_menor = ''
    aux = lista.inicio
    while aux is not None:
        pos = aux.sublista.inicio
        menor_aux = 0
        while pos is not None:
            menor_aux += pos.info.cant_lineas
            pos =pos.sig
        if menor_aux < menor:
            menor = menor_aux
            usuario_menor = aux.info.nombre
        aux = aux.sig
    print(usuario_menor+ ' elimino la mayor cantidad de lineas: '+ str(menor))
    print()
    # C
    aux = lista.inicio
    while aux is not None:
        pos = busqueda_lista(aux.sublista,'test.py','archivo')
        if pos is not None:
            print(aux.info.nombre + ', ha realizado cambios en test.py')
        aux = aux.sig
    # D
    print()
    aux = lista.inicio
    while aux is not None:
        pos = busqueda_lista(aux.sublista,0,'cant_lineas')
        if pos is not None:
            print(aux.info.nombre + ' ha realizado un commit con 0 lineas')
        aux = aux.sig
    print()
    # E
    aux = lista.inicio
    while aux is not None:
        pos = busqueda_lista(aux.sublista,'app.py','archivo')
        if pos is not None:
            print(aux.info.nombre + ', ha realizado cambios en app.py')
            barrido_sublista(aux.sublista)
        aux = aux.sig
print(github(lista))
'''
#19. Los astilleros de propulsores Kuat, son la mayor corporación de construcción de naves
#militares que provee al imperio galáctico –dentro de sus productos más destacados están
#los cazas TIE, destructores estelares, transporte acorazado todo terreno (AT-AT),
#transporte de exploración todo terreno (AT-ST), ejecutor táctico todo terreno (AT-TE),
#entre otros– 
# y nos solicita desarrollar las funciones necesarias para resolver las siguientes necesidades:
#a. debe procesar los datos de las ventas de naves que están almacenados en un
#rudimentario archivo de texto, en el cual cada línea tiene los siguientes datos:
# código del astillero que lo produjo, producto (los mencionados previamente),precio en créditos galácticos, 
# si fue construido con partes recicladas o no(booleano), quien realizo la compra (en algunos casos se 
# desconoce quién realizola compra y este campo tiene valor desconocido), todos estos datos están 
# separados por “;” en cada línea del archivo;
#b. cargar los datos procesados en el punto anterior en dos listas, en la primera las
#ventas de las que se conocen el cliente y la segunda las que no;
#c. el código del astillero son tres caracteres el primero en una letra mayúscula de la “A” 
# hasta la “K” seguido de dos dígitos;
#d. obtener el total de ingresos de créditos galácticos y cuantas unidades se vendieron;
#e. listar los nombres de todos los clientes, los repetidos deberán mostrarse una solavez, puede utilizar 
# una estructura auxiliar para resolverlo;
#f. realizar un informe de las compras realizadas por Darth Vader;
#g. se le debe realizar un descuento del 15% a los clientes que compraron naves que
# fueron fabricadas con partes recicladas, mostrar los clientes y los montos a devolver a cada uno;
# h. determinar cuánto ingreso genero la producción de naves cuyos modelos contengan la sigla “AT”.

def venta_naves():
    lista_ventas = Lista()
    clientes = Lista()
    sin_clientes = Lista()
    nombre_clientes = Lista()
    informe = Lista()
    #A
    archivo = open('naves')
    linea = archivo.readline()
    while linea:
        linea = linea.replace('\n', '')
        linea = linea.split(';')
        linea[0] = linea[0].upper()
        linea[1] = linea[1].upper()
        linea[2] = float(linea[2])
        linea[3] = linea[3].title()
        linea[4] = linea[4].title()
        insertar(lista_ventas, linea)
        linea = archivo.readline()      
    print('Lista de ventas de naves')
    barrido_lista(lista_ventas)
    print()
    aux = lista_ventas.inicio
    cont = 0
    ac = 0
    devolver = 0
    ingresoAT = 0
    while aux is not None:
        #B
        if aux.info[4] == 'Desconocido':
            insertar(sin_clientes, aux.info)
        else:
            insertar(clientes,aux.info)
            pos = busqueda_lista(nombre_clientes, aux.info[4],4)
            #E
            if pos == None:
                insertar(nombre_clientes,aux.info[4])
        #D
        cont += 1
        ac = ac + aux.info[2]
        #F
        if aux.info[4] == 'Darth Vader':
            insertar(informe, aux.info)
        #H
        if aux.info[1] == 'AT-AT' or aux.info == 'AT-ST' or aux.info == 'AT-TE':
            ingresoAT = ingresoAT + aux.info[2]
        aux = aux.sig

    print('Total de ingresos de creditos galacticos: ')
    print(ac)
    print()
    print('Total de naves vendidas:')
    print(cont)
    print()
    print('Listado de clientes')
    barrido_lista(nombre_clientes)
    print()
    print('Informe de compras de Darth Vader')
    barrido_lista(informe)
    print()
    print('Clientes que han comprado naves construidas con material reciclado y monto a devoler:')
    aux2 = lista_ventas.inicio
    while aux2 is not None:
        #G
        if aux2.info[3] == 'Si':
            devolver = (aux2.info[2] * 15) / 100
            print('Al cliente: '+ aux2.info[4] + ' se le devolvera, '+str(round(devolver,2)))
        aux2 = aux2.sig
    print()
    print('Ingreso genero la producción de naves cuyos modelos contengan la sigla “AT”.: '+str(round(ingresoAT,2)))

print(venta_naves())

#20. Una empresa meteorológica necesita registrar los datos de sus distintas estaciones en las
#cuales recolecta la siguiente información proveniente de sus distintas estaciones de
#adquisición de datos diariamente, implemente las funciones para satisfacer los siguientes 
# requerimientos:
# a. se deben poder cargar estaciones meteorológicas, de cada una de estas se sabe su
# país de ubicación, coordenadas de latitud, longitud y altitud;
# b. estas estaciones registran mediciones de temperatura, presión, humedad y estado el clima –como 
# por ejemplo soleado, nublado, lloviendo, nevando, etcétera– en distintos lapsos temporales, estos
# datos deberán guardarse en la lista junto con la fecha y la hora de la medición;
# c. mostrar el promedio de temperatura y humedad de todas las estaciones durante el mes de mayo;
# d. indicar la ubicación de las estaciones meteorológicas en las que en el día actual está lloviendo o nevando;
# e. mostrar los datos de las estaciones meteorológicas que hayan registrado estado del clima tormenta eléctrica o huracanes;
# f. debe implementar el TDA lista de lista.
'''
paises = ['Argentina','Uruguay','Brasil','Chile','Paraguay','Mexico','Colombia','Venezuela']
estados_clima = ['soleado','nublado','lloviendo','nevando','tormenta eléctrica','vientos fuertes','huracanes']
estaciones = ['verano','otoño','invierno','primavera']

class Pais():
    def __init__(self,pais,latitud,longitud,altitud):
        self.pais = pais
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

    def __str__(self):
        return 'Pais: '+ self.pais +'|| Ubicacion: Latitud '+ str(self.latitud) + ', Longitud: '+ str(self.longitud) +', Altitud: '+str(self.altitud)

class Medicion():
    def __init__(self,fecha,temperatura,presion,humedad,clima):
        self.fecha = fecha
        self.temperatura = temperatura
        self.presion = presion
        self.humedad = humedad
        self.clima = clima

    def __str__(self):
        return '- Fecha: '+str(self.fecha)+'. Temperatura: '+str(self.temperatura)+ ' grados, Presion: '+str(self.presion)+ ', Humedad: '+str(self.humedad)+ ' % , Clima: '+self.clima
# A
for i in range(len(paises)):
    dato = Pais(paises[i],randint(0,100),randint(0,100),randint(0,100))
    insertar(lista,dato,'pais')
aux = lista.inicio
# B
while not aux == None:
    print(aux.info)
    for i in range(12):
        d = randint(1,30)
        m = i+1
        a = randint(2020,2021)
        fecha = [d,m,a]
        dato = Medicion(fecha,randint(-10,50),randint(0,20),randint(0,100),choice(estados_clima))
        print(dato)
        insertar(aux.sublista,dato,'fecha')
    print('')
    aux = aux.sig
# C
print('Promedios de Temperatura y Humedad:')
aux = lista.inicio
while not aux == None:
    pos = aux.sublista.inicio
    temp = 0
    hum = 0
    cont = 0
    while not pos == None:
        temp += pos.info.temperatura
        hum += pos.info.humedad
        cont += 1
        pos = pos.sig
    print(aux.info.pais + ': El promedio de Temperatura es: ' + str(round(temp/cont , 2)))
    print(aux.info.pais + ': El promedio de Humedad es: ' + str(round(hum/cont , 2)))
    aux = aux.sig
    print('')
# D
aux = lista.inicio
while aux is not None:
    pos = aux.sublista.inicio
    while not pos == None:
        if pos.info.clima == 'lloviendo':
            print('En la fecha '+str(pos.info.fecha)+', en el pais ' +aux.info.pais + ' esta lloviendo.')
        elif pos.info.clima == 'nevando':
            print('En la fecha '+str(pos.info.fecha)+', en el pais ' +aux.info.pais + ' esta nevando.')
        pos = pos.sig
    aux = aux.sig
print('')
# E
print('- Registros de estado del clima con tormenta eléctrica o huracanes:')
aux = lista.inicio
while aux != None:
    pos = aux.sublista.inicio
    while pos != None:
        if pos.info.clima == 'huracanes':
            print(aux.info.pais + ' registro clima de huracanes en la fecha ' + str(pos.info.fecha))
        elif pos.info.clima == 'tormenta eléctrica':
            print(aux.info.pais+ ' registro clima de Tormenta Electrica en la fecha ' + str(pos.info.fecha))
        pos = pos.sig
    aux = aux.sig
'''


# 21. Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos: 
# nombre, valoración del público –es un valor comprendido entre 0-10–, año de
# estreno y recaudación. Desarrolle los algoritmos necesarios para realizar las siguientes tareas:
# a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determinado año–;
# b. mostrar los datos de la película que más recaudo;
# c. indicar las películas con mayor valoración del público, puede ser más de una;
# d. mostrar el contenido de la lista en los siguientes criterios de orden (solo podrá utilizar una lista auxiliar):
# i. por nombre  #ii. por recaudación,  #iii. por año de estreno,  #iv. por valoración del público.
'''
class Pelicula():
    def __init__(self,nombre,valoracion,estreno,recaudacion):
        self.nombre = nombre
        self.valoracion = valoracion
        self.estreno = estreno
        self.recaudacion = recaudacion

    def __str__(self):
        return '- Pelicula: ' + self.nombre + ' ||valoracion: ' + str(self.valoracion) + '. Año de estreno: ' + str(self.estreno) + '. Ha recaudado: ' + str(self.recaudacion)

pelis = ['Iron Man','Harry Potter','Stars Wars','Avengers','Spider Man','El señor de los anillos','Capitan America']

def lista_peliculas(lista):
    for i in range(len(pelis)):
        dato = Pelicula(pelis[i],randint(1,10),randint(1970,2020),randint(100000,10000000))
        insertar(lista,dato,'nombre')
    barrido_lista(lista)
    print('')
    # A
    pos = None
    while pos == None:
        pos = input('Ingrese un año de estreno: ')
        if pos not in '1234567890':
            pos = None
    aux = lista.inicio
    vacio = False
    while aux is not None:
        if pos == aux.info.estreno:
            print('- '+aux.info.nombre +' se estreno en el año: '+ str(aux.info.estreno))
            vacio = True
        aux = aux.sig
    if vacio == False:
        print('- Ninguna pelicula se ha estrenado en ese año.')
    print('')
    # B
    mas_rec = 0
    mayor_p = ''
    aux = lista.inicio
    while aux is not None:
        if aux.info.recaudacion > mas_rec:
            mas_rec = aux.info.recaudacion
            mayor_p = aux.info
        aux = aux.sig
    print('Pelicula que mas recaudo y sus datos:')
    print(mayor_p)
    print('')
    # C
    print('Valoracion mas Alta:')
    aux = lista.inicio
    max_v = 0
    while aux is not None:
        if aux.info.valoracion > max_v:
            max_v = aux.info.valoracion
        aux = aux.sig
    aux = lista.inicio
    while aux is not None:
        if aux.info.valoracion == max_v:
            print('- ' +aux.info.nombre +' tiene la valoracion mas alta, su puntaje es de ' + str(max_v) + ' puntos.')
        aux = aux.sig
    print('')
    # D
    print('Peliculas mostradas por criterio:')
    crit = None
    lista_aux = Lista()
    print('CRITERIOS: nombre / valoracion / estreno / recaudacion : ')
    while crit == None:
        crit = input('Ingrese criterio por el que quiere mostrar: ')
        if (crit != 'nombre') and (crit != 'recaudacion') and (crit != 'estreno') and (crit != 'valoracion'):
            crit = None
            print('ERROR: Criterio mal ingresado, vuelva a intentar...')
    # ordeno por criterio
    print('')
    aux = lista.inicio
    while aux is not None:
        insertar(lista_aux, aux.info, crit)
        aux = aux.sig
    print('Mostrando Peliculas por ' + crit +'...')
    sleep(2)
    barrido_lista(lista_aux)

print(lista_peliculas(lista))
'''