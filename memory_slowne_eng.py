import tkinter as tk
from tkinter import RIGHT, TOP
import time
import re

# Constants:
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
HOW_TO_PLAY_TEXT_PL = 'The goal of this game is simple: get as much points as you can\n through remembering' \
                      ' and spelling them correctly\nYou can choose between three difficulty levels: easy, medium' \
                      ' and hard.\n' \
                      ' Each one has a different set of words.\n' \
                      'After remembering those words, enter them\n by your keyboard' \
                      ' into the input aera,' \
                      ' and then push the Ok button.\nFor each correct answer you get points.\n' \
                      'At the end of every match you can see your score.\n Good luck!'

with open("easy_ENG.txt", "r", encoding="utf-8") as ef:
    lines_easy = ef.read()

with open("medium_ENG.txt", "r", encoding="utf-8") as mf:
    lines_medium = mf.read()

with open("hard_ENG.txt", "r", encoding="utf-8") as hf:
    lines_hard = hf.read()

sprawdzanie = []


# Windows:
class MenuWindowEng:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title("Memory Słowne")
        self.root.configure(bg="#79CBF7")

        # Title settings
        self.title = tk.Label(self.root, text="Memory Słowne", font=('Arial', 40), fg="#F9E816", bg="#79CBF7")
        self.title.pack(padx=WINDOW_WIDTH / 10, pady=WINDOW_HEIGHT / 5)

        # First row of buttons
        self.button_frame_first_row = tk.Frame(self.root, bg="#79CBF7")
        self.button_frame_first_row.columnconfigure(0, weight=1)
        self.button_frame_first_row.columnconfigure(1, weight=1)

        self.start_button = tk.Button(self.button_frame_first_row, text="Start",
                                      font=("Arial", 14), command=self.start_window)
        self.start_button.grid(row=0, column=0, padx=5)

        self.how_to_play_button = tk.Button(self.button_frame_first_row, text="How to play",
                                            font=("Arial", 14), command=self.how_to_play_window)
        self.how_to_play_button.grid(row=0, column=1, padx=5)

        self.button_frame_first_row.pack()

        # Second row of buttons
        self.button_frame_second_row = tk.Frame(self.root, bg="#79CBF7")

        self.button_frame_second_row.columnconfigure(0, weight=1)
        self.button_frame_second_row.columnconfigure(1, weight=1)

        self.score_button = tk.Button(self.button_frame_second_row, text="Scores", font=("Arial", 14),
                                      command=self.score)
        self.score_button.grid(row=0, column=0, padx=5, pady=10)

        self.quit_button = tk.Button(self.button_frame_second_row, text="Quit",
                                     font=("Arial", 14), command=self.root.destroy)
        self.quit_button.grid(row=0, column=1, padx=5, pady=10)

        self.button_frame_second_row.pack()

        self.root.mainloop()

    def how_to_play_window(self):
        self.root.destroy()
        HowToPlayWindow()

    def start_window(self):
        self.root.destroy()
        StartWindow()

    def score(self):
        self.root.destroy()
        ScoreWindow()


class HowToPlayWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title("Memory Słowne")
        self.root.configure(bg="#79CBF7")

        # Text message
        self.how_to_play_message = tk.Label(text=HOW_TO_PLAY_TEXT_PL, font=('Arial', 13), fg="#F9E816", bg="#79CBF7")
        self.how_to_play_message.pack(side=TOP, pady=100)

        # Return button
        self.return_button = tk.Button(self.root, text="Return", font=("Arial", 14),
                                       command=self.return_from_how_to_play_window)
        self.return_button.pack(side=RIGHT, padx=50)

        self.root.mainloop()

    def return_from_how_to_play_window(self):
        self.root.destroy()
        MenuWindowEng()


class StartWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title("Memory Słowne")
        self.root.configure(bg="#79CBF7")

        # Text message
        self.start_message = tk.Label(self.root, text="Choose a game mode:", font=('Arial', 18),
                                      fg="#F9E816", bg="#79CBF7")
        self.start_message.place(relx=0.38, rely=0.2)

        # Game mode buttons' frame
        self.buttons_frame = tk.Frame(self.root, bg="#79CBF7")

        self.buttons_frame.columnconfigure(0, weight=1)
        self.buttons_frame.columnconfigure(1, weight=1)

        # Game mode buttons
        self.quantity_button = tk.Button(self.buttons_frame, text="Quantity", font=('Arial', 14), command=self.quantity)
        self.quantity_button.grid(row=0, column=0, padx=10)

        self.time_button = tk.Button(self.buttons_frame, text="Time", font=('Arial', 14), command=self.time)
        self.time_button.grid(row=0, column=1)

        # Draw frame with buttons
        self.buttons_frame.place(relx=0.42, rely=0.3)

        # Return button
        self.return_form_start_button = tk.Button(self.root, text="Return", font=('Arial', 14),
                                                  command=self.return_from_start_window)
        self.return_form_start_button.pack(side=RIGHT, padx=50)

        self.root.mainloop()

    def return_from_start_window(self):
        self.root.destroy()
        MenuWindowEng()

    def quantity(self):
        self.root.destroy()
        LevelFromQuantity()

    def time(self):
        self.root.destroy()
        LevelFromTime()


class LevelFromQuantity:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title("Memory Słowne")
        self.root.configure(bg="#79CBF7")

        # Text message
        self.level_from_quantity_message = tk.Label(self.root, text="Choose a difficulty level:", font=('Arial', 18),
                                                    fg="#F9E816", bg="#79CBF7")
        self.level_from_quantity_message.place(relx=0.35, rely=0.2)

        # Game level buttons' frame
        self.buttons_frame = tk.Frame(self.root, bg="#79CBF7")

        self.buttons_frame.columnconfigure(0, weight=1)
        self.buttons_frame.columnconfigure(1, weight=1)
        self.buttons_frame.columnconfigure(2, weight=1)

        # Game level buttons
        self.easy_button = tk.Button(self.buttons_frame, text="Easy",
                                     font=('Arial', 14), command=self.easy_quantity)
        self.easy_button.grid(row=0, column=0, padx=10)

        self.medium_button = tk.Button(self.buttons_frame, text="Medium",
                                       font=('Arial', 14), command=self.medium_quantity)
        self.medium_button.grid(row=0, column=1)

        self.hard_button = tk.Button(self.buttons_frame, text="Hard", font=('Arial', 14), command=self.hard_quantity)
        self.hard_button.grid(row=0, column=2, padx=10)

        # Draw frame with buttons
        self.buttons_frame.place(relx=0.37, rely=0.3)

        # Return button
        self.return_form_level_button = tk.Button(self.root, text="Return", font=('Arial', 14),
                                                  command=self.return_from_level_window)
        self.return_form_level_button.pack(side=RIGHT, padx=50)

        self.root.mainloop()

    def return_from_level_window(self):
        self.root.destroy()
        StartWindow()

    def easy_quantity(self):
        self.root.destroy()
        EasyQuantityGameWindow()

    def medium_quantity(self):
        self.root.destroy()
        MediumQuantityGameWindow()

    def hard_quantity(self):
        self.root.destroy()
        HardQuantityGameWindow()


class LevelFromTime:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title("Memory Słowne")
        self.root.configure(bg="#79CBF7")

        # Text message
        self.level_from_quantity_message = tk.Label(self.root, text="Choose a difficulty level:", font=('Arial', 18),
                                                    fg="#F9E816", bg="#79CBF7")
        self.level_from_quantity_message.place(relx=0.35, rely=0.2)

        # Game level buttons' frame
        self.buttons_frame = tk.Frame(self.root, bg="#79CBF7")

        self.buttons_frame.columnconfigure(0, weight=1)
        self.buttons_frame.columnconfigure(1, weight=1)
        self.buttons_frame.columnconfigure(2, weight=1)

        # Game level buttons
        self.easy_button = tk.Button(self.buttons_frame, text="Easy", font=('Arial', 14), command=self.easy_time)
        self.easy_button.grid(row=0, column=0, padx=10)

        self.medium_button = tk.Button(self.buttons_frame, text="Medium", font=('Arial', 14), command=self.medium_time)
        self.medium_button.grid(row=0, column=1)

        self.hard_button = tk.Button(self.buttons_frame, text="Hard", font=('Arial', 14), command=self.hard_time)
        self.hard_button.grid(row=0, column=2, padx=10)

        # Draw frame with buttons
        self.buttons_frame.place(relx=0.37, rely=0.3)

        # Return button
        self.return_form_level_button = tk.Button(self.root, text="Return", font=('Arial', 14),
                                                  command=self.return_from_level_window)
        self.return_form_level_button.pack(side=RIGHT, padx=50)

        self.root.mainloop()

    def return_from_level_window(self):
        self.root.destroy()
        StartWindow()

    def easy_time(self):
        self.root.destroy()
        EasyTimeGameWindow()

    def medium_time(self):
        self.root.destroy()
        MediumTimeGameWindow()

    def hard_time(self):
        self.root.destroy()
        HardTimeGameWindow()


class EasyQuantityGameWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title("Memory Słowne")
        self.root.configure(bg="#79CBF7")

        # Filler
        self.filler = tk.Label(self.root, text=" ", bg="#79CBF7")
        self.filler.pack(pady=30)

        # Text
        self.str = tk.StringVar(self.root)
        self.str.set("Remember these words. You have 5 min.")
        self.text = tk.Label(self.root, textvariable=self.str, font=('Arial', 18), fg="#F9E816", bg="#79CBF7")
        self.text.pack(pady=40)

        # Input
        self.input = tk.Entry(self.root, width=30)
        self.input.pack()

        # Submit button
        self.button_pressed = tk.StringVar()
        self.button = tk.Button(self.root, text="Ok", font=('Arial', 14),
                                command=lambda: self.button_pressed.set("button pressed"))
        self.button.place(relx=0.7, rely=0.55)

        # Szymon's code implementation
        self.n = len(lines_easy)

        self.root.update()
        self.text.after(3000, self.str.set(f"{lines_easy}"))

        self.root.update()
        self.text.after(300000, self.str.set("Good luck"))

        self.root.update()
        self.text.after(1000, self.str.set("3"))

        self.root.update()
        self.text.after(1000, self.str.set("2"))

        self.root.update()
        self.text.after(1000, self.str.set("1"))

        self.root.update()
        self.text.after(1000, self.str.set("Enter your word:"))

        self.wynik = 0
        self.x = 0

        while self.x < self.n:
            self.button.wait_variable(self.button_pressed)
            self.slowo = str(self.input.get())
            self.m = len(sprawdzanie)
            for i in range(0, self.m):
                if self.slowo == sprawdzanie[i]:
                    self.root.update()
                    self.text.after(3000, self.str.set("Repeated word"))
                    sprawdzanie.clear()
                    self.root.update()
                    self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                    self.root.update()
                    self.text.after(3000, self.str.set("Enter your nick to save the score"))
                    self.button.wait_variable(self.button_pressed)
                    self.nick = self.input.get()
                    self.dodaj_wynik(self.nick, self.wynik)

                    self.root.update()
                    self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                    self.button.wait_variable(self.button_pressed)
                    if self.input.get() == "Yes" or self.input.get() == "yes":
                        self.root.destroy()
                    elif self.input.get() == "No" or self.input.get() == "no":
                        self.root.destroy()
                        EasyQuantityGameWindow()
            if self.slowo in lines_easy:
                self.wynik += 1
            else:
                self.root.update()
                self.text.after(1000, self.str.set("Wrong answer"))
                sprawdzanie.clear()
                self.root.update()
                self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                self.root.update()
                self.text.after(3000, self.str.set("Enter your nick to save the score"))
                self.button.wait_variable(self.button_pressed)
                self.nick = self.input.get()
                self.dodaj_wynik(self.nick, self.wynik)

                self.root.update()
                self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                self.button.wait_variable(self.button_pressed)
                if self.input.get() == "Yes" or self.input.get() == "yes":
                    self.root.destroy()
                elif self.input.get() == "No" or self.input.get() == "no":
                    self.root.destroy()
                    EasyQuantityGameWindow()
            sprawdzanie.append(self.slowo)
            self.root.update()
            self.text.after(1000, self.str.set("Correct answer"))
            self.x += 1
            if self.x < self.n:
                self.root.update()
                self.text.after(3000, self.str.set("Enter next answer"))
        sprawdzanie.clear()
        self.root.update()
        self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

        self.root.update()
        self.text.after(3000, self.str.set("Enter your nick to save the score"))
        self.button.wait_variable(self.button_pressed)
        self.nick = self.input.get()
        self.dodaj_wynik(self.nick, self.wynik)

        self.root.update()
        self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
        self.button.wait_variable(self.button_pressed)
        if self.input.get() == "Yes" or self.input.get() == "yes":
            self.root.destroy()
        elif self.input.get() == "No" or self.input.get() == "nie":
            self.root.destroy()
            EasyQuantityGameWindow()

        self.root.mainloop()

    def dodaj_wynik(self, nick, wynik):

        with open('wyniki.txt', 'r') as file:
            lines = file.readlines()

        min_wynik = float('inf')  # Inicjalizacja minimalnej wartości jako nieskończoność
        min_wynik_index = None  # Indeks najmniejszej wartości

        for i, line in enumerate(lines):
            match = re.search(r'(\d+) pkt', line)
            if match:
                stary_wynik = int(match.group(1))

                if stary_wynik < min_wynik:
                    min_wynik = stary_wynik
                    min_wynik_index = i

        if int(wynik) > min_wynik:  # Zamiana wyniku na liczbę całkowitą
            lines[min_wynik_index] = f"{nick} - {wynik} pkt\n"

            with open('wyniki.txt', 'w') as file:
                file.writelines(lines)
        else:
            pass


class MediumQuantityGameWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title("Memory Słowne")
        self.root.configure(bg="#79CBF7")

        # Filler
        self.filler = tk.Label(self.root, text=" ", bg="#79CBF7")
        self.filler.pack(pady=30)

        # Text
        self.str = tk.StringVar(self.root)
        self.str.set("Remember these words. You have 5 min.")
        self.text = tk.Label(self.root, textvariable=self.str, font=('Arial', 18), fg="#F9E816", bg="#79CBF7")
        self.text.pack(pady=40)

        # Input
        self.input = tk.Entry(self.root, width=30)
        self.input.pack()

        # Submit button
        self.button_pressed = tk.StringVar()
        self.button = tk.Button(self.root, text="Ok", font=('Arial', 14),
                                command=lambda: self.button_pressed.set("button pressed"))
        self.button.place(relx=0.7, rely=0.55)

        # Szymon's code implementation
        self.n = len(lines_medium)

        self.root.update()
        self.text.after(3000, self.str.set(f"{lines_medium}"))

        self.root.update()
        self.text.after(300000, self.str.set("Good luck"))

        self.root.update()
        self.text.after(1000, self.str.set("3"))

        self.root.update()
        self.text.after(1000, self.str.set("2"))

        self.root.update()
        self.text.after(1000, self.str.set("1"))

        self.root.update()
        self.text.after(1000, self.str.set("Enter your word:"))

        self.wynik = 0
        self.x = 0

        while self.x < self.n:
            self.button.wait_variable(self.button_pressed)
            self.slowo = str(self.input.get())
            self.m = len(sprawdzanie)
            for i in range(0, self.m):
                if self.slowo == sprawdzanie[i]:
                    self.root.update()
                    self.text.after(3000, self.str.set("Repeated word"))
                    sprawdzanie.clear()
                    self.root.update()
                    self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                    self.root.update()
                    self.text.after(3000, self.str.set("Enter your nick to save the score"))
                    self.button.wait_variable(self.button_pressed)
                    self.nick = self.input.get()
                    self.dodaj_wynik(self.nick, self.wynik)

                    self.root.update()
                    self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                    self.button.wait_variable(self.button_pressed)
                    if self.input.get() == "Yes" or self.input.get() == "yes":
                        self.root.destroy()
                    elif self.input.get() == "No" or self.input.get() == "nie":
                        self.root.destroy()
                        MediumQuantityGameWindow()
            if self.slowo in lines_medium:
                self.wynik += 1
            else:
                self.root.update()
                self.text.after(1000, self.str.set("Wrong answer"))
                sprawdzanie.clear()
                self.root.update()
                self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                self.root.update()
                self.text.after(3000, self.str.set("Enter your nick to save the score"))
                self.button.wait_variable(self.button_pressed)
                self.nick = self.input.get()
                self.dodaj_wynik(self.nick, self.wynik)

                self.root.update()
                self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                self.button.wait_variable(self.button_pressed)
                if self.input.get() == "Yes" or self.input.get() == "yes":
                    self.root.destroy()
                elif self.input.get() == "No" or self.input.get() == "nie":
                    self.root.destroy()
                    MediumQuantityGameWindow()
            sprawdzanie.append(self.slowo)
            self.root.update()
            self.text.after(1000, self.str.set("Correct answer"))
            self.x += 1
            if self.x < self.n:
                self.root.update()
                self.text.after(3000, self.str.set("Enter next answer"))
        sprawdzanie.clear()
        self.root.update()
        self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

        self.root.update()
        self.text.after(3000, self.str.set("Enter your nick to save the score"))
        self.button.wait_variable(self.button_pressed)
        self.nick = self.input.get()
        self.dodaj_wynik(self.nick, self.wynik)

        self.root.update()
        self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
        self.button.wait_variable(self.button_pressed)
        if self.input.get() == "Yes" or self.input.get() == "yes":
            self.root.destroy()
        elif self.input.get() == "No" or self.input.get() == "nie":
            self.root.destroy()
            MediumQuantityGameWindow()

        self.root.mainloop()

    def dodaj_wynik(self, nick, wynik):

        with open('wyniki.txt', 'r') as file:
            lines = file.readlines()

        min_wynik = float('inf')  # Inicjalizacja minimalnej wartości jako nieskończoność
        min_wynik_index = None  # Indeks najmniejszej wartości

        for i, line in enumerate(lines):
            match = re.search(r'(\d+) pkt', line)
            if match:
                stary_wynik = int(match.group(1))

                if stary_wynik < min_wynik:
                    min_wynik = stary_wynik
                    min_wynik_index = i

        if int(wynik) > min_wynik:  # Zamiana wyniku na liczbę całkowitą
            lines[min_wynik_index] = f"{nick} - {wynik} pkt\n"

            with open('wyniki.txt', 'w') as file:
                file.writelines(lines)
        else:
            pass


class HardQuantityGameWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title("Memory Słowne")
        self.root.configure(bg="#79CBF7")

        # Filler
        self.filler = tk.Label(self.root, text=" ", bg="#79CBF7")
        self.filler.pack(pady=30)

        # Text
        self.str = tk.StringVar(self.root)
        self.str.set("Remember these words. You have 5 min.")
        self.text = tk.Label(self.root, textvariable=self.str, font=('Arial', 18), fg="#F9E816", bg="#79CBF7")
        self.text.pack(pady=40)

        # Input
        self.input = tk.Entry(self.root, width=30)
        self.input.pack()

        # Submit button
        self.button_pressed = tk.StringVar()
        self.button = tk.Button(self.root, text="Ok", font=('Arial', 14),
                                command=lambda: self.button_pressed.set("button pressed"))
        self.button.place(relx=0.7, rely=0.65)

        # Szymon's code implementation
        self.n = len(lines_hard)

        self.root.update()
        self.text.after(3000, self.str.set(f"{lines_hard}"))

        self.root.update()
        self.text.after(300000, self.str.set("Good luck"))

        self.root.update()
        self.text.after(1000, self.str.set("3"))

        self.root.update()
        self.text.after(1000, self.str.set("2"))

        self.root.update()
        self.text.after(1000, self.str.set("1"))

        self.root.update()
        self.text.after(1000, self.str.set("Enter your word:"))

        self.wynik = 0
        self.x = 0

        while self.x < self.n:
            self.button.wait_variable(self.button_pressed)
            self.slowo = str(self.input.get())
            self.m = len(sprawdzanie)
            for i in range(0, self.m):
                if self.slowo == sprawdzanie[i]:
                    self.root.update()
                    self.text.after(3000, self.str.set("Repeated word"))
                    sprawdzanie.clear()
                    self.root.update()
                    self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                    self.root.update()
                    self.text.after(3000, self.str.set("Enter your nick to save the score"))
                    self.button.wait_variable(self.button_pressed)
                    self.nick = self.input.get()
                    self.dodaj_wynik(self.nick, self.wynik)

                    self.root.update()
                    self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                    self.button.wait_variable(self.button_pressed)
                    if self.input.get() == "Yes" or self.input.get() == "yes":
                        self.root.destroy()
                    elif self.input.get() == "No" or self.input.get() == "no":
                        self.root.destroy()
                        HardQuantityGameWindow()
            if self.slowo in lines_hard:
                self.wynik += 1
            else:
                self.root.update()
                self.text.after(1000, self.str.set("Wrong answer"))
                sprawdzanie.clear()
                self.root.update()
                self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                self.root.update()
                self.text.after(3000, self.str.set("Enter your nick to save the score"))
                self.button.wait_variable(self.button_pressed)
                self.nick = self.input.get()
                self.dodaj_wynik(self.nick, self.wynik)

                self.root.update()
                self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                self.button.wait_variable(self.button_pressed)
                if self.input.get() == "Yes" or self.input.get() == "yes":
                    self.root.destroy()
                elif self.input.get() == "No" or self.input.get() == "no":
                    self.root.destroy()
                    HardQuantityGameWindow()
            sprawdzanie.append(self.slowo)
            self.root.update()
            self.text.after(1000, self.str.set("Correct answer"))
            self.x += 1
            if self.x < self.n:
                self.root.update()
                self.text.after(3000, self.str.set("Enter next answer"))
        sprawdzanie.clear()
        self.root.update()
        self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

        self.root.update()
        self.text.after(3000, self.str.set("Enter your nick to save the score"))
        self.button.wait_variable(self.button_pressed)
        self.nick = self.input.get()
        self.dodaj_wynik(self.nick, self.wynik)

        self.root.update()
        self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
        self.button.wait_variable(self.button_pressed)
        if self.input.get() == "Yes" or self.input.get() == "yes":
            self.root.destroy()
        elif self.input.get() == "No" or self.input.get() == "no":
            self.root.destroy()
            HardQuantityGameWindow()

        self.root.mainloop()

    def dodaj_wynik(self, nick, wynik):

        with open('wyniki.txt', 'r') as file:
            lines = file.readlines()

        min_wynik = float('inf')  # Inicjalizacja minimalnej wartości jako nieskończoność
        min_wynik_index = None  # Indeks najmniejszej wartości

        for i, line in enumerate(lines):
            match = re.search(r'(\d+) pkt', line)
            if match:
                stary_wynik = int(match.group(1))

                if stary_wynik < min_wynik:
                    min_wynik = stary_wynik
                    min_wynik_index = i

        if int(wynik) > min_wynik:  # Zamiana wyniku na liczbę całkowitą
            lines[min_wynik_index] = f"{nick} - {wynik} pkt\n"

            with open('wyniki.txt', 'w') as file:
                file.writelines(lines)
        else:
            pass


class EasyTimeGameWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title("Memory Słowne")
        self.root.configure(bg="#79CBF7")

        # Filler
        self.filler = tk.Label(self.root, text=" ", bg="#79CBF7")
        self.filler.pack(pady=30)

        # Text
        self.str = tk.StringVar(self.root)
        self.str.set("Remember these words. You have 5 min.")
        self.text = tk.Label(self.root, textvariable=self.str, font=('Arial', 18), fg="#F9E816", bg="#79CBF7")
        self.text.pack(pady=40)

        # Input
        self.input = tk.Entry(self.root, width=30)
        self.input.pack()

        # Submit button
        self.button_pressed = tk.StringVar()
        self.button = tk.Button(self.root, text="Ok", font=('Arial', 14),
                                command=lambda: self.button_pressed.set("button pressed"))
        self.button.place(relx=0.7, rely=0.55)

        # Szymon's code implementation
        self.n = len(lines_easy)

        self.root.update()
        self.text.after(3000, self.str.set(f"{lines_easy}"))

        self.root.update()
        self.text.after(300000, self.str.set("Good luck"))

        self.root.update()
        self.text.after(1000, self.str.set("3"))

        self.root.update()
        self.text.after(1000, self.str.set("2"))

        self.root.update()
        self.text.after(1000, self.str.set("1"))

        self.root.update()
        self.text.after(1000, self.str.set("Enter your word:"))

        self.wynik = 0
        self.t1 = time.time()
        self.x = 0

        while self.x < self.n:
            self.t2 = time.time()
            if self.t2 - self.t1 >= 900:
                self.root.update()
                self.text.after(3000, self.str.set("Time has run out"))
                sprawdzanie.clear()
                self.root.update()
                self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                self.root.update()
                self.text.after(3000, self.str.set("Enter your nick to save the score"))
                self.button.wait_variable(self.button_pressed)
                self.nick = self.input.get()
                self.dodaj_wynik(self.nick, self.wynik)

                self.root.update()
                self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                self.button.wait_variable(self.button_pressed)
                if self.input.get() == "Yes" or self.input.get() == "yes":
                    self.root.destroy()
                elif self.input.get() == "No" or self.input.get() == "no":
                    self.root.destroy()
                    EasyTimeGameWindow()
            elif self.t2 - self.t1 <= 900:
                self.button.wait_variable(self.button_pressed)
                self.slowo = str(self.input.get())
                self.m = len(sprawdzanie)
                for i in range(0, self.m):
                    if self.slowo == sprawdzanie[i]:
                        self.root.update()
                        self.text.after(3000, self.str.set("Repeated word"))
                        sprawdzanie.clear()
                        self.root.update()
                        self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                        self.root.update()
                        self.text.after(3000, self.str.set("Enter your nick to save the score"))
                        self.button.wait_variable(self.button_pressed)
                        self.nick = self.input.get()
                        self.dodaj_wynik(self.nick, self.wynik)

                        self.root.update()
                        self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                        self.button.wait_variable(self.button_pressed)
                        if self.input.get() == "Yes" or self.input.get() == "yes":
                            self.root.destroy()
                        elif self.input.get() == "No" or self.input.get() == "nie":
                            self.root.destroy()
                            EasyTimeGameWindow()
                if self.slowo in lines_easy:
                    self.wynik += 1
                    sprawdzanie.append(self.slowo)
                    self.root.update()
                    self.text.after(1000, self.str.set("Correct answer"))
                else:
                    self.root.update()
                    self.text.after(1000, self.str.set("Wrong answer"))
                    sprawdzanie.clear()
                    self.root.update()
                    self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                    self.root.update()
                    self.text.after(3000, self.str.set("Enter your nick to save the score"))
                    self.button.wait_variable(self.button_pressed)
                    self.nick = self.input.get()
                    self.dodaj_wynik(self.nick, self.wynik)

                    self.root.update()
                    self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                    self.button.wait_variable(self.button_pressed)
                    if self.input.get() == "Yes" or self.input.get() == "yes":
                        self.root.destroy()
                    elif self.input.get() == "No" or self.input.get() == "no":
                        self.root.destroy()
                        EasyTimeGameWindow()

        self.root.mainloop()

    def dodaj_wynik(self, nick, wynik):

        with open('wyniki.txt', 'r') as file:
            lines = file.readlines()

        min_wynik = float('inf')  # Inicjalizacja minimalnej wartości jako nieskończoność
        min_wynik_index = None  # Indeks najmniejszej wartości

        for i, line in enumerate(lines):
            match = re.search(r'(\d+) pkt', line)
            if match:
                stary_wynik = int(match.group(1))

                if stary_wynik < min_wynik:
                    min_wynik = stary_wynik
                    min_wynik_index = i

        if int(wynik) > min_wynik:  # Zamiana wyniku na liczbę całkowitą
            lines[min_wynik_index] = f"{nick} - {wynik} pkt\n"

            with open('wyniki.txt', 'w') as file:
                file.writelines(lines)
        else:
            pass


class MediumTimeGameWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title("Memory Słowne")
        self.root.configure(bg="#79CBF7")

        # Filler
        self.filler = tk.Label(self.root, text=" ", bg="#79CBF7")
        self.filler.pack(pady=30)

        # Text
        self.str = tk.StringVar(self.root)
        self.str.set("Remember these words. You have 5 min.")
        self.text = tk.Label(self.root, textvariable=self.str, font=('Arial', 18), fg="#F9E816", bg="#79CBF7")
        self.text.pack(pady=40)

        # Input
        self.input = tk.Entry(self.root, width=30)
        self.input.pack()

        # Submit button
        self.button_pressed = tk.StringVar()
        self.button = tk.Button(self.root, text="Ok", font=('Arial', 14),
                                command=lambda: self.button_pressed.set("button pressed"))
        self.button.place(relx=0.7, rely=0.55)

        # Szymon's code implementation
        self.n = len(lines_medium)

        self.root.update()
        self.text.after(3000, self.str.set(f"{lines_medium}"))

        self.root.update()
        self.text.after(300000, self.str.set("Good luck"))

        self.root.update()
        self.text.after(1000, self.str.set("3"))

        self.root.update()
        self.text.after(1000, self.str.set("2"))

        self.root.update()
        self.text.after(1000, self.str.set("1"))

        self.root.update()
        self.text.after(1000, self.str.set("Enter your word:"))

        self.wynik = 0
        self.t1 = time.time()
        self.x = 0

        while self.x < self.n:
            self.t2 = time.time()
            if self.t2 - self.t1 >= 720:
                self.root.update()
                self.text.after(3000, self.str.set("Time has run out"))
                sprawdzanie.clear()
                self.root.update()
                self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                self.root.update()
                self.text.after(3000, self.str.set("Enter your nick to save the score"))
                self.button.wait_variable(self.button_pressed)
                self.nick = self.input.get()
                self.dodaj_wynik(self.nick, self.wynik)

                self.root.update()
                self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                self.button.wait_variable(self.button_pressed)
                if self.input.get() == "Yes" or self.input.get() == "yes":
                    self.root.destroy()
                elif self.input.get() == "No" or self.input.get() == "no":
                    self.root.destroy()
                    MediumTimeGameWindow()
            elif self.t2 - self.t1 <= 720:
                self.button.wait_variable(self.button_pressed)
                self.slowo = str(self.input.get())
                self.m = len(sprawdzanie)
                for i in range(0, self.m):
                    if self.slowo == sprawdzanie[i]:
                        self.root.update()
                        self.text.after(3000, self.str.set("Repeated word"))
                        sprawdzanie.clear()
                        self.root.update()
                        self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                        self.root.update()
                        self.text.after(3000, self.str.set("Enter your nick to save the score"))
                        self.button.wait_variable(self.button_pressed)
                        self.nick = self.input.get()
                        self.dodaj_wynik(self.nick, self.wynik)

                        self.root.update()
                        self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                        self.button.wait_variable(self.button_pressed)
                        if self.input.get() == "Yes" or self.input.get() == "yes":
                            self.root.destroy()
                        elif self.input.get() == "No" or self.input.get() == "no":
                            self.root.destroy()
                            MediumTimeGameWindow()
                if self.slowo in lines_medium:
                    self.wynik += 1
                    sprawdzanie.append(self.slowo)
                    self.root.update()
                    self.text.after(1000, self.str.set("Correct answer"))
                else:
                    self.root.update()
                    self.text.after(1000, self.str.set("Wrong answer"))
                    sprawdzanie.clear()
                    self.root.update()
                    self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                    self.root.update()
                    self.text.after(3000, self.str.set("Enter your nick to save the score"))
                    self.button.wait_variable(self.button_pressed)
                    self.nick = self.input.get()
                    self.dodaj_wynik(self.nick, self.wynik)

                    self.root.update()
                    self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                    self.button.wait_variable(self.button_pressed)
                    if self.input.get() == "Yes" or self.input.get() == "yes":
                        self.root.destroy()
                    elif self.input.get() == "No" or self.input.get() == "no":
                        self.root.destroy()
                        MediumTimeGameWindow()

        self.root.mainloop()

    def dodaj_wynik(self, nick, wynik):

        with open('wyniki.txt', 'r') as file:
            lines = file.readlines()

        min_wynik = float('inf')  # Inicjalizacja minimalnej wartości jako nieskończoność
        min_wynik_index = None  # Indeks najmniejszej wartości

        for i, line in enumerate(lines):
            match = re.search(r'(\d+) pkt', line)
            if match:
                stary_wynik = int(match.group(1))

                if stary_wynik < min_wynik:
                    min_wynik = stary_wynik
                    min_wynik_index = i

        if int(wynik) > min_wynik:  # Zamiana wyniku na liczbę całkowitą
            lines[min_wynik_index] = f"{nick} - {wynik} pkt\n"

            with open('wyniki.txt', 'w') as file:
                file.writelines(lines)
        else:
            pass


class HardTimeGameWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title("Memory Słowne")
        self.root.configure(bg="#79CBF7")

        # Filler
        self.filler = tk.Label(self.root, text=" ", bg="#79CBF7")
        self.filler.pack(pady=30)

        # Text
        self.str = tk.StringVar(self.root)
        self.str.set("Remember these words. You have 5 min.")
        self.text = tk.Label(self.root, textvariable=self.str, font=('Arial', 18), fg="#F9E816", bg="#79CBF7")
        self.text.pack(pady=40)

        # Input
        self.input = tk.Entry(self.root, width=30)
        self.input.pack()

        # Submit button
        self.button_pressed = tk.StringVar()
        self.button = tk.Button(self.root, text="Ok", font=('Arial', 14),
                                command=lambda: self.button_pressed.set("button pressed"))
        self.button.place(relx=0.7, rely=0.65)

        # Szymon's code implementation
        self.n = len(lines_hard)

        self.root.update()
        self.text.after(3000, self.str.set(f"{lines_hard}"))

        self.root.update()
        self.text.after(300000, self.str.set("Good luck"))

        self.root.update()
        self.text.after(1000, self.str.set("3"))

        self.root.update()
        self.text.after(1000, self.str.set("2"))

        self.root.update()
        self.text.after(1000, self.str.set("1"))

        self.root.update()
        self.text.after(1000, self.str.set("Enter your word:"))

        self.wynik = 0
        self.t1 = time.time()
        self.x = 0

        while self.x < self.n:
            self.t2 = time.time()
            if self.t2 - self.t1 >= 600:
                self.root.update()
                self.text.after(3000, self.str.set("Time has run out"))
                sprawdzanie.clear()
                self.root.update()
                self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                self.root.update()
                self.text.after(3000, self.str.set("Enter your nick to save the score"))
                self.button.wait_variable(self.button_pressed)
                self.nick = self.input.get()
                self.dodaj_wynik(self.nick, self.wynik)

                self.root.update()
                self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                self.button.wait_variable(self.button_pressed)
                if self.input.get() == "Yes" or self.input.get() == "yes":
                    self.root.destroy()
                elif self.input.get() == "No" or self.input.get() == "no":
                    self.root.destroy()
                    HardTimeGameWindow()
            elif self.t2 - self.t1 <= 600:
                self.button.wait_variable(self.button_pressed)
                self.slowo = str(self.input.get())
                self.m = len(sprawdzanie)
                for i in range(0, self.m):
                    if self.slowo == sprawdzanie[i]:
                        self.root.update()
                        self.text.after(3000, self.str.set("Repeated word"))
                        sprawdzanie.clear()
                        self.root.update()
                        self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                        self.root.update()
                        self.text.after(3000, self.str.set("Enter your nick to save the score"))
                        self.button.wait_variable(self.button_pressed)
                        self.nick = self.input.get()
                        self.dodaj_wynik(self.nick, self.wynik)

                        self.root.update()
                        self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                        self.button.wait_variable(self.button_pressed)
                        if self.input.get() == "Yes" or self.input.get() == "yes":
                            self.root.destroy()
                        elif self.input.get() == "No" or self.input.get() == "no":
                            self.root.destroy()
                            HardTimeGameWindow()
                if self.slowo in lines_hard:
                    self.wynik += 1
                    sprawdzanie.append(self.slowo)
                    self.root.update()
                    self.text.after(1000, self.str.set("Correct answer"))
                else:
                    self.root.update()
                    self.text.after(1000, self.str.set("Wrong answer"))
                    sprawdzanie.clear()
                    self.root.update()
                    self.text.after(3000, self.str.set(f"Final score: {self.wynik} points"))

                    self.root.update()
                    self.text.after(3000, self.str.set("Enter your nick to save the score"))
                    self.button.wait_variable(self.button_pressed)
                    self.nick = self.input.get()
                    self.dodaj_wynik(self.nick, self.wynik)

                    self.root.update()
                    self.text.after(3000, self.str.set("Do you want to quit the game? Answer Yes/No"))
                    self.button.wait_variable(self.button_pressed)
                    if self.input.get() == "Yes" or self.input.get() == "yes":
                        self.root.destroy()
                    elif self.input.get() == "No" or self.input.get() == "no":
                        self.root.destroy()
                        HardTimeGameWindow()

        self.root.mainloop()

    def dodaj_wynik(self, nick, wynik):

        with open('wyniki.txt', 'r') as file:
            lines = file.readlines()

        min_wynik = float('inf')  # Inicjalizacja minimalnej wartości jako nieskończoność
        min_wynik_index = None  # Indeks najmniejszej wartości

        for i, line in enumerate(lines):
            match = re.search(r'(\d+) pkt', line)
            if match:
                stary_wynik = int(match.group(1))

                if stary_wynik < min_wynik:
                    min_wynik = stary_wynik
                    min_wynik_index = i

        if int(wynik) > min_wynik:  # Zamiana wyniku na liczbę całkowitą
            lines[min_wynik_index] = f"{nick} - {wynik} pkt\n"

            with open('wyniki.txt', 'w') as file:
                file.writelines(lines)
        else:
            pass


class ScoreWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.title("Memory Słowne")
        self.root.configure(bg="#79CBF7")

        # Text message
        self.label = tk.Label(self.root, text="Scores:", font=('Arial', 18), fg="#F9E816", bg="#79CBF7")
        self.label.place(relx=0.43, rely=0.2)

        # Score table
        self.frame = tk.Frame(self.root, bg="#79CBF7")

        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)

        # Set each score
        with open("wyniki.txt", "r") as f:
            line1 = f.readline()
            line2 = f.readline()
            line3 = f.readline()

        self.first_variable = tk.StringVar()
        self.first_variable.set(f"{line1}")
        self.first_score = tk.Label(self.frame, textvariable=self.first_variable, font=('Arial', 14),
                                    fg="#F9E816", bg="#79CBF7")
        self.first_score.grid(row=0, column=0, padx=10)

        self.second_variable = tk.StringVar()
        self.second_variable.set(f"{line2}")
        self.second_score = tk.Label(self.frame, textvariable=self.second_variable, font=('Arial', 14),
                                     fg="#F9E816", bg="#79CBF7")
        self.second_score.grid(row=1, column=0, padx=10)

        self.third_variable = tk.StringVar()
        self.third_variable.set(f"{line3}")
        self.third_score = tk.Label(self.frame, textvariable=self.third_variable, font=('Arial', 14),
                                    fg="#F9E816", bg="#79CBF7")
        self.third_score.grid(row=2, column=0, padx=10)

        # Place the table
        self.frame.place(relx=0.4, rely=0.3)

        # Return button
        self.return_form_level_button = tk.Button(self.root, text="Return", font=('Arial', 14),
                                                  command=self.return_from_score_window)
        self.return_form_level_button.pack(side=RIGHT, padx=50)

        f.close()

        self.root.mainloop()

    def return_from_score_window(self):
        self.root.destroy()
        MenuWindowEng()
