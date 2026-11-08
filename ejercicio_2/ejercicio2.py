# TP Final - Ejercicio 2
# Productos de EcoTech: clases, excepciones y guardado en JSON

import json
import os


#  --- PUNTO A: clases y reglas de inventario ---

# Creo excepcion
class StockInvalidoError(Exception):
    pass


class DispositivoEcologico:
    def __init__(self, modelo, precio, stock):
        self.modelo = modelo
        self.precio = precio
        # uso el setter para que valide el stock desde el principio
        self.set_stock(stock)

    # Veo el stock que es privado con el getter
    def get_stock(self):
        return self.__stock

    # Valida que el stock no sea negativo con el setter
    def set_stock(self, nuevo_stock):
        if nuevo_stock < 0:
            raise StockInvalidoError("El stock no puede ser negativo.")
        self.__stock = nuevo_stock

    def obtener_ficha_tecnica(self):
        return f"Modelo: {self.modelo} | Precio: ${self.precio} | Stock: {self.get_stock()}"

    # convierto el objeto a diccionario para poder guardarlo en un JSON
    def a_diccionario(self):
        return {
            "modelo": self.modelo,
            "precio": self.precio,
            "stock": self.get_stock(),
        }


# PanelSolar hereda de DispositivoEcológico
class PanelSolar(DispositivoEcológico):
    def __init__(self, modelo, precio, stock, eficiencia_watts):
        super().__init__(modelo, precio, stock)
        # atributo propio del panel solar
        self.eficiencia_watts = eficiencia_watts

    # Sobrescribo la ficha técnica de la clase padre
    def obtener_ficha_tecnica(self):
        ficha_base = super().obtener_ficha_tecnica()
        return f"{ficha_base} | Potencia: {self.eficiencia_watts}W (Panel Solar de Alta Eficiencia)"

    # tambien sobrescribo el diccionario para agregar La potencia
    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["eficiencia_watts"] = self.eficiencia_watts
        return datos


#  --- PUNTO B: guardar el catalogo en JSON ---

class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        # paso cada objeto a diccionario
        lista_diccionarios = []
        for dispositivo in lista_dispositivos:
            lista_diccionarios.append(dispositivo.a_diccionario())

        # guardo la lista en el archivo JSON
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)


#   --- Bloque de prueba ---

if __name__ == "__main__":
    # creo los productos validos
    panel = PanelSolar("PanelSolar-500", 1500.0, 10, 500)
    termostato = DispositivoEcológico("Termostato-Pro", 350.0, 8)
    productos_validos = [panel, termostato]

    # muestro las fichas (polimorfismo)
    for producto in productos_validos:
        print(producto.obtener_ficha_tecnica())

    # pruebo agregar un stock negativo y capturo el error
    try:
        termostato.set_stock(-5)
    except StockInvalidoError as error:
        print(f"[ERROR CONTROLADO] {error}")

    # el stock no cambió porque dio error
    print(f"Stock del termostato sigue en: {termostato.get_stock()}")

    # guardo los productos validos en el JSON 
    ruta = os.path.join(os.path.dirname(__file__), "catalogo_ecotech.json")
    gestor = GestorInventario()
    gestor.guardar_catalogo_json(productos_validos, ruta)
    print("Catálogo guardado en catalogo_ecotech.json")
