import tkinter as tk
from turtle import bgcolor
import maze_maker as mm 
import tkinter.messagebox as tkm 

#キーが押された時の反応=================================
def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""





def main_proc():
    global mx, my
    global cx, cy
 ##こうかとんが移動する   =================================
    #通常の移動
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_lst[my][mx] == 0: 
        cx, cy = mx*100+50, my*100+50 #こうかとんの座標
    
    else:  #画面下に到達時
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
        
   #壁を歩く==== 
    if key=="w":
        
        button = tk.Button(root, text="Wall Mode", command = lambda: 
        tkm.showinfo("Mode Wall", "壁の上を歩きます",)) #ボタンWidgetを生成
        button.place(x=750, y=450,relheight = 0.2, relwidth = 0.4,) #ボタンを配置
        
        
        if key == "Up":
            my -= 1
        if key == "Down":
            my += 1
        if key == "Left":
            mx -= 1
        if key == "Right":
            mx += 1
        if maze_lst[my][mx] == 1: 
            cx, cy = mx*100+150, my*100+150 #こうかとんの座標
    
        else:  #画面下に到達時
            if key == "Up":
                my += 1
                
            if key == "Down":
                my -= 1
            if key == "Left":
                mx += 1
            if key == "Right":
                mx -= 1
#====

    if key=="m":
        tkm.showinfo("Moving","壁が動くよ")

    if key == "e":
        tkm.showinfo("ESCAPE","脱出成功")
    
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)
#==================================================================


if __name__ == "__main__": #main関数
    
    root = tk.Tk()
    root.title("迷えるこうかとん") 

    
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    maze_lst = mm.make_maze(15, 9)
   
    mm.show_maze(canv, maze_lst) 
    

    
    tori = tk.PhotoImage(file="ex03/fig/fig/5.png") 
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50 
   
    canv.create_image(cx, cy, image=tori, tag="tori")

    
    key = "" 

    
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)    

    
    main_proc()

    root.mainloop()