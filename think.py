# created by xibai


import tkinter as tk
window = tk.Tk()
window.title('JJ GUI')
window.geometry('500x300')
var = tk.StringVar()
var.set('你是猪头')
l = tk.Label(window,textvariable=var,bg='green',font=('Arial,12'),width=60,height=1)
l.pack()
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        var.set('果然是猪头')
    else:
        var.set('')
b = tk.Button(window,text='不是',width=15,height=2,command=hit_me)
b.pack()
e = tk.Entry(window,show='*')
e.pack()
window.mainloop()

