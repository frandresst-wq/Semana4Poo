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
    
class Docente(Persona):
    def __init__(self, nombre: str, rut: str, especialidad: str):
        super().__init__(nombre, rut)
        self._especialidad = especialidad

    def mostrar_informacion(self):
        print(f"[Docente] {self._nombre} | RUT: {self._rut} | Especialidad: {self._especialidad}")

class Asignatura:
    def __init__(self, id_asignatura: str, nombre_asignatura: str):
        self._id_asignatura = id_asignatura
        self._nombre_asignatura = nombre_asignatura

    def obtener_nombre_asignatura(self):
        return self._nombre_asignatura

class Curso:
    def __init__(self, asignatura: Asignatura, docente: Docente, semestre: str):
        self._asignatura = asignatura
        self._docente = docente
        self._semestre = semestre
        self._estudiantes_inscritos = []
        self._calificaciones = {}

    def inscribir_estudiante_curso(self, estudiante: Estudiante):
        if estudiante not in self._estudiantes_inscritos:
            self._estudiantes_inscritos.append(estudiante)
            self._calificaciones[estudiante.obtener_nombre()] = []     
            print(f"Estudiante {estudiante.obtener_nombre()} inscrito en el curso de {self._asignatura.obtener_nombre_asignatura()}.")
            return True
        else:
            print(f"El estudiante {estudiante.obtener_nombre()} ya está inscrito en este curso.")
            return False

    def asignar_calificacion(self, estudiante: Estudiante, calificacion: float):
        nombre_est = estudiante.obtener_nombre()
        if nombre_est in self._calificaciones:
            if 1.0 <= calificacion <= 7.0:
                self._calificaciones[nombre_est].append(calificacion)
                print(f"Calificación {calificacion} asignada a {nombre_est} en {self._asignatura.obtener_nombre_asignatura()}.")
            else:
                print("Calificación inválida. Debe estar entre 1.0 y 7.0.")
        else:
            print(f"El estudiante {nombre_est} no está inscrito en este curso.")

    def determinar_aprobacion(self, estudiante: Estudiante):
        nombre_est = estudiante.obtener_nombre()
        if nombre_est in self._calificaciones:
            calificaciones = self._calificaciones[nombre_est]
            if calificaciones:
                promedio = sum(calificaciones) / len(calificaciones)
                aprobado = promedio >= 4.0
                estado = "aprobado" if aprobado else "reprobado"
                print(f"El estudiante {nombre_est} ha {estado} con un promedio de {promedio:.2f}.")
                return aprobado
            else:
                print(f"No hay calificaciones registradas para el estudiante {nombre_est}.")
                return False
        else:
            print(f"El estudiante {nombre_est} no está inscrito en este curso.")
            return False

# Ejemplo de uso
if __name__ == "__main__":
    
    asignatura_poo = Asignatura("IT1617A-711-CH2026-T1", "Programación Orientada a Objetos")
    docente_pablo = Docente("PABLO LASTRA CID", "18.144.701-K", "Astronomía")
    est_franco = Estudiante("Franco", "19.155.619-4", "Ingeniería en Informática")  

    docente_pablo.mostrar_informacion()
    est_franco.mostrar_informacion()

    est_franco.aplicar_beca(50)  # Aplica una beca del 50%
    print(f"Arancel final a pagar por {est_franco.obtener_nombre()}: ${est_franco.calcular_arancel_final():.2f}")

    curso_poo_sem1 = Curso(asignatura_poo, docente_pablo, "2026-1")
    curso_poo_sem1.inscribir_estudiante_curso(est_franco)

    curso_poo_sem1.asignar_calificacion(est_franco, 7.0)
    curso_poo_sem1.asignar_calificacion(est_franco, 7.0)
    curso_poo_sem1.determinar_aprobacion(est_franco)

       