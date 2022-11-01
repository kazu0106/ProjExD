import pygame as pg
import sys
from random import randint
import cv2
import numpy as np

class Screen: #画面表示に関して
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #逃げろ！こうかとん
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
        
    def blit(self):#画面に表示
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird: #こうかとんに関して
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }
    
    def __init__(self, img, zoom, xy): #細かい設定
        sfc = pg.image.load(img) # "fig/gagu.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
                


class Bomb:#爆弾に関する情報
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


def check_bound(obj_rct, scr_rct): #壁の跳ね返り
   
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def fight(): #こうかとん闘う
        img1 = pg.image.load("fig/explode.jpg")
        img2 = pg.image.load("fig/angryjpg.jpg")
        
 #---------------  2.画像を表示  --------------------------
        if key == "f":
            Screen.blit(img1, (20, 20))
            Screen.blit(img2, (150,20))
        pg.display.update() #描画処理を実行


def main(): #実際の動作
    scr = Screen("逃げろ！こうかとん", (1200, 900), "fig/darkside_2.jpg")
    kkt = Bird("fig/gagu.png", 2.0 (900,400))
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
    clock = pg.time.Clock() 
    while True:
        scr.blit() 
        
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return
        kkt.update(scr)
        bkd.update(scr)

        if kkt.rct.colliderect(bkd.rct): # こうかとんrctが爆弾rctと重ると
            return
        pg.display.update() 
        clock.tick(1000)


if __name__ == "__main__": #プログラムの終始
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()