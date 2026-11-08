# TP Final - Ejercicio 3
# Cálculo de emisiones de carbono y métricas por planta


def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    # si el consumo es negativo no tiene sentido, así que lanzo un error
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")

    # emisiones = consumo por el factor de emisión
    return consumo_kwh * factor_emision


# ---------- PUNTO B ----------

def obtener_metricas_consumo(registros):
    # recibe una lista de diccionarios, por ejemplo:
    # [{"planta": "Norte", "consumo_kwh": 1200}, {"planta": "Sur", "consumo_kwh": 850}]
    # devuelve un diccionario con el total de emisiones y la planta que más consumió

    # si no hay registros devuelvo valores por defecto
    if not registros:
        return {"total_emisiones": 0.0, "planta_top": "Sin datos"}

    total_emisiones = 0.0
    consumo_por_planta = {}

    for registro in registros:
        # uso la función de arriba para calcular las emisiones de cada registro
        total_emisiones += calcular_emisiones_carbono(registro["consumo_kwh"])

        # voy sumando el consumo de cada planta
        planta = registro["planta"]
        consumo_por_planta[planta] = consumo_por_planta.get(planta, 0) + registro["consumo_kwh"]

    # la planta top es la que tiene el consumo total más alto
    planta_top = max(consumo_por_planta, key=consumo_por_planta.get)

    return {"total_emisiones": total_emisiones, "planta_top": planta_top}


# esto solo corre si ejecuto este archivo directamente
if __name__ == "__main__":
    registros_consumo = [
        {"planta": "Norte", "consumo_kwh": 1200},
        {"planta": "Sur", "consumo_kwh": 850},
        {"planta": "Norte", "consumo_kwh": 1400},
    ]
    metricas = obtener_metricas_consumo(registros_consumo)
    print(f"Total de emisiones: {metricas['total_emisiones']} kgCO2")
    print(f"Planta con mayor consumo: {metricas['planta_top']}")
