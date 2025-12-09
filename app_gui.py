#!/usr/bin/env python
'''
    GUI application for the command line tool.
    Can open multiple image files with a simple FM prompt.
'''

import subprocess
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("660x300")

        self.create_widgets()

    def create_widgets(self):
        input_label = tk.Label(self, text="Selecionar arquivo fonte(s)... (.png, .jpg, etc.):")
        input_box = tk.Entry(self, width=80, state="disabled")
        input_btn = tk.Button(self, text="Pesquisar...", height=1)

        input_label.grid(column=0, row=0)
        input_box.grid(column=0, row=1)
        input_btn.grid(column=1, row=1)


app = App()
app.mainloop()