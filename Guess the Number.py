import tkinter as tk
import random

number = random.randint(0, 9)


def onclick1():
    print('You selected one')
    right_number1 = 1
    if right_number1 == number:
        print('Correct!')
    else:
        print('incorrect')


def onclick2():
    print('You selected two')
    right_number2 = 2
    if right_number2 == number:
        print('Correct!')
    else:
        print('incorrect')


def onclick3():
    print('You selected three')
    right_number3 = 3
    if right_number3 == number:
        print('Correct!')
    else:
        print('incorrect')


def onclick4():
    print('You selected four')
    right_number4 = 4
    if right_number4 == number:
        print('Correct!')
    else:
        print('incorrect')


def onclick5():
    print('You selected five')
    right_number5 = 5
    if right_number5 == number:
        print('Correct!')
    else:
        print('incorrect')


def onclick6():
    print('You selected six')
    right_number6 = 6
    if right_number6 == number:
        print('Correct!')
    else:
        print('incorrect')


def onclick7():
    print('You selected seven')
    right_number7 = 7
    if right_number7 == number:
        print('Correct!')
    else:
        print('incorrect')


def onclick8():
    print('You selected eight')
    right_number8 = 8
    if right_number8 == number:
        print('Correct!')
    else:
        print('incorrect')


def onclick9():
    print('You selected nine')
    right_number9 = 9
    if right_number9 == number:
        print('Correct!')
    else:
        print('incorrect')


def onclick0():
    print('You selected zero')
    right_number0 = 0
    if right_number0 == number:
        print('Correct!')
    else:
        print('incorrect')


root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=600, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='grey')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

zero = tk.Button(root, text='Zero', padx=10, pady=5, fg='orange', bg='#263D42', command=onclick0)
zero.pack(side=tk.LEFT)

one = tk.Button(root, text='One', padx=10, pady=5, fg='red', bg='#263D42', command=onclick1)
one.pack(side=tk.LEFT)

two = tk.Button(root, text='Two', padx=10, pady=5, fg='white', bg='#263D42', command=onclick2)
two.pack(side=tk.LEFT)

three = tk.Button(root, text='Three', padx=10, pady=5, fg='yellow', bg='#263D42', command=onclick3)
three.pack(side=tk.LEFT)

four = tk.Button(root, text='Four', padx=10, pady=5, fg='magenta', bg='#263D42', command=onclick4)
four.pack(side=tk.LEFT)

five = tk.Button(root, text='Five', padx=10, pady=5, fg='turquoise', bg='#263D42', command=onclick5)
five.pack(side=tk.LEFT)
six = tk.Button(root, text='Six', padx=10, pady=5, fg='tan', bg='#263D42', command=onclick6)
six.pack(side=tk.LEFT)

seven = tk.Button(root, text='Seven', padx=10, pady=5, fg='gold', bg='#263D42', command=onclick7)
seven.pack(side=tk.LEFT)

eight = tk.Button(root, text='Eight', padx=10, pady=5, fg='blue', bg='#263D42', command=onclick8)
eight.pack(side=tk.LEFT)

nine = tk.Button(root, text='Nine', padx=10, pady=5, fg='green', bg='#263D42', command=onclick9)
nine.pack(side=tk.LEFT)

how_to_play = tk.Label(root, text="How to Play")
how_to_play.place(x=273, y=100)

rules = tk.Label(root, text='''
You have to try to guess the mystery number in the least amount of tries. 
To guess, you have to click the number buttons on the bottom. If you want 
to quit, you can click the x button on the top right corner.''')
rules.place(x=97, y=150)

root.mainloop()
