import tkinter as tk
import random

user_score = 0
computer_score = 0

def determine_winner(user_choice):
    global user_score, computer_score
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    
    label_user_choice.config(text=f"Your choice: {user_choice}")
    label_computer_choice.config(text=f"Computer's choice: {computer_choice}")
    label_result.config(text=result)
    label_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    label_user_choice.config(text="Your choice: ")
    label_computer_choice.config(text="Computer's choice: ")
    label_result.config(text="")
    label_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

label_instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
label_instructions.pack()

button_rock = tk.Button(root, text="Rock", command=lambda: determine_winner("Rock"))
button_rock.pack()

button_paper = tk.Button(root, text="Paper", command=lambda: determine_winner("Paper"))
button_paper.pack()

button_scissors = tk.Button(root, text="Scissors", command=lambda: determine_winner("Scissors"))
button_scissors.pack()

label_user_choice = tk.Label(root, text="Your choice: ")
label_user_choice.pack()

label_computer_choice = tk.Label(root, text="Computer's choice: ")
label_computer_choice.pack()

label_result = tk.Label(root, text="")
label_result.pack()

label_score = tk.Label(root, text=f"Score - You: {user_score} | Computer: {computer_score}")
label_score.pack()

button_reset = tk.Button(root, text="Reset Game", command=reset_game)
button_reset.pack()

root.mainloop()