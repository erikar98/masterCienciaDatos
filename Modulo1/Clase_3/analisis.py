dataset = [10, 20, 30, 40, 50]

def calcular_promedio(datos):
    return sum(datos) / len(datos)

def calcular_maximo(datos):
    return max(datos)

def mostrar_resumen(datos):
    print(f"Total de registros: {len(datos)}")
    print(f"Promedio: {calcular_promedio(datos)}")
    print(f"Máximo: {calcular_maximo(datos)}")