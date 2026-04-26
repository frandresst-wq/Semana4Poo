class Persona:
    def __init__(self, nombre: str, rut: str):
        self._nombre = nombre
        self._rut = rut

    def mostrar_informacion(self):
        print(f"Nombre: {self._nombre}, RUT: {self._rut}")

    def obtener_nombre(self):
        return self._nombre

 class Estudiante(Persona):
    def __init__(self, nombre: str, rut: str, carrera: str):
        super().__init__(nombre, rut)
        self._carrera = carrera
        self._arancel_base = 238.000  # Ejemplo de arancel base
        self._porcentaje_beca = 0.0

    def mostrar_informacion(self):
        

    def aplicar_beca(self, porcentaje: float):
        self._porcentaje_beca = porcentaje

    def calcular_arancel_final(self):
        descuento = self._arancel_base * (self._porcentaje_beca / 100)
        return self._arancel_base - descuento