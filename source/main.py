from tkinter import *
def claer_windo():
  result.delete('0', 'end')


def add_iteam(number):
  total = result.get()
  result.delete('0', 'end')
  global msg
  msg  = str(total) + str(number)
  result.insert(END, msg)


def result_iteam():
  global msg
  result.delete('0', 'end')
  result.insert(END, eval(msg)) // i need remove this (RCE)
  msg = ''
 

element = 0
window = Tk()
window.title('מחשבון')
window.geometry('210x230')
window.iconbitmap('logo.ico')
window.resizable(False, False)

result = Entry(window, bd='20', width='27')
result.place(y=5,x=5)
number_one = Button(window, text='1', bd='5', width='7', command=lambda : add_iteam(1))
number_one.place(y=65,x=7)
number_two = Button(window, text='2', bd='5', width='7', command=lambda : add_iteam(2))
number_two.place(y=65,x=70)
number_Third = Button(window, text='3', bd='5', width='7', command=lambda : add_iteam(3))
number_Third.place(y=65,x=133)
number_four = Button(window, text='4', bd='5', width='7', command=lambda : add_iteam(4))
number_four.place(y=95,x=133)
number_five = Button(window, text='5', bd='5', width='7', command=lambda : add_iteam(5))
number_five.place(y=95,x=70)
number_Six = Button(window, text='6', bd='5', width='7', command=lambda : add_iteam(6))
number_Six.place(y=95,x=7)
number_seven = Button(window, text='7', bd='5', width='7', command=lambda : add_iteam(7))
number_seven.place(y=125,x=7)
number_eight = Button(window, text='8', bd='5', width='7', command=lambda : add_iteam(8))
number_eight.place(y=125,x=70)
number_Nine = Button(window, text='9', bd='5', width='7', command=lambda : add_iteam(9))
number_Nine.place(y=125,x=133)
number_minues = Button(window, text='-', bd='5', width='7', command=lambda : add_iteam('-'))
number_minues.place(y=155,x=7)
number_plues = Button(window, text='+', bd='5', width='7', command=lambda : add_iteam('+'))
number_plues.place(y=155,x=70)
number_zero = Button(window, text='0', bd='5', width='7', command=lambda : add_iteam(0))
number_zero.place(y=155,x=133)
number_multiplication = Button(window, text='x', bd='5', width='7', command=lambda : add_iteam('*'))
number_multiplication.place(y=185,x=7)
number_reslut = Button(window, text='=', bd='5', width='7', command=result_iteam)
number_reslut.place(y=185,x=70)
number_claer = Button(window, text='claer', bd='5', width='7', command=claer_windo)
number_claer.place(y=185,x=133)

window.mainloop()
