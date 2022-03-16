from tkinter import*

expression = ""

def on_click(number):
    global expression
    expression = expression + str(number)
    input_text.set(expression)

def button_clear():
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

def calculator():

    window = Tk()
    window.geometry("500x500")
    window.resizable(0, 0)
    window.title("Calculator")

    input_text = StringVar()

    # INPUT FRAMEN LUONTI
    input_frame = Frame(window, width = 500, height = 75)
    input_frame.pack(side = TOP)

    # INPUT TEKSTIKENTÄN LUONTI
    input_field = Entry(input_frame, width = 50, justify = RIGHT, textvariable = input_text)
    input_field.grid(row   = 0, column = 0)
    input_field.pack(ipady = 10)

    # BUTTONS FRAME
    buttons_frame = Frame(window, width = 500, height = 425)
    buttons_frame.pack()


    # BUTTONS
    zero = Button(buttons_frame, text = "0", width = 22, height = 5, command = lambda: on_click(0))
    dot = Button(buttons_frame, text = ".", width = 10, height = 5, command = lambda: on_click("."))
    equals = Button(buttons_frame, text = "=", width = 10, height = 5, command = lambda: button_equal())

    one = Button(buttons_frame, text = "1", width = 10, height = 5, command = lambda: on_click(1))
    two = Button(buttons_frame, text = "2", width = 10, height = 5, command = lambda: on_click(2))
    three = Button(buttons_frame, text = "3", width = 10, height = 5, command = lambda: on_click(3))
    plus = Button(buttons_frame, text = "+", width = 10, height = 5, command = lambda: on_click("+"))

    four = Button(buttons_frame, text = "4", width = 10, height = 5, command = lambda: on_click(4))
    five = Button(buttons_frame, text = "5", width = 10, height = 5, command = lambda: on_click(5))
    six = Button(buttons_frame, text = "6", width = 10, height = 5, command = lambda: on_click(6))
    minus = Button(buttons_frame, text = "-", width = 10, height = 5, command = lambda: on_click("-"))

    seven = Button(buttons_frame, text = "7", width = 10, height = 5, command = lambda: on_click(7))
    eight = Button(buttons_frame, text = "8", width = 10, height = 5, command = lambda: on_click(8))
    nine = Button(buttons_frame, text = "9", width = 10, height = 5, command = lambda: on_click(9))
    div = Button(buttons_frame, text = "/", width = 10, height = 5, command = lambda: on_click("/"))

    clear = Button(buttons_frame, text = "Clear", width = 32, height = 5 , command = lambda: button_clear())
    multipy = Button(buttons_frame, text = "*", width = 10, height = 5, command = lambda: on_click("*"))

    # BUTTONS LAYOUT
    zero.grid(row = 5, column = 0, columnspan = 2)
    dot.grid(row = 5, column = 2)
    equals.grid(row = 5, column = 3)

    one.grid(row = 4, column = 0)
    two.grid(row = 4, column = 1)
    three.grid(row = 4, column = 2)
    plus.grid(row = 4, column = 3)

    four.grid(row = 3, column = 0)
    five.grid(row = 3, column = 1)
    six.grid(row = 3, column = 2)
    minus.grid(row = 3, column = 3)

    seven.grid(row = 2, column = 0)
    eight.grid(row = 2, column = 1)
    nine.grid(row = 2, column = 2)
    div.grid(row = 2, column = 3)

    multipy.grid(row = 1, column = 3)
    clear.grid(row = 1, column = 0, columnspan = 3)


    window.mainloop()


def main():
    calculator()

if __name__ == "__main__":
    main()

    
