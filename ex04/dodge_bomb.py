
import pygame as pg
import sys 
import time


def main():
    pg.display.set_caption("Escape!! こうかとん")# 　ディスプレイ名
    scrn_sfc =pg.display.set_mode((1600,900))
    bomb_sfc=pg.image.load("fig/pg_bg.jpg") #背景画像
    bomb_rct=bomb_sfc.get_rect() #背景画像を取り出す

    
    tori_sfc=pg.image.load("fig/6.png") # こうかとん
    tori_sfc=pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct=tori_sfc.get_rect()
    tori_rct.center=900,400

    
    clock= pg.time.Clock() # 時間をつかさどる
    
    while True:

        scrn_sfc.blit(bomb_sfc,bomb_rct) # スクリーンに貼り付け
    
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                return

            #if event.type == pg.KEYDOWN and event.key==pg.K_F1:
                #scrn_sfc = pg.display.set_mode((800,600),pg.FULLSCREEN)
            
            #if  event.type == pg.KEYDOWN and event.key==pg.K_ESCAPE:
                #scrn_sfc = pg.displayget_mode((800,600),pg.FULLSCREEN)

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:    tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:  tori_rct.centery += 1
        if key_states[pg.K_LEFT]:  tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]: tori_rct.centerx += 1
        
        scrn_sfc.blit(tori_sfc,tori_rct) # スクリーンに貼り付け
       
        pg.display.update() #更新
        clock.tick(1000) #framerate 1000　1秒あたり1000フレーム　1秒間で1000フレーム



if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()