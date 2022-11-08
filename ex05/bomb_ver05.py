import pygame as pg
import tkinter as tk
import sys
from random import randint
#import cv2
#import numpy as np

#画面表示に関して
class Screen: 
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #逃げろ！こうかとん
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
        
    def blit(self):#画面に表示
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


#こうかとんに関して
class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }
    
    def __init__(self, img, zoom, xy): #細かい設定
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

    def blit(self, scr:Screen):#貼り付け
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):#更新内容適用
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
                

#爆弾に関する情報
class Bomb:
    
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 円の大元を造る
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        #円の中心を決める
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy #円が動く

    def blit(self, scr:Screen):#貼り付け
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)

#ブロック詳細設定
class Block: 
        
    def __init__(self, rect,x,y):
        self.rect=rect
        self.rect=pg.Rect(100, 200,20,40)
        self.src=Screen
        # ブロックの左上座標 描画
        self.rect.left = self.src.left + x * self.rect.width 
        self.rect.top = self.src.top + y * self.rect.height
            
        #ブロックの判定
        blocks_collided = pg.sprite.spritecollide(self, self.blocks, True)
        if blocks_collided:  # 衝突ブロックがある場合
            broken_rect = self.rect #ブロックを認識するためのリスト
            for block in blocks_collided:
                
                # ボールが左からブロックへ衝突した場合
                if broken_rect.left < block.rect.left and broken_rect.right < block.rect.right:
                    self.rect.right = block.rect.left
                    self.dx = -self.dx #跳ね返る
                    
                
                # ボールが右からブロックへ衝突した場合
                if block.rect.left < broken_rect.left and block.rect.right < broken_rect.right:
                    self.rect.left = block.rect.right
                    self.dx = -self.dx #跳ね返る

                # ボールが上からブロックへ衝突した場合
                if broken_rect.top < block.rect.top and broken_rect.bottom < block.rect.bottom:
                    self.rect.bottom = block.rect.top
                    self.dy = -self.dy #跳ね返る

                # ボールが下からブロックへ衝突した場合
                if block.rect.top < broken_rect.top and block.rect.bottom < broken_rect.bottom:
                    self.rect.top = block.rect.bottom
                    self.dy = -self.dy #跳ね返る         



#壁の跳ね返り
def check_bound(obj_rct, scr_rct): 
   
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main(): #実際の動作
    scr = Screen("逃げろ！こうかとん", (1200, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900,400))
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
    rect=pg.Rect(100,200,20,40)
    
    block_design=Block(rect,3,3)

    
    clock = pg.time.Clock() 
    while True:
        scr.blit() 
        
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return
      
        bkd.update(scr)
        kkt.update(scr)

        if kkt.rct.colliderect(bkd.rct): # こうかとんrctが爆弾rctと重ると
            return
        pg.display.update() 
        clock.tick(1000)


if __name__ == "__main__": #プログラムの終始
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()