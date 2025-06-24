import tkinter as tk
from tkinter import messagebox
from math import comb

# Function to calculate hypergeometric probability
def hypergeometric_probability(N, K, n, k):
    try:
        return (comb(K, k) * comb(N - K, n - k)) / comb(N, n)
    except ValueError:
        return 0

# Function to handle button click and update result
def calculate_probability():
    try:
        N = int(entry_total_deck.get())
        K = int(entry_desired_cards.get())
        n = int(entry_draws.get())
        k = int(entry_successful_draws.get())

        prob = hypergeometric_probability(N, K, n, k)
        result_var.set(f"Probability: {prob:.6f}")
    except Exception as e:
        messagebox.showerror("Input Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Hypergeometric Distribution Calculator")

tk.Label(root, text="Total Deck Size (N):").grid(row=0, column=0, sticky="e")
tk.Label(root, text="Desired Cards in Deck (K):").grid(row=1, column=0, sticky="e")
tk.Label(root, text="Number of Draws (n):").grid(row=2, column=0, sticky="e")
tk.Label(root, text="Successful Draws (k):").grid(row=3, column=0, sticky="e")

entry_total_deck = tk.Entry(root)
entry_desired_cards = tk.Entry(root)
entry_draws = tk.Entry(root)
entry_successful_draws = tk.Entry(root)

entry_total_deck.grid(row=0, column=1)
entry_desired_cards.grid(row=1, column=1)
entry_draws.grid(row=2, column=1)
entry_successful_draws.grid(row=3, column=1)

tk.Button(root, text="Calculate", command=calculate_probability).grid(row=4, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Helvetica", 14)).grid(row=5, column=0, columnspan=2)

# Save the GUI script for user
gui_script_path = "/mnt/data/hypergeometric_gui.py"
with open(gui_script_path, "w") as f:
    f.write('''import tkinter as tk
from tkinter import messagebox
from math import comb

def hypergeometric_probability(N, K, n, k):
    try:
        return (comb(K, k) * comb(N - K, n - k)) / comb(N, n)
    except ValueError:
        return 0

def calculate_probability():
    try:
        N = int(entry_total_deck.get())
        K = int(entry_desired_cards.get())
        n = int(entry_draws.get())
        k = int(entry_successful_draws.get())

        prob = hypergeometric_probability(N, K, n, k)
        result_var.set(f"Probability: {prob:.6f}")
    except Exception as e:
        messagebox.showerror("Input Error", str(e))

root = tk.Tk()
root.title("Hypergeometric Distribution Calculator")

tk.Label(root, text="Total Deck Size (N):").grid(row=0, column=0, sticky="e")
tk.Label(root, text="Desired Cards in Deck (K):").grid(row=1, column=0, sticky="e")
tk.Label(root, text="Number of Draws (n):").grid(row=2, column=0, sticky="e")
tk.Label(root, text="Successful Draws (k):").grid(row=3, column=0, sticky="e")

entry_total_deck = tk.Entry(root)
entry_desired_cards = tk.Entry(root)
entry_draws = tk.Entry(root)
entry_successful_draws = tk.Entry(root)

entry_total_deck.grid(row=0, column=1)
entry_desired_cards.grid(row=1, column=1)
entry_draws.grid(row=2, column=1)
entry_successful_draws.grid(row=3, column=1)

tk.Button(root, text="Calculate", command=calculate_probability).grid(row=4, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Helvetica", 14)).grid(row=5, column=0, columnspan=2)

root.mainloop()
''')

gui_script_path
