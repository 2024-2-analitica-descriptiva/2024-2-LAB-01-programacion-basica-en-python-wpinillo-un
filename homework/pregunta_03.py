"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    file_path = 'files/input/data.csv'

    letter_sum = {}

    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            if columns:
                letter = columns[0]
                value = int(columns[1])
                if letter in letter_sum:
                    letter_sum[letter] += value
                else:
                    letter_sum[letter] = value
                    
                    
    sorted_result = sorted(letter_sum.items())

    return sorted_result