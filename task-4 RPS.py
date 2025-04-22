import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x500")
root.config(bg="#523A28")
root.resizable(False, False)

choices = ["Rock", "Paper", "Scissors"]
emojis = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌️"
}

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_hand.config(text=emojis[user_choice])
    comp_hand.config(text=emojis[computer_choice])

    if user_choice == computer_choice:
        result.set("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        user_score += 1
        result.set("You win!")
    else:
        computer_score += 1
        result.set("Computer wins!")

    user_score_label.config(text=f"You: {user_score}")
    comp_score_label.config(text=f"Computer: {computer_score}")

# Title
tk.Label(root, text="Rock Paper Scissors", fg="white",font=("Arial", 20, "bold"), bg="#523A28").pack(pady=10)
tk.Label(root, text="Try your luck!", fg="#DDDDA4", font=("Arial", 12), bg="#523A28").pack()

# Score Frame
score_frame = tk.Frame(root, bg="#523A28")
score_frame.pack(pady=10)

user_score_label = tk.Label(score_frame, text="You: 0", font=("Arial", 14), bg="#523A28" ,fg="white")
comp_score_label = tk.Label(score_frame, text="Computer: 0", font=("Arial", 14), bg="#523A28",fg="white")
user_score_label.grid(row=0, column=0, padx=50)
comp_score_label.grid(row=0, column=1, padx=50)

# Hands
hands_frame = tk.Frame(root, bg="#523A28")
hands_frame.pack(pady=10)

user_hand = tk.Label(hands_frame, text="❓", font=("Arial", 40), bg="black", fg="#E4D4C8", width=4, height=2)
comp_hand = tk.Label(hands_frame, text="❓", font=("Arial", 40), bg="black", fg="#E4D4C8", width=4, height=2)
user_hand.grid(row=0, column=0, padx=50)
comp_hand.grid(row=0, column=1, padx=50)

# Result Label
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 14), fg="#FFCDB2", bg="#523A28")
result_label.pack(pady=10)

tk.Label(root, text="Choose One!", font=("Arial", 12, "bold"), fg="#FFB4A2", bg="#523A28").pack()

# Buttons Frame
button_frame = tk.Frame(root, bg="#523A28")
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="✊", font=("Arial", 20), width=4, command=lambda: play("Rock"))
paper_btn = tk.Button(button_frame, text="✋", font=("Arial", 20), width=4, command=lambda: play("Paper"))
scissors_btn = tk.Button(button_frame, text="✌️", font=("Arial", 20), width=4, command=lambda: play("Scissors"))

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

root.mainloop()
