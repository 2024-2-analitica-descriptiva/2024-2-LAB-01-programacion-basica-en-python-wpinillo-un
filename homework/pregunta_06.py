"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    file_path = 'files/input/data.csv'
    
    keys = {}

    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            if columns:
                dictionary = dict(item.split(':') for item in columns[4].split(','))
                dictionary = {k: int(v) for k, v in dictionary.items()}

                for key, value in dictionary.items():
                    if key not in keys:
                        keys[key] = [value, value]
                    else:
                        keys[key][0] = min(keys[key][0], value)
                        keys[key][1] = max(keys[key][1], value)
    
    result = [(key, values[0], values[1]) for key, values in keys.items()]
    result.sort()

    return result

