import tkinter as tk
from turtle import width
root=tk.Tk()
root.title("電卓")
root.geometry("300x500")

def bt_click(event):
    btn = event.widget
    calc_n = btn["text"]

r, c = 0, 0
for i, calc_n in enumerate(range(9,-1, -1), 1):
    btn = tk.Button(root, text=f"{calc_n}", width=3, height=4)
    btn.bind("<2>",bt_click)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
         r += 1
         c = 0
root.mainloop()

