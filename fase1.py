__author__="Enrique Bonilla & Ernesto Ramirez"
__date__ ="$25-ene-2014 12:36:13$"



from CoreGraphics import concat
import nltk
from collections import Counter
import difflib

num_dat = 0; #contador del numero de dato que se esta procesando

datos = ["2@^Sept.^1@@0", "15/12/1990", "15/Sept/2013"] #debe de ser arreglo

fecha_num = list([] for i in range(len(datos))) #Arreglo que contendra las fechas numericas

fecha_cod = list([] for i in range(len(datos))) #Arreglo que contendra los codigos de las fechas

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

for f in datos:
    #Se obtienen cualquier caracter que no sea alfanumerico
    tokens = nltk.regexp_tokenize(f, '''\W+''')

    #lo juntamos en una sola palabra para poder hacer el conteo de caracteres
    tokens = ''.join(tokens)

     #Cuenta las veces que aparece un caracter. Lo guarda en el diccionario c.
    c = Counter(tokens)

    #Se necesita ahora acceder a los valores del diccionario, que son el numero
    #de repeticiones de cada caracter (claves).
    inv_c = {}
    for k,v in c.iteritems():
        inv_c[v]=inv_c.get(v,[])
        inv_c[v].append(k)

    #Obtener el caracter que se repite dos veces
    #Si no hay o si hay varios de ellos, entonces no se puede saber exactamente que
    #caracter es el separador y ese caso se deja para la siguiente fase.
    if inv_c.has_key(2):
        if len(inv_c[2])==1:
            #Se accede primero al caracter que tenga 2 repeticiones, esta regresa una
            #lista con un solo elemento. Accesamos el primer y unico elemento de la
            #lista con el comando [0].
            fecha = f.split(inv_c[2][0])
        else:
            print 'Mandar a la fase 2'
    else:
        #No se puede resolver en la fase 1. Marcar elemento para mandarlo a la fase2
        print 'Mandar a la fase 2'


    cont_alfa = 0 #contador de strings que no son numeros
    for s in fecha:
        if s.isdigit():
            s = int(s)
            fecha_num[num_dat].append(s)
            if 0 < s <=12:
                fecha_cod[num_dat].appeconcat(1)
            elif 12 < s < 31:
                fecha_cod[num_dat].append(2)
            elif s >31:
                fecha_cod[num_dat].append(3)
        else:
            cont_alfa = cont_alfa + 1
            if cont_alfa < 2:
                fecha_num[num_dat].append( difflib.get_close_matches(s, meses, 1, .25) )
                fecha_cod[num_dat].append(4)
            else:
                #No se puede resolver en la fase 1. Marcar elemento para mandarlo a la fase2
                print 'Mandar a la fase 2'
    

    num_dat = num_dat + 1

for x in fecha_num:
    print x

for x in fecha_cod:
    print x
