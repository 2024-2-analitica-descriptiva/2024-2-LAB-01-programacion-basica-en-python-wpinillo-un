"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    file_path = 'files/input/data.csv'
    
    key_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            if len(columns) >= 5:
                keys = columns[4].split(',')
                for key in keys:
                    key_name = key.split(':')[0]
                    if key_name in key_count:
                        key_count[key_name] += 1
                    else:
                        key_count[key_name] = 1

    sorted_result = dict(sorted(key_count.items()))

    return sorted_result
