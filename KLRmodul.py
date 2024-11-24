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
    """Az osztály inicializálója."""
    def __init__(self, root):
        self.root = root
        self.root.title("Manchester United kvíz")
        self.questions = load_questions_from_file("questions.json")
        self.current_question_index = 0
        self.score = 0
        self.create_widgets()
        self.load_question()

    """Létrehozza a GUI elemeket."""
    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Arial", 16), wraplength=400, justify="center")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Arial", 14), width=20,
                            command=lambda opt=i: self.check_answer(opt))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

    """Betölti az aktuális kérdést és frissíti a GUI-t."""
    def load_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option)
        else:
            self.end_quiz()

    """Ellenőrzi a választ, és továbblép a következő kérdésre."""
    def check_answer(self, selected_index):
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

    """Befejezi a kvízt, és megjeleníti az eredményt."""
    def end_quiz(self):
        messagebox.showinfo("Játék vége", f"Kvíz vége! Az eredményed: {self.score}/{len(self.questions)} pont.")
        self.root.destroy()

def FunctionKLR():
    if __name__ == "__main__":
        root = tk.Tk()  #  Tkinter ablakot
        app = ClassKLR(root)  # A kvízjáték osztály példánya
        root.mainloop()  # A Tkinter főciklust