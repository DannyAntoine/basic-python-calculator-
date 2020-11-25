from tkinter import *


# creating the function of the equal button
# the btn_press function continuously updates the entry field whenever you enter a number


def btn_press(item):
    global expression
    expression = expression + str(item)
    textvar.set(expression)




def btnclear():
    global expression
    expression = ""
    textvar.set("")




def btnequal():
    global expression
    result = str(eval(expression))
    textvar.set(result)
    expression = ""


expression = ""







# creates window object
window = Tk()
#displays message at top of window
window.title('Basic Calculator ')
#Gives size dimensions to window
window.geometry('400x300')
window.resizable(0,0)


# 'StringVar()' :It is used to get the instance of input field

textvar = StringVar()

#

input_frame = Frame(window, width=290, height=80, bd=0, highlightbackground="black", highlightcolor="black", ).place(x=0,y=0)

entry_field = Entry(input_frame, font=('arial', 20, 'bold'),textvariable= textvar ).place(x =0 , y = 0, width=290,height=80)

btn0 = Button(window, text='0',width=20, height=2, command=lambda: btn_press(0)).place(x=100,   y=84)
btn1 = Button(window, text='1',width=10, height=2, command=lambda: btn_press(1)).place(x=0,   y=259)
btn2 = Button(window, text='2',width=10, height=2, command=lambda: btn_press(2)).place(x=100, y=259)
btn3 = Button(window, text='3',width=10, height=2, command=lambda: btn_press(3)).place(x=200, y=259)
btn4 = Button(window, text='4',width=10, height=2, command=lambda: btn_press(4)).place(x=0,   y=200)
btn5 = Button(window, text='5',width=10, height=2, command=lambda: btn_press(5)).place(x=100, y=200)
btn6 = Button(window, text='6',width=10, height=2, command=lambda: btn_press(6)).place(x=200, y=200)
btn7 = Button(window, text='7',width=10, height=2, command=lambda: btn_press(7)).place(x=0,   y=142)
btn8 = Button(window, text='8',width=10, height=2, command=lambda: btn_press(8)).place(x=100, y=142)
btn9 = Button(window, text='9',width=10, height=2, command=lambda: btn_press(9)).place(x=200, y=142)

#operation buttons
btnenter = Button(window, text='=',width=10, height=2,bg='Purple', command = lambda: btnequal()).place(x=290, y=28)
btnclr = Button(window, text='Clear',width=10, height=2, bg='orange',command = lambda: btnclear()).place(x=0, y=84)
btnplus = Button(window, text='+',width=10, height=2, bg='yellow',  command=lambda: btn_press("+")).place(x=290, y=84)
btnminus = Button(window, text='-',width=10, height=2, bg='green', command=lambda: btn_press("-")).place(x=290, y=142)
btndivide = Button(window, text='/',width=10, height=2, bg='red', command=lambda: btn_press("/")).place(x=290, y=200)
btnmultiply = Button(window, text='*',width=10, height=2, bg='blue', command=lambda: btn_press("*")).place(x=290, y=259)

#
mainloop()

