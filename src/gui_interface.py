from core import generate_password, calculate_entropy, assess_strength, estimate_crack_time
import tkinter as tk
from tkinter import messagebox

# Entry point for the GUI application
def run_gui():
    # Handle password generation and output display
    def on_generate():
        try:
            length = int(entry_length.get())
            password = generate_password(
                length, var_upper.get(), var_lower.get(), var_digits.get(), var_special.get()
            )
            entropy = calculate_entropy(password)
            strength, score = assess_strength(entropy)
            crack_time = estimate_crack_time(password)

            # Display the results
            output.delete("1.0", tk.END)
            output.insert(tk.END, f"Password: {password}\n")
            output.insert(tk.END, f"Entropy: {entropy:.2f} bits\n")
            output.insert(tk.END, f"Strength: {strength} ({score}/100)\n")
            output.insert(tk.END, f"Estimated crack time: {crack_time}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Create the main window
    root = tk.Tk()
    root.title("Password Generator")

    # Input: password length
    tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky="e")
    entry_length = tk.Entry(root)
    entry_length.insert(0, "12")
    entry_length.grid(row=0, column=1)

    # Options: character types
    var_upper = tk.BooleanVar(value=True)
    var_lower = tk.BooleanVar(value=True)
    var_digits = tk.BooleanVar(value=True)
    var_special = tk.BooleanVar(value=False)

    tk.Checkbutton(root, text="Include Uppercase", variable=var_upper).grid(row=1, column=0, columnspan=2, sticky="w")
    tk.Checkbutton(root, text="Include Lowercase", variable=var_lower).grid(row=2, column=0, columnspan=2, sticky="w")
    tk.Checkbutton(root, text="Include Digits", variable=var_digits).grid(row=3, column=0, columnspan=2, sticky="w")
    tk.Checkbutton(root, text="Include Special Characters", variable=var_special).grid(row=4, column=0, columnspan=2, sticky="w")

    # Button to generate the password
    tk.Button(root, text="Generate Password", command=on_generate).grid(row=5, column=0, columnspan=2, pady=10)

    # Output field for the results
    output = tk.Text(root, height=6, width=50)
    output.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    root.mainloop()
