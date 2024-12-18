"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    file_path = 'files/input/data.csv'

    result = {}

    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            if len(columns) >= 5:
                key = columns[0].strip()
                try:
                    # Extraemos los valores después de los dos puntos en la columna 5
                    values = columns[4].strip().split(',')
                    total = sum(int(value.split(':')[1]) for value in values)
                except ValueError:
                    continue

                if key in result:
                    result[key] += total
                else:
                    result[key] = total

    result = dict(sorted(result.items()))
    return result
