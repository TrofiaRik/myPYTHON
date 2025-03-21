from ttkthemes import ThemedStyle
from tkinter import Tk, Button, Label

def apply_next_theme():
    global current_theme_index
    current_theme_index = (current_theme_index + 1) % len(themes)
    style.set_theme(themes[current_theme_index])
    theme_label.config(text=f"Current theme: {themes[current_theme_index]}")

root = Tk()
style = ThemedStyle(root)

themes = style.theme_names()
current_theme_index = 0
style.set_theme(themes[current_theme_index])

theme_label = Label(root, text=f"Current theme: {themes[current_theme_index]}")
theme_label.pack(pady=10)

Button(root, text="Next Theme", command=apply_next_theme).pack(pady=10)

root.mainloop()
