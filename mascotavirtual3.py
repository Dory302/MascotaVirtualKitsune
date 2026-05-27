import time

nombre = "Kitsune"
energia = 100
hambre = 20
felicidad = 50

print(f"¡Bienvenido! Tu nuevo zorrito se llama: {nombre}")

opciones_menu = [
    "1.- Darle una manzana (Baja hambre)",
    "2.- Jugar a las carreras (Sube felicidad, gasta energía)",
    "3.- Hacerlo tomar una siesta (Sube energía)",
    "4.- Ver estado actual",
    "5.- Salir del juego"
]

while energia > 0 and hambre < 100:
    try:
        print("\n--- MENÚ DE OPCIONES ---")
        
        for opcion_texto in opciones_menu:
            print(opcion_texto)
        
        opcion = int(input("Selecciona una opción: "))
        
        if opcion == 1:
            hambre = hambre - 20
            if hambre < 0: 
                hambre = 0
            print(f"Alimentaste a {nombre}. ¡Ya no tiene tanta hambre!")
            
        elif opcion == 2:
            if energia < 20:
                print(f"{nombre} está muy cansado para jugar ahora.")
            else:
                energia = energia - 20
                felicidad = felicidad + 30
                hambre = hambre + 15
                
                print("\nPreparados, listos...")
                for i in range(3):
                    print("¡Fiuuuush! 🦊💨")
                    time.sleep(0.5)
                    
                print(f"Jugaste con {nombre}. ¡Está muy feliz pero cansado!")
                
        elif opcion == 3:
            energia = energia + 40
            if energia > 100: 
                energia = 100
            print(f"\n{nombre} se ha acurrucado...")
            
            for i in range(3):
                print("Zzz...")
                time.sleep(0.6)
                
            print(f"{nombre} durmió un rato y recuperó sus fuerzas.")
            
        elif opcion == 4:
            print("    /\_/\ ")
            print("   (^..^ )")
            print("    /   \ ")
            print(f"Mascota: {nombre}")
            print(f"Energía: {energia}/100")
            print(f"Hambre: {hambre}/100")
            print(f"Felicidad: {felicidad}")
            
        elif opcion == 5:
            print("\n¡Gracias por jugar! Adiós.")
            break
            
        else:
            print("Opción incorrecta, elige un número del 1 al 5.")
            
    except ValueError:
        print("\n¡Error! Por favor, ingresa un número válido del 1 al 5. No uses letras ni símbolos.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")

if energia <= 0:
    print(f"\nGame Over: {nombre} se quedó sin energía y se durmió profundamente.")
elif hambre >= 100:
    print(f"\nGame Over: Olvidaste alimentar a {nombre} y se escapó a buscar comida.")
