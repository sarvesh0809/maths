import random
from tkinter import *

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def submt(var1):
    if var1.get() == str(resultPLUS()):
        correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.3, rely=0.2)
    else:
        wrong = Label(app, text="Wrong!!!", fg="red", font=("Courier", 16))
        wrong.place(relx=0.3, rely=0.2)


def Next():
    Next.num1update = random.choice(num)
    Next.num2update = random.choice(num)
    newQ = Label(
        app, text=f"{Next.num1update}+{Next.num2update}", font=("Courier", 16)
    )
    newQ.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)


def resultPLUS():
    Next
    return Next.num1update + Next.num2update


app = Tk()
app.title("Math For Kids")
# canvas = Canvas(app, width=240, height=300)
# canvas.pack()
app.geometry("240x300")
app.resizable(False, False)
start = Button(app, text="Start", command=Next)
start.place(relx=0.45, rely=0.2)

solving = Entry(app)
solving.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)
submit = Button(app, text="Submit", command=lambda: submt(solving))
submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)
Next = Button(app, text="Next", command=Next)
Next.place(relx=0.39, rely=0.9)
app.mainloop()
