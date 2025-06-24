def read_file_to_dict(datos):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    dictionary = dict()
    try:
        with open(datos, 'r') as file:
            linea = file.readline()
            inicio = 0
            for i in range(len(linea)):
                if linea[i] == ";":
                    venta = linea[inicio:i]
                    pos = venta.find(":")
                    if pos != -1:
                        key = venta[:pos]
                        value = float(venta[pos+1:])
                        if key not in dictionary:
                            dictionary[key] = [value]
                        else:
                            dictionary[key].append(value)
                    inicio = i+1
        return dictionary
    except FileNotFoundError:
        raise FileNotFoundError


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for producto, ventas in data.items():
        contador = 0
        for n in ventas:
            contador = float(contador + n)
            promedio = contador / len(ventas)
        ventas = contador
        print(f"{producto}: ventas totales ${ventas:.2f}, promedio ${promedio:.2f}")

