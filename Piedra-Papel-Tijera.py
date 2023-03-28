#-------------------------------------#
#               Reglas                #
#-------------------------------------#
#     Tijeras corta papel             #
#     Papel cubre piedra              #
#     Piedra aplasta a lagarto        #
#     Lagarto envenena a Spock        #
#     Spock rompe las tijeras         #
#     Tijeras decapitan al lagarto    #
#     Lagarto se come el papel        #
#     Papel desaprueba a Spock        #
#     Spock vaporiza a piedra         #
#     Piedra aplasta a tijera         #
#-------------------------------------#

#-------------------------------------#
#               Rules                 #
#-------------------------------------#
# Scissors cut paper                  #
# Paper covers stone                  #
# Stone crushes lizard                #
# Lizard poisons Spock                #
# Spock breaks the scissors           #
# Scissors decapitate the lizard      #
# Lizard eats paper                   #
# Paper disapproves of Spock          #
# Spock vaporizes stone               #
# Rock crushes scissors               #
#-------------------------------------#

# Import libraries
from ast import main
from random import *
import os

# Funcion principal, main
def fStart():
    
    vIntentos = 0 # Intentos maximos van a ser 3, por ende lo inicializamos en 0 mientras.
    vVida = 0 # La vida maxima es para el jugador, porque este juego es el user vs la maquina
    while True:
        # Menu
        os.system("color 0B")
        os.system("cls")
        print("""
                ┌─────────────────────────────────────────────────────────┐
                │     Bienvenidos al juego de piedra papel y tijera...    │
                │_________________________________________________________│
                │                                                         │
                │    1- Jugar                                             │
                │    2- Reglas                                            │
                │    3- Salir                                             │
                │                                                         │
                └─────────────────────────────────────────────────────────┘ 
        """)
        vOp = int(input("¿Cual eliges? ")) # Se puede elegir entre 3 opciones dependiendo que se elija, las condiciones seran las siguientes.

        if (vOp == 1): # Si es = a 1.
            while True:
                os.system("color 0A")
                os.system("cls")
                vUsuario1 = []
                #vUsuario2 = [] # Por si queremos un 1 vs 1, de momento no se ha implementado
                vNombres = ['Piedra', 'Papel', 'Tijera', 'Lagarto', 'Spock'] # Almacenamos los valores del juego al usuario
                Maquina = ['Piedra', 'Papel', 'Tijera', 'Lagarto', 'Spock'] # E igualmente a la maquina

                # Caracteres aleatorios de la maquina
                Aleatorio = randrange(len(Maquina)) # Con esta funcion, nos permite tomar un valor dentro del array maquina, aleatoriamente
                Maquina = Maquina[Aleatorio] # Ese valor previamente seleccionado aleatoriamente va a ser igual al array maquina, es decir, se va a almacenar alli

                print("""
                ┌─────────────────────────────────────────────────────────┐
                │     Bienvenidos al juego de piedra papel y tijera...    │
                │_________________________________________________________│
                │                                                         │
                │    1- Piedra                                            │
                │    2- Papel                                             │
                │    3- Tijera                                            │
                │    4- Lagarto                                           │
                │    5- Spock                                             │
                │    6- Salir                                             │
                │                                                         │
                └─────────────────────────────────────────────────────────┘ 
                    """) # Imprimimos el menu del juego
                
                vOp = int(input("¿Cual eliges? ")) # Variable para preguntar al usuario

                if (vOp == 1): # Si la opcion elegida es igual a 1, pues el usuario eligio Piedra
                    vUsuario1 = vNombres[0]
                    
                elif (vOp == 2): # Si la opcion elegida es igual a 2, pues el usuario eligio Papel
                    vUsuario1 = vNombres[1]
                    
                elif (vOp == 3): # Si la opcion elegida es igual a 3, pues el usuario eligio Tijera
                    vUsuario1 = vNombres[2]
                    
                elif (vOp == 4): # Si la opcion elegida es igual a 3, pues el usuario eligio Lagarto
                    vUsuario1 = vNombres[3]
                    
                elif (vOp == 5): # Si la opcion elegida es igual a 4, pues el usuario eligio Spock
                    vUsuario1 = vNombres[4]
                    
                elif (vOp == 6): # Si la opcion elegida es igual a 5, pues el usuario eligio Salir
                    print("\nGracias por jugar")
                    os.system("pause")
                    fStart()

                else: # De lo contrario, la opcion que digito el usuario es no valida, no se encuentra en el menu
                    print("Opcion no valida, intentelo de nuevo")

                ##################################
                # CODIGO DEL - Jugador principal #
                ##################################
                
                print("")

                if (vUsuario1 == vNombres[1] and Maquina == vNombres[0]):
                    print("Ganaste, papel tapa piedra")
                    vIntentos = vIntentos + 1

                elif (vUsuario1 == vNombres[2] and Maquina == vNombres[1]):
                    print("Ganaste, Tijera corta papel")
                    vIntentos = vIntentos + 1

                elif (vUsuario1 == vNombres[0] and Maquina == vNombres[2]):
                    print("Ganaste, Piedra destruye tijera")
                    vIntentos = vIntentos + 1

                elif (vUsuario1 == vNombres[0] and Maquina == vNombres[3]):
                    print("Ganaste, piedra aplasta a lagarto")
                    vIntentos = vIntentos + 1

                elif (vUsuario1 == vNombres[3] and Maquina == vNombres[4]):
                    print("Ganaste, lagarto envenena a spock")
                    vIntentos = vIntentos + 1

                elif (vUsuario1 == vNombres[3] and Maquina == vNombres[1]):
                    print("Ganaste, lagarto devora a papel")
                    vIntentos = vIntentos + 1

                elif (vUsuario1 == vNombres[2] and Maquina == vNombres[3]):
                    print("Ganaste, tijera decapita a lagarto")
                    vIntentos = vIntentos + 1

                elif (vUsuario1 == vNombres[4] and Maquina == vNombres[2]):
                    print("Ganaste, Spock rompe a tijera")
                    vIntentos = vIntentos + 1

                elif (vUsuario1 == vNombres[1] and Maquina == vNombres[4]):
                    print("Ganaste, papel desautoriza a Spock")
                    vIntentos = vIntentos + 1

                elif (vUsuario1 == vNombres[4] and Maquina == vNombres[0]):
                    print("Ganaste, Spock vaporiza a piedra")
                    vIntentos = vIntentos + 1

                ################################
                # CODIGO DEL JUGADOR - maquina #
                ################################
                
                # Condiciones del juego
                if (Maquina == vNombres[1] and vUsuario1 == vNombres[0]):
                    print("Perdiste, papel tapa piedra")
                    vVida = vVida + 1

                elif (Maquina == vNombres[2] and vUsuario1 == vNombres[1]):
                    print("Perdiste, Tijera corta papel")
                    vVida = vVida + 1

                elif (Maquina == vNombres[0] and vUsuario1 == vNombres[2]):
                    print("Perdiste, Piedra destruye tijera")
                    vVida = vVida + 1

                elif (Maquina == vNombres[0] and vUsuario1 == vNombres[3]):
                    print("Perdiste, piedra aplasta a lagarto")
                    vVida = vVida + 1

                elif (Maquina == vNombres[3] and vUsuario1 == vNombres[4]):
                    print("Perdiste, lagarto envenena a spock")
                    vVida = vVida + 1

                elif (Maquina == vNombres[3] and vUsuario1 == vNombres[1]):
                    print("Perdiste, lagarto devora a papel")
                    vVida = vVida + 1

                elif (Maquina == vNombres[2]and vUsuario1 == vNombres[3]):
                    print("Perdiste, tijera decapita a lagarto")
                    vVida = vVida + 1

                elif (Maquina == vNombres[4] and vUsuario1 == vNombres[2]):
                    print("Perdiste, Spock rompe a tijera")
                    vVida = vVida + 1

                elif (Maquina == vNombres[1] and vUsuario1 == vNombres[4]):
                    print("Perdiste, papel desautoriza a Spock")
                    vVida = vVida + 1

                elif (Maquina == vNombres[4] and vUsuario1 == vNombres[0]):
                    print("Perdiste, Spock vaporiza a piedra")
                    vVida = vVida + 1

                # Empate
                elif (Maquina == vUsuario1):
                    print("Empate")

                # Contador de Intentos
                if (vOp != 6 and vOp != 7 and vOp <= 7):
                    print(f"\nGanadas por el usuario: {vIntentos}/3")
                    print(f"Ganadas por la maquina: {vVida}/3\n")

                # Finalizar ciclo * las vidas
                if (vVida == 3 or vIntentos == 3):

                    while True:

                        Salir = input("S -> Salir, N -> Seguir intentando. S/N: ").upper()

                        if (Salir == 'N'):
                            vIntentos = 0
                            vVida = 0
                            break

                        elif (Salir == 'S'):
                            fStart()

                        else:
                            print("Opcion no valida")
                            

                os.system("pause")
                
        ####################
        # Reglas del juego #
        ####################
        
        elif (vOp == 2):
            print("""
                Reglas del game:
                ─────────────────────────────────────────────────────────── 
                - Tijeras corta papel               
                - Papel cubre piedra
                - Piedra aplasta a lagarto
                - Lagarto envenena a Spock
                - Spock rompe las tijeras 
                - Tijeras decapitan al lagarto
                - Lagarto se come el papel
                - Papel desaprueba a Spock
                - Spock vaporiza a piedra
                - Piedra aplasta a tijera
                ─────────────────────────────────────────────────────────── 
                    """)
            os.system("pause")
        
        elif (vOp == 3):
            exit()
        
        else:
            print("Opcion no valida")
            os.system('pause')

fStart() # Llamado a la funcion Start que inicia el juego completamente.