# TP Final - Ejercicio 3 - Punto B
# Vista del panel de sustentabilidad

from django.shortcuts import render

from emisiones import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    # historial de consumos de ejemplo (el mismo que usé en emisiones.py)
    registros_consumo = [
        {"planta": "Norte", "consumo_kwh": 1200},
        {"planta": "Sur", "consumo_kwh": 850},
        {"planta": "Norte", "consumo_kwh": 1400},
    ]

    # calculo las métricas con la función del otro archivo
    metricas = obtener_metricas_consumo(registros_consumo)

    # armo el diccionario de contexto que se le pasa al HTML
    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_top": metricas["planta_top"],
    }

    # renderizo la plantilla pasándole el contexto
    return render(request, "sustentabilidad/panel.html", contexto)
