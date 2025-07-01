import random

def iniciar_juego():
    elementos = ["limón", "pera", "manzana"]
    # Generar lista inicial de 10 elementos aleatorios
    inventario = [random.choice(elementos) for _ in range(10)]

    print("\n¡Bienvenido al juego del intercambio!")
    print("Inventario inicial:", inventario)

    # Contar cuántos grupos de 1 limón, 1 pera y 1 manzana se pueden formar
    def contar_grupos(inventario):
        conteo_limon = inventario.count("limón")
        conteo_pera = inventario.count("pera")
        conteo_manzana = inventario.count("manzana")
        return min(conteo_limon, conteo_pera, conteo_manzana)

    grupos_posibles = contar_grupos(inventario)
    print(f"\nPuedes formar {grupos_posibles} grupo(s) de 1 limón, 1 pera y 1 manzana.")

    while True:
        print("\nMenú:")
        print("1. Canjear 2 grupos por un regalo y 2 elementos adicionales")
        print("2. Canjear un regalo por 6 elementos")
        print("3. Mostrar inventario")
        print("4. Salir del juego")

        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            if grupos_posibles >= 2:
                print("Inventario actual:", inventario)
                for _ in range(2):
                    inventario.remove("limón")
                    inventario.remove("pera")
                    inventario.remove("manzana")
                grupos_posibles -= 2
                inventario.append("regalo")
                print("Canjeaste 2 grupos de 1 limón, 1 pera y 1 manzana por un regalo.")

                elemento_extra1 = input("Elige un elemento adicional (limón, pera o manzana): ").strip()
                elemento_extra2 = input("Elige otro elemento adicional (limón, pera o manzana): ").strip()

                if elemento_extra1 in elementos:
                    inventario.append(elemento_extra1)
                else:
                    print(f"{elemento_extra1} no es válido. No se añadió al inventario.")

                if elemento_extra2 in elementos:
                    inventario.append(elemento_extra2)
                else:
                    print(f"{elemento_extra2} no es válido. No se añadió al inventario.")

                print(f"Tu inventario ahora es: {inventario}")
                grupos_posibles = contar_grupos(inventario)
                print(f"\nAhora puedes formar {grupos_posibles} grupo(s) de 1 limón, 1 pera y 1 manzana.")
            else:
                print("No tienes suficientes grupos para canjear un regalo.")

        elif opcion == "2":
            if "regalo" in inventario:
                inventario.remove("regalo")
                for _ in range(6):
                    nuevo_elemento = input("Elige un nuevo elemento (limón, pera o manzana): ").strip()
                    if nuevo_elemento in elementos:
                        inventario.append(nuevo_elemento)
                    else:
                        print(f"{nuevo_elemento} no es válido. Elige entre limón, pera o manzana.")
                print("Canjeaste un regalo por 6 nuevos elementos.")
                grupos_posibles = contar_grupos(inventario)
                print(f"\nAhora puedes formar {grupos_posibles} grupo(s) de 1 limón, 1 pera y 1 manzana.")
            else:
                print("No tienes un regalo para intercambiar.")

        elif opcion == "3":
            print("Inventario actual:", inventario)

        elif opcion == "4":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

        else:
            print("Opción no válida. Por favor, elige entre 1 y 4.")

# Iniciar el juego
iniciar_juego()
