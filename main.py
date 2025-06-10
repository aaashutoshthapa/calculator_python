import tkinter as tk 

from gui import gui 

def main():
    
    input = tk.Tk()
    input.title("Acefinfo's calculator")
    input.geometry("390x340")
    input.configure(bg="#2b2b2b")
    gui(input)
    input.mainloop()

if __name__ == "__main__":
    main()
