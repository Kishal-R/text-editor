import tkinter as tk
from tkinter import filedialog, messagebox
import os
import platform

def new_file():
    if text_area.get("1.0", tk.END).strip():
        if messagebox.askyesno("Save File", "Do you want to save the current file?"):
            save_file()
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file_path:
        text_area.delete(1.0, tk.END)
        with open(file_path, "r") as file:
            text_area.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        messagebox.showinfo("File Saved", "File saved successfully!")

def exit_editor():
    if text_area.get("1.0", tk.END).strip():
        if messagebox.askyesno("Exit", "Do you want to save the current file before exiting?"):
            save_file()
    root.destroy()

def open_terminal():
    current_os = platform.system()
    if current_os == "Linux" or current_os == "Darwin":  # Linux or macOS
        os.system("gnome-terminal &" if current_os == "Linux" else "open -a Terminal.app")
    elif current_os == "Windows":
        os.system("start cmd")
    else:
        messagebox.showerror("Unsupported OS", "This feature is not supported on your operating system.")

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

# Text area with black background and white text
text_area = tk.Text(root, wrap='word', bg='black', fg='white', insertbackground='white')
text_area.pack(expand=1, fill='both')

# Menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

# Adding Tools menu
tools_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Open Terminal", command=open_terminal)

root.mainloop()
