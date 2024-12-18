"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    file_path = 'files/input/data.csv'
    
    result = {}

    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            if columns:
                letters = columns[3].strip().lower().split(',')
                value = int(columns[1])

                for letter in letters:
                    if letter in result:
                        result[letter] += value
                    else:
                        result[letter] = value

    result = dict(sorted(result.items()))

    return result
