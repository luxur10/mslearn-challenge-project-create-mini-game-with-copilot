import random

#El ganador se determina por la siguientes reglas:
#La Rock gana a las tijeras.
#Las Scissors ganan al papel.
#El Paper gana a la piedra.

#debes tener en cuenta en las interacciones del juego
#Donde el ordenador será su oponente y podrá elegir aleatoriamente uno de los elementos (rock, paper o scissors) por cada movimiento
#La interacción con el juego será a través de la consola (terminal).

#El jugador podrá elegir una de las tres opciones, rock, paper o scissors, y se le debería advertir en caso de introducir una opción no válida.
#En cada ronda, el jugador debe entrar en una de las opciones de la lista y ser informado de si ganó, perdió o empató con el oponente.
#Al final de cada ronda, el jugador elegirá si vuelve a jugar.
#Muestra la puntuación del jugador al final del juego.
#El minijuego debe controlar las entradas del usuario, colocarlas en minúsculas e informar al usuario si la opción no es válida.

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
        return "Player wins"
    else:
        return "Computer wins"

def play_game():
    score = 0
    play_again = True

    while play_again:
        valid_choices = ["rock", "paper", "scissors"]
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if player_choice not in valid_choices:
            print("Invalid choice. Please enter a valid option.")
            continue

        computer_choice = random.choice(valid_choices)
        result = determine_winner(player_choice, computer_choice)

        print(f"Player chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        print(f"Result: {result}")

        if result == "Player wins":
            score += 1
        elif result == "Computer wins":
            score -= 1

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input != "yes":
            play_again = False

    print(f"Final score: {score}")

play_game()

