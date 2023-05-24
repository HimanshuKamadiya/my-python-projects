import random
import tkinter as tk

# Range of the values of a dice
min_val = 1
max_val = 6

def roll_dice():
    # Clear the existing dice values
    dice_values.delete(1.0, tk.END)
    
    # Generate and display the 1st random integer from 1 to 6
    dice1_value = random.randint(min_val, max_val)
    dice_values.insert(tk.END, str(dice1_value) + "\n")
    
    # Generate and display the 2nd random integer from 1 to 6
    dice2_value = random.randint(min_val, max_val)
    dice_values.insert(tk.END, str(dice2_value) + "\n")
    
def quit_app():
    root.destroy()

# Create the GUI window
root = tk.Tk()
root.title("Dice Rolling")
root.geometry("250x200")

# Create a Text widget to display the dice values
dice_values = tk.Text(root, height=5, width=10)
dice_values.pack()

# Create a Roll Dice button
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack()

# Create a Quit button
quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack()

# Start the GUI event loop
root.mainloop()