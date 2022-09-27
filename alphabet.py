import random
import datetime

#基本情報　全て26　対象10　欠損2　挑戦2

all = 26  
subjects = 10 
loss = 2  
challenge = 2 
#===================================

def reqest(alphabet):#問題文の設定
    
    all_al = random.sample(alphabet, subjects) # 最初に並び替えておくA-Z
    print("対象文字：", end="")
    for exchange in sorted(all_al): 
        print(exchange, end=" ")

    loss_al= random.sample(all_al, loss)  #欠損文字を選ぶ
    print("表示文字：", end="")
    for exchange in all_al: 
        if exchange not in loss_al :  
            print(exchange, end=" ")

def Correct(ans):
    ele = input("欠損文字はいくつあるでしょうか？：") #欠損文字の個数 
    if ele != loss: 
        print("不正解です。")
    
    else : 
        print("正解です．では，具体的に欠損文字を1つずつ入力してください．")
        for  spe in range(ans):
            print(f'{spe+1}番目の数を入力してください。')

    

   
   

