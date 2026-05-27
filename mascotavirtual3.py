nombre = "Kitsune"
energia = 100
hambre = 20
felicidad = 50

print(f"¡Bienvenido! Tu nuevo zorrito se llama: {nombre}")

# El juego sigue mientras tenga energía y no tenga demasiada hambre
while energia > 0 and hambre < 100:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1.- Darle una manzana (Baja hambre)")
    print("2.- Jugar a las carreras (Sube felicidad, gasta energía)")
    print("3.- Hacerlo tomar una siesta (Sube energía)")
    print("4.- Ver estado actual")
    print("5.- Salir del juego")
    
    opcion = input("Selecciona una opción: ")
    
    for i in range(3):
    hambre = hambre - 10

    if hambre < 0:
        hambre = 0

    print(f"Le diste una manzana #{i+1} a {nombre}")
        
    elif opcion == "2":
        if energia < 20:
            print(f"{nombre} está muy cansado para jugar ahora.")
        else:
            energia = energia - 20
            felicidad = felicidad + 30
            hambre = hambre + 15
            print(f"Jugaste con {nombre}. ¡Está muy feliz pero cansado!")
            
    elif opcion == "3":
        energia = energia + 40
        if energia > 100: 
            energia = 100
        print(f"{nombre} durmió un rato y recuperó sus fuerzas.")
        
    elif opcion == "4":
        print("    /\\_/\\ ")
        print("   (^. .^)")
        print("   /     \\ ")
        print(f"Mascota: {nombre}")
        print(f"Energía: {energia}/100")
        print(f"Hambre: {hambre}/100")
        print(f"Felicidad: {felicidad}")
        
    elif opcion == "5":
        print("¡Gracias por jugar! Adiós.")
        break
        
    else:
        print("Opción incorrecta, elige un número del 1 al 5.")

# Mensajes de fin de juego
if energia <= 0:
    print(f"\nGame Over: {nombre} se quedó sin energía y se durmió profundamente.")
elif hambre >= 100:
    print(f"\nGame Over: Olvidaste alimentar a {nombre} y se escapó a buscar comida.")
