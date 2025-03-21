from ttkthemes import ThemedStyle
from tkinter import Tk, ttk, Label

def change_theme(event=None):
    selected_theme = theme_selector.get()
    style.set_theme(selected_theme)
    theme_label.config(text=f"Current theme: {selected_theme}")

# Initialize main Tkinter window
root = Tk()
root.title("ttkthemes Explorer")

# Add ThemedStyle
style = ThemedStyle(root)

# Get available themes
themes = style.theme_names()

# Dropdown (combobox) to select themes
theme_selector = ttk.Combobox(root, values=themes, state="readonly")
theme_selector.set(themes[0])  # Default theme
theme_selector.pack(pady=10)
theme_selector.bind("<<ComboboxSelected>>", change_theme)

# Label to show the current theme
theme_label = Label(root, text=f"Current theme: {themes[0]}")
theme_label.pack(pady=10)

# Button to apply the selected theme
ttk.Button(root, text="Apply Theme", command=change_theme).pack(pady=10)

# Example widget for visual feedback
ttk.Label(root, text="This is a sample widget").pack(pady=20)
ttk.Button(root, text="Sample Button").pack(pady=10)

root.mainloop()
