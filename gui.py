import tkinter as tk 

from logic import expression_evaluation as logic

def gui(input):
    def click(event):
        button_text = event.widget.cget("text")
        current = entry.get()

        if button_text == "=":
            result = logic(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        elif button_text == "C":
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, button_text)
    
    global entry
    entry = tk.Entry(input, font= "Helvetica 24", borderwidth=5, relief=tk.RIDGE, justify="right", bg="#e6e6e6")
    entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10, ipady=10, sticky="nsew")

    buttons =[
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        'C', '0', '=', '+'
    ]

    row = 1
    column = 0

    for button in buttons:
        btn = tk.Button(input,font= "Helvetica 18", width=5, height=2, bg="#4d4d4d", fg="white", activebackground="#666")

        if button == "=":
            btn.config(bg ="#00cc66")
        elif button == "C":
            btn.config(bg = "#00cc66")
        
        btn.grid(row=row, column=column, padx=5, pady=5)
        btn.bind("<Button-1>", click)

        column += 1
        if column == 4:
            row += 1
            column = 0




