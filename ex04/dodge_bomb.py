
import pygame as pg
import sys 
import time
from random import randint

#こうかとん、爆弾が画面外に出たかどうかチェックする
def check_bound(obj_rct,scr_rct):
    
    yoko, tate=+1, +1
    if obj_rct.left < scr_rct .left or scr_rct.right < obj_rct .right:# 横に関して
        yoko=-1
    if obj_rct.top < scr_rct .top or scr_rct.bottom < obj_rct.bottom:#縦に関して
        tate=-1
    return yoko,tate

def main():
    pg.display.set_caption("Escape!! こうかとん")# 　ディスプレイ名

    #背景について  
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

    vx, vy = +1, +1 #爆弾が移動する

    #表示時間   
    clock= pg.time.Clock() 
    
#実際の動作   
    while True:

        scrn_sfc.blit(bomb_game_bg_sfc,bomb_game_bg_rct) # スクリーンに貼り付け
    
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                return
        
        #操作について
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:    tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:  tori_rct.centery += 1
        if key_states[pg.K_LEFT]:  tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]: tori_rct.centerx += 1

        yoko, tate=check_bound(tori_rct,scrn_rct)
      
        #壁にぶつかったかどうかの具体的な条件
        if yoko == -1:
            if key_states[pg.K_LEFT]: 
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        
        if tate == -1:
            if key_states[pg.K_UP]: 
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1  
        scrn_sfc.blit(tori_sfc,tori_rct)    # こうかとん貼り付け     
        

    #爆弾の壁判定
        yoko, tate = check_bound(baku_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        baku_rct.move_ip(vx, vy) 
        scrn_sfc.blit(baku_sfc, baku_rct) 
        baku_rct.move_ip(vx,vy)
        scrn_sfc.blit(baku_sfc, baku_rct)   #爆弾貼り付け
        
        
        
        if tori_rct.colliderect(baku_rct):
            return 
        
        pg.display.update() #更新
        clock.tick(1000) #framerate 1000　1秒あたり1000フレーム　1秒間で1000フレーム

#プログラムの開始・終了
if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()