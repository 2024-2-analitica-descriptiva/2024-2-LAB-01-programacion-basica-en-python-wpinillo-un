"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    file_path = 'files/input/data.csv'
    
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            if columns:
                total_sum += int(columns[1])

    return total_sum
