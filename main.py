# main.py
import tkinter as tk
from KLRmodul import QuizApp  # A quiz_app.py-ban lévő QuizApp osztály importálása

def main():
    root = tk.Tk()  # Létrehozzuk a Tkinter ablakot
    app = QuizApp(root)  # Létrehozzuk a kvízjáték osztály példányát
    root.mainloop()  # Elindítjuk a Tkinter főciklust

if __name__ == "__main__":  # Ha közvetlenül futtatjuk a fájlt
    main()  # Elindítjuk a programot