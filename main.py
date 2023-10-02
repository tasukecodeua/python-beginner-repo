import tkinter as tk
from tkinter import scrolledtext
from random import choice

last_computer_letter = None

def check_city():
    global last_computer_letter

    city = entery.get().title()
    if not city:
        response = f"City didn't entered."
    elif city in used_cities:
        response = f"City {city} used."
    elif city not in cities:
        response = f"City {city} unknown."
    elif last_computer_letter and city[0] != last_computer_letter:
        response = f"City must begin with a letter {last_computer_letter}"
    else: 
        used_cities.append(city)

        last_letter = get_last_letter(city)

        computer_city = get_city_by_letter(last_letter)
        if not computer_city:
            response = f"You won! I don't know any cities starting with the letter {last_letter}."
        else:
            used_cities.append(computer_city)
            last_computer_letter = get_last_letter(computer_city)
            response = f"My city: {computer_city}."

    game_log.config(state = tk.NORMAL)
    game_log.insert(tk.END, f"You: {city}.\n")
    game_log.insert(tk.END, f"Game: {response}\n")
    game_log.yview(tk.END)
    game_log.config(state=tk.DISABLED)
    notification.config(text=response)
    entery.delete(0, tk.END)

def get_last_letter(city):
    last_letter = city[-1].upper()
    if last_letter in ["Ь", "Й", "И"]:
        last_letter = city[-2].upper()
    return last_letter

def get_city_by_letter(letter):
    avaible_cities = []
    for city in cities:
        if city[0].upper() == letter and city not in used_cities:
            avaible_cities.append(city)
    if avaible_cities:
        return choice(avaible_cities)
    return None

def surrender():
    game_log.config(state = tk.NORMAL)
    game_log.insert(tk.END, f"Who would doubt it!\n")
    game_log.yview(tk.END)
    game_log.config(state=tk.DISABLED)
    notification.config(text="The computer is better than the human again!")
    entery.delete(0, tk.END)

def load_cities_from_file(filename):
    cities = []
    with open(filename, "r", encoding="utf-8") as fd:
        for line in fd:
            cities.append(line.strip())
    return cities

cities = load_cities_from_file('cities.txt')
used_cities = []

root = tk.Tk()
root.title('Cities')
root.geometry("800x400")

left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.BOTH)

label = tk.Label(left_frame, text="Input city name")
label.pack(padx=10, pady=10)

entery = tk.Entry(left_frame, width=35)
entery.pack(padx=10, pady=10)

button_frame = tk.Frame(left_frame)
button_frame.pack(padx=10)

button = tk.Button(button_frame, text="Send", command=check_city)
button.pack(padx=10, side=tk.LEFT)

button_end = tk.Button(button_frame, text="I lost", command=surrender)
button_end.pack(padx=10, side=tk.LEFT)

notification = tk.Label(left_frame, text="")
notification.pack(padx=10, pady=10)

game_log = scrolledtext.ScrolledText(root, width = 50, height = 15, wrap = tk.WORD)
game_log.pack(padx=10, pady=10, side=tk.RIGHT)
game_log.config(state=tk.DISABLED)

root.mainloop()