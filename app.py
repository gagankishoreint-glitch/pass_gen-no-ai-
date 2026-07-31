import random
import secrets
import string
import tkinter as tk
from tkinter import messagebox, ttk


# Core Configuration & Algorithms (Preserved from your original code)

SPECIAL_CHARACTERS = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "`",
    "~",
    "/",
    "?",
    "-",
]
GAGU_ALGORITHM = ("reverse", "skip", "change-to-special_characters")


def generate_diceware(num_words):
    """Algorithm 1: Diceware generator loading from dice.txt"""
    dice_map = {}
    try:
        with open("dice.txt", "r") as file:
            for line in file:
                parts = line.split()
                if len(parts) == 2:
                    dice_map[parts[0]] = parts[1]
    except FileNotFoundError:
        return None, "Error: 'dice.txt' file was not found in this folder!"

    if not dice_map:
        return None, "Error: 'dice.txt' is empty or invalid."

    password_pieces = []
    for _ in range(num_words):
        five_digit_roll = "".join(secrets.choice("123456") for _ in range(5))
        matched_word = dice_map.get(five_digit_roll, "word")
        password_pieces.append(matched_word)

    return "-".join(password_pieces), None


def generate_gagu(keywords):
    """Algorithm 2: GAGU generator using user-provided keywords"""
    password_divided = []
    valid_keywords = 0

    for keyword in keywords:
        keyword = keyword.strip()
        if not keyword or len(keyword) <= 2:
            continue

        valid_keywords += 1
        action = random.choice(GAGU_ALGORITHM)

        if action == "reverse":
            password_divided.append(keyword[::-1])
        elif action == "skip":
            continue
        elif action == "change-to-special_characters":
            password_divided.append(random.choice(SPECIAL_CHARACTERS))

    if valid_keywords == 0:
        return None, "Please enter keywords longer than 2 characters!"

    return "".join(password_divided), None


def generate_random(length, include_spec, custom_spec):
    """Algorithm 3: Standard random generator with custom specials"""
    string_set = string.ascii_letters + string.digits

    if include_spec:
        if custom_spec.strip():
            string_set += custom_spec.strip()
        else:
            string_set += "".join(SPECIAL_CHARACTERS)

    password_pieces = [secrets.choice(string_set) for _ in range(length)]
    return "".join(password_pieces), None

# Tkinter Graphical User Interface

class PasswordApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("480x520")
        self.root.resizable(False, False)

        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self._build_ui()

    def _build_ui(self):
        # Header Banner
        header = ttk.Label(
            self.root,
            text="🔐 Password Generator",
            font=("Helvetica", 16, "bold"),
        )
        header.pack(pady=12)

        #setup of tab
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(padx=15, pady=5, fill="both", expand=True)

        # Build individual tabs
        self.tab_diceware = ttk.Frame(self.notebook, padding=15)
        self.tab_gagu = ttk.Frame(self.notebook, padding=15)
        self.tab_random = ttk.Frame(self.notebook, padding=15)

        self.notebook.add(self.tab_diceware, text="🧠 Diceware")
        self.notebook.add(self.tab_gagu, text="⚡ GAGU Algo")
        self.notebook.add(self.tab_random, text="🎲 Random")

        self._setup_diceware_tab()
        self._setup_gagu_tab()
        self._setup_random_tab()

        # Shared Output Section at the bottom
        output_frame = ttk.LabelFrame(
            self.root, text=" Generated Password ", padding=12
        )
        output_frame.pack(padx=15, pady=12, fill="x")

        self.result_entry = ttk.Entry(
            output_frame, font=("Consolas", 12), justify="center"
        )
        self.result_entry.pack(fill="x", ipady=4, pady=(0, 8))

        copy_btn = ttk.Button(
            output_frame, text="📋 Copy to Clipboard", command=self.copy_pass
        )
        copy_btn.pack(fill="x")

    #Tab 1 Setup: Diceware
    def _setup_diceware_tab(self):
        ttk.Label(
            self.tab_diceware,
            text="Strong & Rememberable (Diceware)",
            font=("Helvetica", 11, "bold"),
        ).pack(anchor="w", pady=(0, 5))
        ttk.Label(
            self.tab_diceware,
            text="Generates passphrases using words from 'dice.txt'.",
            font=("Helvetica", 9, "italic"),
        ).pack(anchor="w", pady=(0, 15))

        ttk.Label(self.tab_diceware, text="Number of Words:").pack(anchor="w")
        self.dice_words_var = tk.IntVar(value=4)
        spin = ttk.Spinbox(
            self.tab_diceware,
            from_=2,
            to=10,
            textvariable=self.dice_words_var,
            width=10,
        )
        spin.pack(anchor="w", pady=(2, 15))

        gen_btn = ttk.Button(
            self.tab_diceware,
            text="Generate Diceware Passphrase",
            command=self.run_diceware,
        )
        gen_btn.pack(fill="x", pady=10)

    # Tab 2 Setup: GAGU Algo 
    def _setup_gagu_tab(self):
        ttk.Label(
            self.tab_gagu,
            text="GAGU Algorithm",
            font=("Helvetica", 11, "bold"),
        ).pack(anchor="w", pady=(0, 5))
        ttk.Label(
            self.tab_gagu,
            text="Enter catchy keywords (separated by commas).\nAvoid names, locations, or personal numbers!",
            font=("Helvetica", 9, "italic"),
        ).pack(anchor="w", pady=(0, 10))

        ttk.Label(
            self.tab_gagu, text="Keywords (e.g. coffee, monkey, summer):"
        ).pack(anchor="w")
        self.gagu_input = ttk.Entry(self.tab_gagu)
        self.gagu_input.pack(fill="x", pady=(2, 15))

        gen_btn = ttk.Button(
            self.tab_gagu, text="Run GAGU Algorithm", command=self.run_gagu
        )
        gen_btn.pack(fill="x", pady=10)

    # --- Tab 3 Setup: Random ---
    def _setup_random_tab(self):
        ttk.Label(
            self.tab_random,
            text="Random Character Generator",
            font=("Helvetica", 11, "bold"),
        ).pack(anchor="w", pady=(0, 5))

        ttk.Label(self.tab_random, text="Password Length:").pack(anchor="w")
        self.rand_len_var = tk.IntVar(value=14)
        len_spin = ttk.Spinbox(
            self.tab_random,
            from_=4,
            to=64,
            textvariable=self.rand_len_var,
            width=10,
        )
        len_spin.pack(anchor="w", pady=(2, 10))

        self.use_spec_var = tk.BooleanVar(value=True)
        spec_check = ttk.Checkbutton(
            self.tab_random,
            text="Include Special Characters",
            variable=self.use_spec_var,
        )
        spec_check.pack(anchor="w", pady=2)

        ttk.Label(
            self.tab_random, text="Custom Special Characters (Optional):"
        ).pack(anchor="w", pady=(8, 0))
        self.custom_spec_entry = ttk.Entry(self.tab_random)
        self.custom_spec_entry.pack(fill="x", pady=(2, 15))

        gen_btn = ttk.Button(
            self.tab_random,
            text="Generate Random Password",
            command=self.run_random,
        )
        gen_btn.pack(fill="x", pady=5)

    # --- Button Action Handlers ---
    def display_password(self, password):
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, password)

    def run_diceware(self):
        count = self.dice_words_var.get()
        password, error = generate_diceware(count)
        if error:
            messagebox.showerror("Error", error)
        else:
            self.display_password(password)

    def run_gagu(self):
        raw_text = self.gagu_input.get()
        keywords = [k for k in raw_text.split(",") if k.strip()]
        if not keywords:
            messagebox.showwarning(
                "Input Required", "Please enter at least one keyword!"
            )
            return

        password, error = generate_gagu(keywords)
        if error:
            messagebox.showwarning("Warning", error)
        elif not password:
            messagebox.showinfo(
                "Notice", "GAGU skipped all keywords! Try generating again."
            )
        else:
            self.display_password(password)

    def run_random(self):
        length = self.rand_len_var.get()
        use_spec = self.use_spec_var.get()
        custom_spec = self.custom_spec_entry.get()

        password, _ = generate_random(length, use_spec, custom_spec)
        self.display_password(password)

    def copy_pass(self):
        pwd = self.result_entry.get()
        if pwd:
            self.root.clipboard_clear()
            self.root.clipboard_append(pwd)
            messagebox.showinfo(
                "Success", "Password copied to clipboard successfully!"
            )
        else:
            messagebox.showwarning(
                "Empty", "No password generated yet to copy!"
            )


# -------------------------------------------------------------------
# Application Entry Point
# -------------------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordApp(root)
    root.mainloop()