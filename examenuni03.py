class Planeta:
    total_planetas = 0  

    def __init__(self, nombre, distancia):
        self.nombre = nombre
        self.distancia = distancia  
        Planeta.total_planetas += 1
        print(f"[+] Planeta registrado: {self.nombre}")

    def __del__(self):
        print(f"[-] Planeta eliminado: {self.nombre}")
        Planeta.total_planetas -= 1

    @classmethod
    def contar_planetas(cls):
        return cls.total_planetas


class NaveEspacial:
    total_naves = 0  

    def __init__(self, nombre, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad  
        self.destino = None
        self.misiones = []
        NaveEspacial.total_naves += 1
        print(f"[+] Nave registrada: {self.nombre}")

    def __del__(self):
        print(f"[-] Nave destruida: {self.nombre}")
        NaveEspacial.total_naves -= 1

    @classmethod
    def contar_naves(cls):
        return cls.total_naves

    def asignar_destino(self, planeta):
        self.destino = planeta
        print(f"{self.nombre} ahora tiene como destino: {planeta.nombre}")

    def calcular_tiempo_viaje(self):
        if self.destino:
            tiempo = self.destino.distancia / self.velocidad
            print(f"Tiempo estimado de viaje a {self.destino.nombre}: {tiempo:.2f} horas")
        else:
            print("No se ha asignado un destino aún.")

    def agregar_misiones(self, *misiones):
        self.misiones.extend(misiones)
        print(f"Misiones asignadas a {self.nombre}: {', '.join(self.misiones)}")



planetas = []
naves = []


def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar planeta")
        print("2. Registrar nave")
        print("3. Asignar destino a nave")
        print("4. Calcular tiempo de viaje")
        print("5. Mostrar información")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del planeta: ")
            distancia = float(input("Distancia desde la Tierra (millones de km): "))
            planetas.append(Planeta(nombre, distancia))

        elif opcion == "2":
            nombre = input("Nombre de la nave: ")
            velocidad = float(input("Velocidad (millones de km/h): "))
            nave = NaveEspacial(nombre, velocidad)
            naves.append(nave)
            misiones = input("Misiones adicionales (separadas por coma): ")
            if misiones.strip():
                nave.agregar_misiones(*[m.strip() for m in misiones.split(",")])

        elif opcion == "3":
            if not planetas or not naves:
                print("Debe registrar al menos una nave y un planeta.")
                continue
            for i, nave in enumerate(naves):
                print(f"{i + 1}. {nave.nombre}")
            idx_nave = int(input("Selecciona una nave por número: ")) - 1

            for j, planeta in enumerate(planetas):
                print(f"{j + 1}. {planeta.nombre}")
            idx_planeta = int(input("Selecciona un planeta como destino: ")) - 1

            naves[idx_nave].asignar_destino(planetas[idx_planeta])

        elif opcion == "4":
            for i, nave in enumerate(naves):
                print(f"{i + 1}. {nave.nombre}")
            idx_nave = int(input("Selecciona una nave para calcular tiempo: ")) - 1
            naves[idx_nave].calcular_tiempo_viaje()

        elif opcion == "5":
            print(f"\nTotal de planetas registrados: {Planeta.contar_planetas()}")
            for planeta in planetas:
                print(f"- {planeta.nombre}, distancia: {planeta.distancia} millones de km")

            print(f"\nTotal de naves registradas: {NaveEspacial.contar_naves()}")
            for nave in naves:
                destino = nave.destino.nombre if nave.destino else "Sin destino"
            print(f"- {nave.nombre}, velocidad: {nave.velocidad} millones km/h, destino: {destino}")
            if nave.misiones:
                    print(f"  Misiones: {', '.join(nave.misiones)}")

        elif opcion == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


menu()