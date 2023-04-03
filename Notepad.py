import tkinter as tk
from tkinter import filedialog

#lmr_lumiere
#code pour simuler un notepad valide

class Notepad:
    def __init__(self, master):
        self.master = master
        self.text = tk.Text(self.master)
        self.text.pack(fill='both', expand=True)

        # creation du menu bar
        self.menu_bar = tk.Menu(self.master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.master.config(menu=self.menu_bar)

        self.filename = None

    def new_file(self):
        self.text.delete(1.0, tk.END)
        self.filename = None

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            self.text.delete(1.0, tk.END)
            with open(self.filename, "r") as file:
                self.text.insert(1.0, file.read())

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text.get(1.0, tk.END))

root = tk.Tk()
root.title("Notepad")
notepad = Notepad(root)
root.mainloop()
