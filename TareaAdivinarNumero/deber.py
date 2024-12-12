import tkinter as tk
import random

class GameLogic:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(["Piedra", "Papel", "Tijera"])

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Empate"
        elif (player_choice == "Piedra" and computer_choice == "Tijera") or \
             (player_choice == "Tijera" and computer_choice == "Papel") or \
             (player_choice == "Papel" and computer_choice == "Piedra"):
            return "Jugador"
        else:
            return "Computadora"

    def update_score(self, winner):
        if winner == "Jugador":
            self.player_score += 1
        elif winner == "Computadora":
            self.computer_score += 1

class GameGUI:
    def __init__(self, root):
        self.logic = GameLogic()
        self.root = root
        self.root.title("Piedra, Papel o Tijera")
        self.setup_gui()

    def setup_gui(self):
        # Result label
        self.result_label = tk.Label(self.root, text="¡Bienvenido!", font=("Arial", 16))
        self.result_label.pack(pady=10)

        # Computer choice label
        self.computer_choice_label = tk.Label(self.root, text="La computadora eligió: ", font=("Arial", 12))
        self.computer_choice_label.pack(pady=10)

        # Score labels
        self.score_label = tk.Label(self.root, text="Jugador: 0 | Computadora: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        piedra_button = tk.Button(button_frame, text="Piedra", font=("Arial", 14), command=lambda: self.on_player_choice("Piedra"))
        piedra_button.grid(row=0, column=0, padx=10)

        papel_button = tk.Button(button_frame, text="Papel", font=("Arial", 14), command=lambda: self.on_player_choice("Papel"))
        papel_button.grid(row=0, column=1, padx=10)

        tijera_button = tk.Button(button_frame, text="Tijera", font=("Arial", 14), command=lambda: self.on_player_choice("Tijera"))
        tijera_button.grid(row=0, column=2, padx=10)

    def on_player_choice(self, choice):
        computer_choice = self.logic.get_computer_choice()
        winner = self.logic.determine_winner(choice, computer_choice)
        self.logic.update_score(winner)
        self.update_gui(winner, computer_choice)

    def update_gui(self, result, computer_choice):
        self.result_label.config(text=f"Resultado: {result}")
        self.computer_choice_label.config(text=f"La computadora eligió: {computer_choice}")
        self.score_label.config(text=f"Jugador: {self.logic.player_score} | Computadora: {self.logic.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = GameGUI(root)
    root.mainloop()

