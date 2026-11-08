# TP Final - Ejercicio 3
# Cálculo de emisiones de carbono


def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    # si el consumo es negativo no tiene sentido, así que lanzo un error
    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")

    # emisiones = consumo por el factor de emisión
    return consumo_kwh * factor_emision
