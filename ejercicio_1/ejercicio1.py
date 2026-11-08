# TP Final - Ejercicio 1
# Limpieza y análisis de los sensores de EcoTech


def limpiar_registro_sensor(registro_raw):
    # recibe un diccionario con datos sucios y devuelve uno limpio

    # le saco los espacios al id
    sensor_id = registro_raw.get("sensor_id").strip()

    # a la temperatura le saco los espacios y la C, y la paso a float
    temperatura = float(registro_raw.get("temperatura").strip().replace("C", ""))

    # si no tiene la ubicacion, la dejo como "Desconocida"
    ubicacion = registro_raw.get("ubicacion", "Desconocida")

    # devuelvo un diccionario nuevo con todo limpio
    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion,
    }


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    # recibe la lista de sensores limpios y el umbral
    # devuelve una tupla: (ids en alerta, promedio de temperatura)

    # me quedo solo con los sensores que pasan el umbral
    en_alerta = filter(lambda s: s["temperatura"] > umbral_temperatura, lista_sensores_limpios)

    # de esos sensores saco solo el id
    lista_sensores_alerta = list(map(lambda s: s["sensor_id"], en_alerta))

    # promedio: sumo todas las temperaturas y divido por la cantidad
    total = sum(s["temperatura"] for s in lista_sensores_limpios)
    promedio_temperatura = total / len(lista_sensores_limpios)

    return (lista_sensores_alerta, promedio_temperatura)


# esto solo corre si ejecuto este archivo directamente
if __name__ == "__main__":
    # datos de prueba, el SENSOR-003 no tiene ubicacion
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": " 31.2C ", "ubicacion": "Planta Sur"},
        {"sensor_id": " SENSOR-003", "temperatura": "28.0C"},
    ]
    umbral = 25.0

    # limpio cada registro
    registros_limpios = []
    for sensor in registros_crudos:
        registros_limpios.append(limpiar_registro_sensor(sensor))

    # genero el resumen
    alertas, promedio = generar_resumen_sensores(registros_limpios, umbral)

    # imprimo reporte
    print("=== REPORTE DE SENSORES ===")
    print(f"Umbral de temperatura: {umbral}°C")
    print(f"Sensores en alerta: {alertas}")
    print(f"Promedio de temperatura: {promedio:.2f}°C")
