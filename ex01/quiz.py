import random

def main():
    quetions=["サザエさんの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    correct_1=["マスオ","ますお"]
    correct_2=["わかめ","ワカメ"]
    correct_3=["甥","おい","甥っ子","おいっこ"]
    
    que=random.choice(quetions)
    ans=input("答えるんだ :")
    
    print("問題:")
    print(que)
    print(ans)
    

    if (ans in correct_1) and quetions[0]:
        print("正解")
    if (ans in correct_2) and quetions[1]:
        print("正解")
    if (ans in correct_3) and quetions[2]:
        print("正解")
    else:
        print("不正解") 
 

    

    


