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
        print(f"Nombre: {self._nombre}, RUT: {self._rut}, Carrera: {self._carrera}")

    def aplicar_beca(self, porcentaje: float):
        if 0 <= porcentaje <= 100:
            self._porcentaje_beca = porcentaje
            print(f"Beca aplicada: {porcentaje}% a {self._nombre}")
        else:
            print("Porcentaje de beca inválido. Debe estar entre 0 y 100.")

    def calcular_arancel_final(self):
        descuento = self._arancel_base * (self._porcentaje_beca / 100)
        total_a_pagar = self._arancel_base - descuento 
        return total_a_pagar
    
    