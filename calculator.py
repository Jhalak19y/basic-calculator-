import tkinter as tk
import math

class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Basic Calculator")
        self.expression = ""
        self.text_input = tk.StringVar()

        # Create display
        self.display = tk.Entry(window, textvariable=self.text_input, font=('arial', 20, 'bold'), bd=30, insertwidth=4, width=14, justify='right')
        self.display.grid(columnspan=4)

        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
            ('sqrt', 5, 0), ('^', 5, 1), ('sin', 5, 2), ('cos', 5, 3),
            ('tan', 6, 0)
        ]

        for (text, row, col) in button_texts:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.window, text=text, padx=20, pady=20, font=('arial', 18, 'bold'),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=col)

    def button_click(self, text):
        if text == 'C':
            self.expression = ""
        elif text == '=':
            self.calculate()
        elif text == 'sqrt':
            self.expression += "**0.5"
        elif text == '^':
            self.expression += "**"
        elif text in ('sin', 'cos', 'tan'):
            self.expression = f"math.{text}(math.radians({self.expression}))"
        else:
            self.expression += str(text)
        self.text_input.set(self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.text_input.set(result)
            self.expression = str(result)
        except Exception as e:
            self.text_input.set("Error")
            self.expression = ""

if __name__ == "__main__":
    window = tk.Tk()
    calculator = Calculator(window)
    window.mainloop()
