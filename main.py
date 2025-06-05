import tkinter as tk 

from gui import gui

def main():
    input = tk.Tk()
    input.title("Acefinfo's calculator")
    input.geometry("330x430")
    input.configure(bg="#2b2b2b")
    gui(input)
    input.mainloop()

if __name__ == "__main__":
    main()
