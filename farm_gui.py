import tkinter as tk
from tkinter import ttk, messagebox
from farm import Farm
from farm_animals import Cow, Chicken, Sheep, Pig, Horse
import threading
import time

class FarmGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🐄 Farm Animal Simulation 🐓")
        self.root.geometry("800x800")
        self.farm = Farm()
        self.selected_animal = None
        self.is_paused = True
        self.game_started = False
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
        self.style.configure("TButton", font=("Helvetica", 12))
        self.style.configure("Treeview", font=("Helvetica", 11))
        self.style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"))
        
        # Create main frame with padding
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=3)
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.rowconfigure(2, weight=2)
        
        # Create animal list
        self.create_animal_list()
        
        # Create control buttons
        self.create_control_buttons()
        
        # Create status display
        self.create_status_display()
        
        # Update initial animal list
        self.update_animal_list()
        
        # Start update thread
        self.running = True
        self.update_thread = threading.Thread(target=self.update_loop)
        self.update_thread.daemon = True
        self.update_thread.start()

    def create_animal_list(self):
        # Animal list frame
        list_frame = ttk.LabelFrame(self.main_frame, text="🐾 Animals (Click to select)", padding="10")
        list_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)
        
        # Create treeview with custom columns
        self.tree = ttk.Treeview(list_frame, columns=("Name", "Type", "Hunger", "Boredom", "Health", "Age", "Status"),
                                show="headings", height=15)
        
        # Configure columns
        columns = [
            ("Name", 150),
            ("Type", 100),
            ("Hunger", 100),
            ("Boredom", 100),
            ("Health", 100),
            ("Age", 80),
            ("Status", 100)
        ]
        
        for col, width in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor=tk.CENTER)
        
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Bind selection event
        self.tree.bind('<<TreeviewSelect>>', self.on_animal_select)

    def create_control_buttons(self):
        # Control buttons frame
        control_frame = ttk.LabelFrame(self.main_frame, text="🎮 Controls", padding="10")
        control_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Add start button at the top
        self.start_btn = ttk.Button(control_frame, text="▶️ Start Game", command=self.start_game, width=15)
        self.start_btn.grid(row=0, column=0, columnspan=2, pady=5)
        
        # Create sections for different types of controls
        care_frame = ttk.LabelFrame(control_frame, text="Care Options", padding="5")
        care_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Individual care buttons
        individual_frame = ttk.Frame(care_frame)
        individual_frame.grid(row=0, column=0, padx=5)
        ttk.Label(individual_frame, text="Individual Care:").grid(row=0, column=0, columnspan=2)
        ttk.Button(individual_frame, text="🍽️ Feed Selected", command=self.feed_selected, width=15).grid(row=1, column=0, padx=2)
        ttk.Button(individual_frame, text="🎮 Play with Selected", command=self.play_with_selected, width=15).grid(row=1, column=1, padx=2)
        
        # Group care buttons
        group_frame = ttk.Frame(care_frame)
        group_frame.grid(row=0, column=1, padx=5)
        ttk.Label(group_frame, text="Group Care:").grid(row=0, column=0, columnspan=2)
        ttk.Button(group_frame, text="🍽️ Feed All", command=self.feed_all, width=15).grid(row=1, column=0, padx=2)
        ttk.Button(group_frame, text="🎮 Play with All", command=self.play_with_all, width=15).grid(row=1, column=1, padx=2)
        
        # Breeding section
        breeding_frame = ttk.LabelFrame(control_frame, text="Breeding", padding="5")
        breeding_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Add breeding buttons with counts
        animal_types = [
            ("🐄 Cows", Cow),
            ("🐓 Chickens", Chicken),
            ("🐑 Sheep", Sheep),
            ("🐖 Pigs", Pig),
            ("🐎 Horses", Horse)
        ]
        
        for i, (text, animal_type) in enumerate(animal_types):
            count = self.farm.get_animal_count(animal_type)
            btn = ttk.Button(breeding_frame, 
                           text=f"{text} ({count})", 
                           command=lambda t=animal_type: self.breed_animals(t),
                           width=15)
            btn.grid(row=i//3, column=i%3, padx=5, pady=2)
        
        # Add new animal section
        add_frame = ttk.LabelFrame(control_frame, text="Add New Animals", padding="5")
        add_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        add_btn = ttk.Button(add_frame, text="➕ Add New Animal", command=self.show_add_animal_dialog, width=20)
        add_btn.grid(row=0, column=0, padx=5, pady=5)

    def show_add_animal_dialog(self):
        """Show dialog to add a new animal"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Animal")
        dialog.geometry("300x200")
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Create frame
        frame = ttk.Frame(dialog, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Animal type selection
        ttk.Label(frame, text="Select Animal Type:").grid(row=0, column=0, pady=5)
        animal_type = tk.StringVar()
        animal_types = [
            ("🐄 Cow", Cow),
            ("🐓 Chicken", Chicken),
            ("🐑 Sheep", Sheep),
            ("🐖 Pig", Pig),
            ("🐎 Horse", Horse)
        ]
        
        for i, (text, _) in enumerate(animal_types):
            ttk.Radiobutton(frame, text=text, variable=animal_type, value=text).grid(row=i+1, column=0, pady=2)
        
        def add_animal():
            selected_type = animal_type.get()
            if selected_type:
                # Extract animal class from selection
                animal_class = next(cls for text, cls in animal_types if text == selected_type)
                # Create new animal
                new_animal = animal_class(f"New{animal_class.__name__}{len(self.farm.animals) + 1}")
                self.farm.add_animal(new_animal)
                self.add_status_messages([f"Added new {animal_class.__name__} to the farm!"])
                self.update_animal_list()
                self.create_control_buttons()  # Update counts
                dialog.destroy()
            else:
                messagebox.showwarning("Warning", "Please select an animal type!")
        
        # Add button
        ttk.Button(frame, text="Add Animal", command=add_animal).grid(row=len(animal_types)+1, column=0, pady=10)

    def create_status_display(self):
        # Status display frame
        status_frame = ttk.LabelFrame(self.main_frame, text="📝 Status Messages", padding="10")
        status_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Create text widget with custom font
        self.status_text = tk.Text(status_frame, height=8, width=80, font=("Helvetica", 11))
        self.status_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(status_frame, orient=tk.VERTICAL, command=self.status_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.status_text.configure(yscrollcommand=scrollbar.set)

    def on_animal_select(self, event):
        """Handle animal selection"""
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            values = self.tree.item(item)['values']
            animal_name = values[0].split(' ')[1]  # Remove emoji and get name
            self.selected_animal = next((a for a in self.farm.animals if a.name == animal_name), None)
            self.add_status_messages([f"Selected animal: {animal_name}"])
        else:
            self.selected_animal = None

    def feed_selected(self):
        """Feed the selected animal"""
        if self.selected_animal:
            message = self.selected_animal.feed()
            self.add_status_messages([message])
            self.update_animal_list()
        else:
            self.add_status_messages(["Please select an animal first!"])

    def play_with_selected(self):
        """Play with the selected animal"""
        if self.selected_animal:
            message = self.selected_animal.play()
            self.add_status_messages([message])
            self.update_animal_list()
        else:
            self.add_status_messages(["Please select an animal first!"])

    def update_animal_list(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add current animals with emojis
        emoji_map = {
            "Cow": "🐄",
            "Chicken": "🐓",
            "Sheep": "🐑",
            "Pig": "🐖",
            "Horse": "🐎"
        }
        
        for animal in self.farm.animals:
            status = "❤️ Alive" if animal.is_alive else "💔 Deceased"
            animal_type = animal.__class__.__name__
            emoji = emoji_map.get(animal_type, "")
            
            self.tree.insert("", tk.END, values=(
                f"{emoji} {animal.name}",
                f"{emoji} {animal_type}",
                f"{'🍽️' if animal.hunger < 50 else '⚠️'} {animal.hunger}%",
                f"{'😊' if animal.boredom < 50 else '😫'} {animal.boredom}%",
                f"{'💪' if animal.health > 50 else '🤒'} {animal.health}%",
                f"{animal.age} days",
                status
            ))

    def feed_all(self):
        messages = self.farm.feed_all()
        self.add_status_messages(messages)
        self.update_animal_list()

    def play_with_all(self):
        messages = self.farm.play_with_all()
        self.add_status_messages(messages)
        self.update_animal_list()

    def breed_animals(self, animal_type):
        """Breed animals and update the interface"""
        message = self.farm.breed_animals(animal_type)
        self.add_status_messages([message])
        self.update_animal_list()
        # Update breeding buttons to show new counts
        self.create_control_buttons()

    def add_status_messages(self, messages):
        for message in messages:
            self.status_text.insert(tk.END, f"📢 {message}\n")
            self.status_text.see(tk.END)

    def start_game(self):
        """Start the game"""
        if not self.game_started:
            self.game_started = True
            self.is_paused = False
            self.start_btn.configure(text="⏸️ Pause Game", command=self.toggle_pause)
            self.add_status_messages(["Game started! Take care of your animals!"])
        else:
            self.toggle_pause()

    def toggle_pause(self):
        """Toggle game pause state"""
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.start_btn.configure(text="▶️ Resume Game")
            self.add_status_messages(["Game paused"])
        else:
            self.start_btn.configure(text="⏸️ Pause Game")
            self.add_status_messages(["Game resumed"])

    def check_game_over(self):
        """Check if all animals are dead"""
        alive_animals = [animal for animal in self.farm.animals if animal.is_alive]
        if not alive_animals:
            messagebox.showinfo("Game Over", "All animals have passed away. The game is over!")
            self.root.after(1000, self.root.destroy)  # Close the game after 1 second

    def update_loop(self):
        while self.running:
            if not self.is_paused:  # Only update if not paused
                messages = self.farm.update_all()
                if messages:
                    self.root.after(0, self.add_status_messages, messages)
                    self.root.after(0, self.update_animal_list)
                    self.root.after(0, self.check_game_over)  # Check for game over after each update
            time.sleep(5)  # Update every 5 seconds

    def on_closing(self):
        self.running = False
        self.root.destroy()

def main():
    root = tk.Tk()
    app = FarmGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main() 