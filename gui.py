import tkinter as tk 

from logic import expression_evaluation as logic

def gui(input):
    """
    This function creates a simple graphical user interface (GUI) for a calculator application using Tkinter.

    The calculator can perform basic arithmetic operations: addition, subtraction, multiplication, division, and clear the current input.

    Parameters:
    input (tk.Tk or tk.Toplevel): The parent Tkinter window or frame in which the calculator will be displayed.

    Functionality:
    - The user can click buttons to input numbers and arithmetic operations.
    - The "=" button evaluates the expression using the `expression_evaluation` function from the `logic` module.
    - The "C" button clears the current input.
    - The calculator supports the operations: addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).

    Buttons:
    - The number buttons (`0-9`) append the corresponding digit to the input.
    - The operation buttons (`+`, `-`, `*`, `/`) append the respective operator to the input.
    - The "=" button evaluates the expression and shows the result.
    - The "C" button clears the input.
    """
    def click(event):
        """
        Handles the button clicks within the calculator GUI.

        Based on the button clicked:
        - If the "=" button is pressed, the current expression is evaluated and the result is displayed.
        - If the "C" button is pressed, the entry field is cleared.
        - Otherwise, the button's text (i.e., the digit or operator) is appended to the current input.

        Parameters:
        event (tk.Event): The event object generated when a button is clicked.
        """

        #Retrives the text of the clicked button and gets the text field from the entry feild
        button_text = event.widget.cget("text")
        current = entry.get()  

        # Handle button clicks: evaluate the expression for "=" button, clear input for "C", or append button text to input otherwise.
        if button_text == "=":
            result = logic(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        elif button_text == "C":
            entry.delete(0, tk.END)
        else:
            entry.insert(tk.END, button_text)
    
    # Create and configure the input entry field for the calculator with custom font, border, and layout settings.
    global entry
    entry = tk.Entry(input, font= "Helvetica 24", borderwidth=5, relief=tk.RIDGE, justify="right", bg="#ffffff")
    entry.grid(row=0, column=0, columnspan=4, pady=20, padx=10, ipady=10, sticky="nsew")

    # Define the list of button labels (numbers, operators, and special buttons) for the calculator.
    buttons =[
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        'C', '0', '=', '+'
    ]

    # Initialize the starting row and column for placing buttons in the grid layout.
    row = 1
    column = 0

    # Create and place buttons in a grid layout, configure their appearance, and bind the click event for each button.
    for button in buttons:
        btn = tk.Button(input, text=button, font="Helvetica 18", width=5, height=2, bg="#000000", fg="white", activebackground="#666")

        if button == "=":
            btn.config(bg="#00ff1e")
        elif button == "C":
            btn.config(bg="#00ff1e")

        btn.grid(row=row, column=column, padx=5, pady=5)
        btn.bind("<Button-1>", click)

        column += 1
        if column == 4:
            row += 1
            column = 0
