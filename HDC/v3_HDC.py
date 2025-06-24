import tkinter as tk
from tkinter import messagebox, ttk
from math import comb

# Global variables for K entries and toggle state
k_labels = []  # Labels for "cards in hand" entries
k_entries = []  # Entries for "cards in hand" values
k_deck_labels = []  # Labels for "desired cards in deck" entries
k_deck_entries = []  # Entries for "desired cards in deck" values
active_k_count = 1  # Default to showing just one K entry
max_k_entries = 10  # Maximum K entries (K1-K10)
toggle_expanded = False  # Toggle state for K expansion

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
        n = int(entry_draws.get())
        
        # Create result text with probabilities for each active K value
        result_text = []
        
        for i in range(active_k_count):
            try:
                K = int(k_deck_entries[i].get())  # Get K (desired cards in deck) for this entry
                k = int(k_entries[i].get())  # Get k (desired cards in hand) for this entry
                prob = hypergeometric_probability(N, K, n, k)
                percentage = prob * 100
                result_text.append(f"K{i+1}: {k}/{K} cards = {percentage:.2f}%")
            except ValueError:
                # Skip if entry is empty or invalid
                pass
        
        # Join results with newlines for display
        result_var.set("\n".join(result_text))
    except Exception as e:
        messagebox.showerror("Input Error", str(e))

# Function to generate and display probability table for opening hand
def show_probability_table():
    try:
        N = int(entry_total_deck.get())
        n = int(entry_draws.get())  # Opening hand size
        
        # Create a new window for the table
        table_window = tk.Toplevel(root)
        table_window.title("Opening Hand Probability Table")
        
        # Create a frame with scrollbars
        frame = tk.Frame(table_window)
        frame.pack(fill='both', expand=True)
        
        # Add a notebook for tabs if multiple K values are active
        if active_k_count > 1 and toggle_expanded:
            notebook = ttk.Notebook(frame)
            notebook.pack(fill='both', expand=True)
            
            # Create a tab for each K value
            for i in range(active_k_count):
                try:
                    K = int(k_deck_entries[i].get())  # Get K (desired cards in deck) for this entry
                    k_value = int(k_entries[i].get())  # Get k (desired cards in hand) for this entry
                    tab = tk.Frame(notebook)
                    notebook.add(tab, text=f"K{i+1}: {k_value}/{K}")
                    create_probability_table(tab, N, K, n, k_value)
                except ValueError:
                    # Skip if entry is empty or invalid
                    continue
        else:
            # Just show a single table for the first K value
            try:
                K = int(k_deck_entries[0].get())  # Get K (desired cards in deck) for first entry
                k_value = int(k_entries[0].get())  # Get k (desired cards in hand) for first entry
                create_probability_table(frame, N, K, n, k_value)
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid values for K1")
    except Exception as e:
        messagebox.showerror("Input Error", str(e))

# Helper function to create a probability table in the given container
def create_probability_table(container, N, K, n, target_k):
    # Add a Treeview widget for the table
    columns = ["Cards in Hand", "Exact %", "At least this many %", "At most this many %"]
    tree = ttk.Treeview(container, columns=columns, show='headings')
    
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
        
        # Highlight the target k value
        if k == target_k:
            item_id = tree.get_children()[-1]
            tree.item(item_id, tags=('highlight',))
    
    # Add highlight style
    tree.tag_configure('highlight', background='lightblue')
    
    # Add scrollbars
    yscrollbar = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=yscrollbar.set)
    yscrollbar.pack(side="right", fill="y")
    
    tree.pack(fill="both", expand=True)

# Function to toggle between single K and multiple K entries
def toggle_k_entries():
    global toggle_expanded, active_k_count
    
    toggle_expanded = not toggle_expanded
    
    if toggle_expanded:
        toggle_btn.config(text="Hide Multiple K")
        # Show K entries from K2 to active_k_count
        for i in range(1, active_k_count):
            k_deck_labels[i].grid()
            k_deck_entries[i].grid()
            k_labels[i].grid()
            k_entries[i].grid()
    else:
        toggle_btn.config(text="Show Multiple K")
        # Hide all K entries except the first one
        for i in range(1, max_k_entries):
            if i < len(k_deck_labels):
                k_deck_labels[i].grid_remove()
            if i < len(k_deck_entries):
                k_deck_entries[i].grid_remove()
            if i < len(k_labels):
                k_labels[i].grid_remove()
            if i < len(k_entries):
                k_entries[i].grid_remove()

# Function to add another K entry (up to max_k_entries)
def add_k_entry():
    global active_k_count
    
    if active_k_count < max_k_entries:
        active_k_count += 1
        
        # Create new entries if needed
        if active_k_count > len(k_entries):
            # Create new "Desired Cards in Deck" entry
            deck_label = tk.Label(k_frame, text=f"K{active_k_count} Desired Cards in Deck:")
            deck_entry = tk.Entry(k_frame)
            k_deck_labels.append(deck_label)
            k_deck_entries.append(deck_entry)
            
            # Create new "Cards in Hand" entry
            hand_label = tk.Label(k_frame, text=f"K{active_k_count} Cards in Hand:")
            hand_entry = tk.Entry(k_frame)
            k_labels.append(hand_label)
            k_entries.append(hand_entry)
        
        # Position and show the entries if toggle is expanded
        row_offset = (active_k_count - 1) * 2  # Each K set takes 2 rows
        
        k_deck_labels[active_k_count-1].grid(row=row_offset, column=0, sticky="e", padx=5, pady=2)
        k_deck_entries[active_k_count-1].grid(row=row_offset, column=1, padx=5, pady=2)
        
        k_labels[active_k_count-1].grid(row=row_offset+1, column=0, sticky="e", padx=5, pady=2)
        k_entries[active_k_count-1].grid(row=row_offset+1, column=1, padx=5, pady=2)
        
        # Hide if toggle is not expanded (except first entry)
        if not toggle_expanded and active_k_count > 1:
            k_deck_labels[active_k_count-1].grid_remove()
            k_deck_entries[active_k_count-1].grid_remove()
            k_labels[active_k_count-1].grid_remove()
            k_entries[active_k_count-1].grid_remove()
            
        # Enable remove button when we have more than one entry
        if active_k_count > 1:
            remove_k_btn.config(state=tk.NORMAL)
            
        # Disable add button if we've reached the maximum
        if active_k_count >= max_k_entries:
            add_k_btn.config(state=tk.DISABLED)

# Function to remove a K entry
def remove_k_entry():
    global active_k_count
    
    if active_k_count > 1:
        # Hide the last entries
        k_deck_labels[active_k_count-1].grid_remove()
        k_deck_entries[active_k_count-1].grid_remove()
        k_labels[active_k_count-1].grid_remove()
        k_entries[active_k_count-1].grid_remove()
        
        active_k_count -= 1
        
        # Disable remove button if we're back to one entry
        if active_k_count <= 1:
            remove_k_btn.config(state=tk.DISABLED)
            
        # Enable add button if we're below max
        if active_k_count < max_k_entries:
            add_k_btn.config(state=tk.NORMAL)

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

# Main form entries
tk.Label(root, text="Total Deck Size (N):").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_total_deck = tk.Entry(root)
entry_total_deck.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Opening Hand Size (n):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_draws = tk.Entry(root)
entry_draws.grid(row=1, column=1, padx=5, pady=5)

# Frame for K entries
k_frame = tk.Frame(root)
k_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Lists to store K labels and entries
k_deck_labels = []  # "Desired Cards in Deck" labels
k_deck_entries = []  # "Desired Cards in Deck" entries
k_labels = []        # "Cards in Hand" labels
k_entries = []       # "Cards in Hand" entries

# Create first K entry (always visible)
# Desired Cards in Deck entry
deck_label = tk.Label(k_frame, text="K1 Desired Cards in Deck:")
deck_entry = tk.Entry(k_frame)
k_deck_labels.append(deck_label)
k_deck_entries.append(deck_entry)
deck_label.grid(row=0, column=0, sticky="e", padx=5, pady=2)
deck_entry.grid(row=0, column=1, padx=5, pady=2)

# Cards in Hand entry
hand_label = tk.Label(k_frame, text="K1 Cards in Hand:")
hand_entry = tk.Entry(k_frame)
k_labels.append(hand_label)
k_entries.append(hand_entry)
hand_label.grid(row=1, column=0, sticky="e", padx=5, pady=2)
hand_entry.grid(row=1, column=1, padx=5, pady=2)

# K toggle and controls frame
k_controls = tk.Frame(root)
k_controls.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

toggle_btn = tk.Button(k_controls, text="Show Multiple K", command=toggle_k_entries)
toggle_btn.pack(side=tk.LEFT, padx=5)

add_k_btn = tk.Button(k_controls, text="Add K", command=add_k_entry)
add_k_btn.pack(side=tk.LEFT, padx=5)

remove_k_btn = tk.Button(k_controls, text="Remove K", command=remove_k_entry, state=tk.DISABLED)
remove_k_btn.pack(side=tk.LEFT, padx=5)

# Button frame for calculation actions
button_frame = tk.Frame(root)
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

tk.Button(button_frame, text="Calculate", command=calculate_probability).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Show Table", command=show_probability_table).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Opening Hand Presets", command=set_opening_hand).pack(side=tk.LEFT, padx=5)

# Result display
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Helvetica", 14)).grid(row=5, column=0, columnspan=2, pady=10)

# Helpful instructions
instructions = """
Enter information about your deck and the cards you want to draw.
• Total Deck Size: Total number of cards in your deck
• Opening Hand: Number of cards drawn in your opening hand
• K1-K10 Desired Cards: Number of specific cards of each type in the deck
• K1-K10 Cards in Hand: How many of each type you want in your hand
• Use multiple K values to calculate probabilities for different card types
"""
tk.Label(root, text=instructions, justify=tk.LEFT, wraplength=350).grid(row=6, column=0, columnspan=2, pady=10, padx=10)

# Start the main event loop
root.mainloop()
