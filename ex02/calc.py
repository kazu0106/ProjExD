import tkinter as tk
import tkinter.messagebox as tkm

def click_number(event):#数字の入力に対する対応
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END, num) 
    b = event.widget.flash()#点滅をさせる部分 


def click_equal(event):#=に関する入力に対する対応
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)
    b = event.widget.flash()#点滅をさせる部分


root = tk.Tk() 
root.geometry("300x500")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right") # 練
entry.grid(row=0, column=0, columnspan=3)

r, c = 1, 0 # 
numbers = list(range(9, -1, -1)) # 
operators = ["+"] # ＋だけ用意



for i, num in enumerate(numbers+operators, 1):#電卓を造る
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", click_number)
    
    b = tk.Button(text=f"{num}", bg='light blue',font=("",30),width=4,height=2)#点滅を実装
    b.bind('<1>' ,click_number) 
    
    btn.grid(row=r, column=c)   #縦横を仕切
    b.grid(row=r, column=c)
    c += 1
    
    if i%3 == 0: #縦横　3列　4列の判別　
        r += 1
        c = 0


btn = tk.Button(root, text=f"=", font=("", 30),bg='red', width=4, height=2)

btn.bind("<1>", click_equal)

btn.grid(row=r, column=c) #=を実装

root.mainloop()