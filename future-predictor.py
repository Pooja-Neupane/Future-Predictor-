import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random

# Class-based OOP structure
class FuturePredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 Future Predictor 🌟")
        self.root.geometry("400x400")
        self.root.config(bg="#f0f8ff")

        # UI Widgets
        tk.Label(root, text="Enter Your Name:", bg="#f0f8ff").pack(pady=5)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.pack()

        tk.Label(root, text="Enter Your Birthdate (YYYY-MM-DD):", bg="#f0f8ff").pack(pady=5)
        self.birthdate_entry = tk.Entry(root, width=30)
        self.birthdate_entry.pack()

        tk.Label(root, text="Enter Your Birthplace:", bg="#f0f8ff").pack(pady=5)
        self.birthplace_entry = tk.Entry(root, width=30)
        self.birthplace_entry.pack()

        tk.Button(root, text="Predict Future", command=self.predict_future, bg="#4682B4", fg="white").pack(pady=20)

        self.result_label = tk.Label(root, text="", wraplength=350, bg="#f0f8ff", fg="#2F4F4F", font=("Arial", 11, "italic"))
        self.result_label.pack(pady=10)

    def predict_future(self):
        name = self.name_entry.get()
        birthdate_str = self.birthdate_entry.get()
        birthplace = self.birthplace_entry.get()

        try:
            birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter the date in YYYY-MM-DD format.")
            return

        # Random predictions
        predictions = [
            "will achieve great success in the tech world 🌐💡",
            "is destined to inspire people through creativity 🎨✨",
            "will travel the world and share wisdom 🌍📘",
            "is going to build an innovative startup 💼🚀",
            "will spread positivity and light everywhere 🌞❤️",
            "will find peace, purpose, and power in their path 🌈🧘‍♀️",
        ]

        random.seed(len(name) + birthdate.year + len(birthplace))
        prediction = random.choice(predictions)

        result_text = f"{name.title()} from {birthplace.title()} (born on {birthdate.strftime('%B %d, %Y')})\n\n👉 {prediction}"
        self.result_label.config(text=result_text)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FuturePredictorApp(root)
    root.mainloop()
