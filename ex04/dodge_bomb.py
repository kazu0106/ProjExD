
import pygame as pg
import sys 
import time
from random import randint 


def main():
    pg.display.set_caption("Escape!! こうかとん")# 　ディスプレイ名
    scrn_sfc =pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    bomb_game_bg_sfc=pg.image.load("fig/pg_bg.jpg") #背景画像
    bomb_game_bg_rct=bomb_game_bg_sfc.get_rect() #背景画像を取り出す

    
#こうかとんについて 
    tori_sfc=pg.image.load("fig/6.png") # こうかとん
    tori_sfc=pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct=tori_sfc.get_rect()
    tori_rct.center=900,400

# 爆弾について
    baku_sfc = pg.Surface((20, 20)) # 空のSurface
    baku_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
    pg.draw.circle(baku_sfc, (255, 0, 0), (10, 10), 10) # 円を描く
    baku_rct = bomb_game_bg_sfc.get_rect()
    baku_rct.centerx = randint(0, scrn_rct.width)
    baku_rct.centery = randint(0, scrn_rct.height)

    
    clock= pg.time.Clock() # 時間をつかさどる
    
    while True:

        scrn_sfc.blit(bomb_game_bg_sfc,bomb_game_bg_rct) # スクリーンに貼り付け
    
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                return

            #if event.type == pg.KEYDOWN and event.key==pg.K_F1:
                #scrn_sfc = pg.display.set_mode((800,600),pg.FULLSCREEN)
            
            #if  event.type == pg.KEYDOWN and event.key==pg.K_ESCAPE:
                #scrn_sfc = pg.displayget_mode((800,600),pg.FULLSCREEN)

        #操作について
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:    tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:  tori_rct.centery += 1
        if key_states[pg.K_LEFT]:  tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]: tori_rct.centerx += 1
        
        scrn_sfc.blit(tori_sfc,tori_rct) # スクリーンに貼り付け
       
        scrn_sfc.blit(baku_sfc, baku_rct)
        
        pg.display.update() #更新
        clock.tick(1000) #framerate 1000　1秒あたり1000フレーム　1秒間で1000フレーム



if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()