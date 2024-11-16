import tkinter as tk
from tkinter import messagebox
import json

def load_questions_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Hiba: A '{file_path}' fájl nem található.")
        return []
    except json.JSONDecodeError:
        print(f"Hiba: A '{file_path}' fájl hibás formátumú.")
        return []

class ClassKLR:
    def __init__(self, root):
        """Az osztály inicializálója, amely létrehozza a GUI elemeket és betölti a kérdéseket."""
        self.root = root
        self.root.title("Kvízjáték")
        self.questions = load_questions_from_file("questions.json")
        self.current_question_index = 0
        self.score = 0

        # GUI elemek létrehozása
        self.create_widgets()

        # Első kérdés betöltése
        self.load_question()

    def create_widgets(self):
        """Létrehozza a GUI elemeket (címke, gombok)."""
        self.question_label = tk.Label(self.root, text="", font=("Arial", 16), wraplength=400, justify="center")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Arial", 14), width=20,
                            command=lambda opt=i: self.check_answer(opt))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

    def load_question(self):
        """Betölti az aktuális kérdést és frissíti a GUI-t."""
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)
        else:
            self.end_quiz()

    def check_answer(self, selected_index):
        """Ellenőrzi a választ, és továbblép a következő kérdésre."""
        question_data = self.questions[self.current_question_index]
        selected_option = question_data["options"][selected_index]
        correct_answer = question_data["answer"]

        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Helyes válasz", "Helyes!")
        else:
            messagebox.showinfo("Rossz válasz", f"Rossz! A helyes válasz: {correct_answer}")

        self.current_question_index += 1
        self.load_question()

    def end_quiz(self):
        """Befejezi a kvízt, és megjeleníti az eredményt."""
        messagebox.showinfo("Játék vége", f"Kvíz vége! Az eredményed: {self.score}/{len(self.questions)} pont.")
        self.root.destroy()

def FunctionKLR():
    root = tk.Tk()  # Létrehozzuk a Tkinter ablakot
    app = ClassKLR(root)  # Létrehozzuk a kvízjáték osztály példányát
    root.mainloop()  # Elindítjuk a Tkinter főciklust