from clases.pokemon import Pokemon # type: ignore

pokemones = []

def capturar_pokemon():
    nombre = input("Nombre del Pokémon: ")
    tipo = input("Tipo: ")
    ataque = int(input("Ataque inicial: "))
    defensa = int(input("Defensa inicial: "))
    salud = int(input("Salud inicial: "))
    nuevo = Pokemon(nombre, tipo, ataque, defensa, salud)
    pokemones.append(nuevo)

def entrenar_pokemon():
    if not pokemones:
        print("No tienes ningún Pokémon aún.")
        return

    listar_pokemones()
    i = int(input("Selecciona el número del Pokémon a entrenar: ")) - 1
    if 0 <= i < len(pokemones):
        print("Puedes ingresar mejoras específicas (ejemplo: 5 3 10) o dejar vacío.")
        args = input("Mejoras (ataque defensa salud): ").split()
        mejoras = [int(x) for x in args] if args else []
        pokemones[i].entrenar(*mejoras)
    else:
        print("Opción inválida.")

def listar_pokemones():
    if not pokemones:
        print("No tienes ningún Pokémon aún.")
    else:
        for idx, p in enumerate(pokemones, start=1):
            print(f"{idx}. {p.nombre} (Nivel {p.nivel}, Tipo {p.tipo})")

def ver_info():
    if not pokemones:
        print("No tienes ningún Pokémon aún.")
        return
    listar_pokemones()
    i = int(input("Selecciona el número del Pokémon: ")) - 1
    if 0 <= i < len(pokemones):
        pokemones[i].mostrar_info()
    else:
        print("Opción inválida.")

def atacar_pokemon():
    if len(pokemones) < 2:
        print("Necesitas al menos dos Pokémon.")
        return
    listar_pokemones()
    atacante = int(input("Selecciona el número del atacante: ")) - 1
    objetivo = int(input("Selecciona el número del objetivo: ")) - 1
    if 0 <= atacante < len(pokemones) and 0 <= objetivo < len(pokemones):
        pokemones[atacante].atacar(pokemones[objetivo])
    else:
        print("Opción inválida.")

def liberar_pokemon():
    if not pokemones:
        print("No tienes Pokémon para liberar.")
        return
    listar_pokemones()
    i = int(input("Selecciona el número del Pokémon a liberar: ")) - 1
    if 0 <= i < len(pokemones):
        liberado = pokemones.pop(i)
        del liberado
    else:
        print("Opción inválida.")

def menu():
    while True:
        print("""
--- MENÚ ENTRENADOR POKÉMON ---
1. Capturar Pokémon
2. Entrenar Pokémon
3. Ver información
4. Atacar
5. Ver total de Pokémon
6. Liberar Pokémon
7. Salir
------------------------------
""")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            capturar_pokemon()
        elif opcion == "2":
            entrenar_pokemon()
        elif opcion == "3":
            ver_info()
        elif opcion == "4":
            atacar_pokemon()
        elif opcion == "5":
            Pokemon.total_pokemons()
        elif opcion == "6":
            liberar_pokemon()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
