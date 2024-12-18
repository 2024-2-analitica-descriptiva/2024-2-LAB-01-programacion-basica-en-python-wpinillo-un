"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    file_path = 'files/input/data.csv'
    
    grouped_data = {}

    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            letter = columns[0]
            value = int(columns[1])

            if letter not in grouped_data:
                grouped_data[letter] = []

            grouped_data[letter].append(value)

    result = [(letter, max(valores), min(valores)) for letter, valores in grouped_data.items()]
    sorted_result = sorted(result)

    return sorted_result
