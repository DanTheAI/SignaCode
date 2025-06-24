import tkinter as tk
from tkinter import messagebox, ttk
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
        percentage = prob * 100
        result_var.set(f"Chance: {percentage:.2f}%")
    except Exception as e:
        messagebox.showerror("Input Error", str(e))

# Function to generate and display probability table for opening hand
def show_probability_table():
    try:
        N = int(entry_total_deck.get())
        K = int(entry_desired_cards.get())
        n = int(entry_draws.get())  # Opening hand size
        
        # Create a new window for the table
        table_window = tk.Toplevel(root)
        table_window.title("Opening Hand Probability Table")
        
        # Create a frame with scrollbars
        frame = tk.Frame(table_window)
        frame.pack(fill='both', expand=True)
        
        # Add a Treeview widget for the table
        columns = ["Cards in Hand", "Exact %", "At least this many %", "At most this many %"]
        tree = ttk.Treeview(frame, columns=columns, show='headings')
        
        # Add column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=120, anchor='center')
        
        # Calculate probabilities for each possible k value
        probs = []
        for k in range(min(n, K) + 1):
            prob = hypergeometric_probability(N, K, n, k)
            probs.append(prob)
        
        # Calculate cumulative probabilities
        cum_ge = [sum(probs[i:]) for i in range(len(probs))]  # Cumulative ≥ k
        cum_le = [sum(probs[:i+1]) for i in range(len(probs))]  # Cumulative ≤ k
        
        # Add data to the table with percentages
        for k in range(min(n, K) + 1):
            tree.insert("", "end", values=(
                k, 
                f"{probs[k]*100:.2f}%", 
                f"{cum_ge[k]*100:.2f}%", 
                f"{cum_le[k]*100:.2f}%"
            ))
        
        # Add scrollbars
        yscrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=yscrollbar.set)
        yscrollbar.pack(side="right", fill="y")
        
        tree.pack(fill="both", expand=True)
        
    except Exception as e:
        messagebox.showerror("Input Error", str(e))

# Add function for opening hand preset
def set_opening_hand():
    # Common opening hand sizes for different games
    games = {
        "Magic: The Gathering": {"deck": 60, "hand": 7},
        "Pokémon TCG": {"deck": 60, "hand": 7},
        "Yu-Gi-Oh!": {"deck": 40, "hand": 5},
        "Hearthstone": {"deck": 30, "hand": 3},
        "Legends of Runeterra": {"deck": 40, "hand": 4}
    }
    
    # Create selection dialog
    dialog = tk.Toplevel(root)
    dialog.title("Select Game")
    dialog.geometry("300x200")
    
    tk.Label(dialog, text="Select a game for opening hand:").pack(pady=10)
    
    game_var = tk.StringVar()
    game_dropdown = ttk.Combobox(dialog, textvariable=game_var, values=list(games.keys()))
    game_dropdown.pack(pady=5)
    game_dropdown.current(0)
    
    def apply_preset():
        game = game_var.get()
        if game in games:
            entry_total_deck.delete(0, tk.END)
            entry_total_deck.insert(0, games[game]["deck"])
            
            entry_draws.delete(0, tk.END)
            entry_draws.insert(0, games[game]["hand"])
            
            dialog.destroy()
    
    tk.Button(dialog, text="Apply", command=apply_preset).pack(pady=10)

# GUI setup
root = tk.Tk()
root.title("Card Game Opening Hand Calculator")

tk.Label(root, text="Total Deck Size (N):").grid(row=0, column=0, sticky="e", padx=5, pady=5)
tk.Label(root, text="Desired Cards in Deck (K):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
tk.Label(root, text="Opening Hand Size (n):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
tk.Label(root, text="Desired Cards in Hand (k):").grid(row=3, column=0, sticky="e", padx=5, pady=5)

entry_total_deck = tk.Entry(root)
entry_desired_cards = tk.Entry(root)
entry_draws = tk.Entry(root)
entry_successful_draws = tk.Entry(root)

entry_total_deck.grid(row=0, column=1, padx=5, pady=5)
entry_desired_cards.grid(row=1, column=1, padx=5, pady=5)
entry_draws.grid(row=2, column=1, padx=5, pady=5)
entry_successful_draws.grid(row=3, column=1, padx=5, pady=5)

# Button frame for better organization
button_frame = tk.Frame(root)
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Calculate", command=calculate_probability).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Show Table", command=show_probability_table).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Opening Hand Presets", command=set_opening_hand).pack(side=tk.LEFT, padx=5)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Helvetica", 14)).grid(row=5, column=0, columnspan=2, pady=10)

# Helpful instructions
instructions = """
Enter information about your deck and the cards you want to draw.
• Total Deck Size: Total number of cards in your deck
• Desired Cards: Number of specific cards you're looking for in the deck
• Opening Hand: Number of cards drawn in your opening hand
• Desired in Hand: How many of the desired cards you want in your opening hand
"""
tk.Label(root, text=instructions, justify=tk.LEFT, wraplength=350).grid(row=6, column=0, columnspan=2, pady=10, padx=10)

# Start the main event loop
root.mainloop()
