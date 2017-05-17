# Importacion de librerias y funciones utilizadas.
import string
from collections import Counter

import nltk
import pandas as pd


def import_files(tx_path, lm_path, sw_path, vb_path):
    """Importacion de los ficheros con los datos para el analisis."""
    
    # o_text: string del texto original.
    with open(tx_path, 'r', encoding='utf8') as current_file:
        o_text = current_file.read()
        
    # lm_dict: diccionario lematizador.
    lm_df = pd.read_csv(lm_path, names=('col1', 'col2'))
    lm_dict = dict(zip(lm_df['col1'], lm_df['col2']))
    
    # sw_list: lista de stopwords (palabras sin significado propio).
    sw_df = pd.read_csv(sw_path, names=('col1',))
    sw_list = sw_df['col1'].tolist()
    
    # vb_list: lista de verbos.
    vb_df = pd.read_csv(vb_path, names=('col1',))
    vb_list = vb_df['col1'].tolist()

    return o_text, lm_dict, sw_list, vb_list


def single_tokens(o_text):
    """Tokenizacion del texto en palabras individuales."""
    
    # Se crea un string filtrado f_text a partir del string original o_text.
    # Unicamente incluiremos los caracteres alfabeticos y los espacios, para el 
    # resto de caracteres introducimos la cadena ' . ' que actuara de 
    # separador.
    f_text = ''
    for i in o_text:      
        if i.isalpha() or i.isspace():
            f_text += i
        else:
            f_text += ' . '
            
    # Se divide la cadena f_text en la lista s_tokens por espacios sin incluir
    # los puntos introducidos.
    s_tokens = [i for i in f_text.split() if i != '.']
    
    # Si una palabra en mayuscula existe tambien en minuscula podemos pasarla
    # a minuscula para homogeneizar los resultados.
    exist = set(s_tokens)
    for i, j in enumerate(s_tokens):
        if j.istitle():
            if j.lower() in exist:
                s_tokens[i] = j.lower()

    return s_tokens


def lemmatize(s_tokens, lm_dict):
    """Lematizacion de los tokens individuales."""
    
    # Cada token se busca en el diccionario lematizador y se coloca en su
    # lugar la palabra lematizada, si no se encuentra se deja tal cual.
    for i, j in enumerate(s_tokens):
        if j in lm_dict:
            s_tokens[i] = lm_dict[j]

    return s_tokens


def filter_tokens(s_tokens, vb_list, sw_list):
    """Filtracion de los tokens para eliminar las palabras no relevantes."""
    
    # Lista con todas las palabras a filtrar: stopwords + verbos + letras. 
    f = sw_list + vb_list + list(string.ascii_letters)
    
    # Ademas, se eliminan tambien los numeros.
    s_tokens = [i for i in s_tokens if i not in f and not i.isnumeric()]
    
    return s_tokens


def bigram_tokens(s_tokens):
    """Creacion de bigramas a partir de los tokens individuales."""
    
    # Se utiliza la funcion propia de la libreria NLTK
    b_tokens = list(nltk.bigrams(s_tokens))
    
    # Ordenamos por orden alfabetico las palabras dentro de los bigramas,
    # la razon de esto es que a la hora de hacer la cuenta sea lo mismo tener
    # (palabra A, palabra B) que (palabra B, palabra A)
    for i, j in enumerate(b_tokens):
        if j[0] > j[1]:
            b_tokens[i] = (j[1], j[0])

    return b_tokens


def compound_tokens(o_text):
    """Tokenizacion del texto original solamente con los nombres propios
    compuestos."""
    
    # Lista de palabras que sirven de "puente" entre dos nombres propios.
    joiners = ['de', 'la', 'los', 'del', 'las', 'el']
    
    # Se filtran los caracteres del mismo modo que en la funcion single_tokens.
    f_text = ''
    for i in o_text:
        if i.isalpha() or i.isspace():
            f_text += i
        else:
            f_text += ' . '
            
    # Creamos una lista f_list que solo incluira las palabras en mayuscula y 
    # las que se encuentren en la lista de joiners. Para el resto introducimos 
    # un punto que nos servira de separador.
    f_list = []
    for i in f_text.split():
        if i.lower() in joiners:
            f_list.append(i.lower())
        elif i.istitle():
            f_list.append(i)
        else:
            f_list.append('.')
            
    # Redefinimos la lista uniendola con espacios y dividiendola por puntos.
    f_list = ' '.join(f_list).split('.') 
    
    # Creamos otra lista c_tokens quedandonos unicamente con los elementos de 
    # la lista f_list que contengan mas de una palabra en mayuscula.
    c_tokens = []
    for i in f_list:
        n = 0
        for j in i.split():
            if j.istitle():
                n += 1
        if n > 1:
            c_tokens.append(i.strip())
        
    # Limpiamos los elementos de c_tokens asegurandonos de que empiezan y 
    # finalizan con una palabra en mayuscula.
    for i, j in enumerate(c_tokens):
        w = j.split()
        while not w[0].istitle():
            if not w[0].istitle():
                del w[0]
        while not w[-1].istitle():
            if not w[-1].istitle():
                del w[-1]
        c_tokens[i] = ' '.join(w)

    return c_tokens


def show_stats(tokens, n):
    """Funcion para mostrar por pantalla la cuenta de tokens unicos y totales,
    asi como los tokens mas comunes."""
    
    # La funcion Counter devuelve un diccionario {token: cantidad}.
    count = Counter(tokens)
    
    # Cantidad de tokens unicos. 
    unique = len(count)
    
    # Contidad de tokens totales.
    total = len(tokens)
    
    # Ratio tokens unicos vs tokens totales.
    if total > 0:
        ratio = round(unique / total, 2)
    else:
        ratio = None
        
    # Mostramos en pantalla los resultados.
    print("Unique: %s\nTotal: %s\nRatio: %s\nMost Common (%s):\n%s"
          % (unique, total, ratio, n, count.most_common(n)))


def main(tx_path, lm_path, sw_path, vb_path, n):
    """Funcion principal que dirige el flujo del algoritmo llamando al resto de
    funciones."""
    
    # Importacion de ficheros.
    print("Importing files...")
    o_text, lm_dict, sw_list, vb_list = import_files(tx_path, lm_path,
                                                     sw_path, vb_path)
    
    # Tokenizacion individual.
    print("Tokenizing text...")
    s_tokens = single_tokens(o_text)
    
    # Lematizacion.
    print("Lemmatizing single tokens...")
    s_tokens = lemmatize(s_tokens, lm_dict)
    
    # Filtrado.
    print("Filtering single tokens...")
    s_tokens = filter_tokens(s_tokens, sw_list, vb_list)
    
    # Tokenizacion en bigramas.
    print("Making bigram tokens...")
    b_tokens = bigram_tokens(s_tokens)
    
    # Tokenizacion en palabras compuestas.
    print("Searching compound tokens...")
    c_tokens = compound_tokens(o_text)
    
    # Muestra de resultados.
    print("\n<<Single-Tokens>>")
    show_stats(s_tokens, n)
    print("\n<<Bigram-Tokens>>")
    show_stats(b_tokens, n)
    print("\n<<Compound-Tokens>>")
    show_stats(c_tokens, n)


# Llamamos a la funcion principal con los ficheros de entrada y el numero de 
# resultados que queremos que aparezcan en pantalla.
main(tx_path='docs/paste_text.txt',
     lm_path='docs/lemmatization_es.txt',
     sw_path='docs/stopwords_es.txt',
     vb_path='docs/verbs_es.txt',
     n=10)
