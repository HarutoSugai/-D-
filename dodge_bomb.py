import pygame as pg
import sys
import random

delta={pg.K_UP:(0,-1),
       pg.K_DOWN:(0,+1),
       pg.K_LEFT:(-1,0),
       pg.K_RIGHT:(+1,0)}

def main():
    kaiten=0
    bbsize=20
    time=0
    bwnd=0
    rr=255
    gg=0
    bb=0
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("2day/ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("2day/ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, kaiten, 2.0)
    kk_rct=kk_img.get_rect()
    tmr = 0
    bb_img = pg.Surface((bbsize,bbsize))
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)
    bb_img.set_colorkey((0,0,0))
    x,y=random.randint(0,1600),random.randint(0,900) 
    screen.blit(bb_img, [x, y])
    vx,vy=+1,+1
    bb_rct=bb_img.get_rect()
    bb_rct.center=(x,y)
    kk_rct.center=(900,400)


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        if tmr%1000==200:
            bb_img = pg.Surface((bbsize,bbsize))
            pg.draw.circle(bb_img,(rr,gg,bb),(bbsize/2,bbsize/2),bbsize/2)
            bb_img.set_colorkey((0,0,0))
            bbsize+=10
            rr=255
            bb=0
            gg=0
        

        key_lst=lst=pg.key.get_pressed()
        for k,mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)
        if c_b(screen.get_rect(),kk_rct)!=(True,True):
            for k,mv in delta.items():
                if key_lst[k]:
                    kk_rct.move_ip(-mv[0],-mv[1])    

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx,vy)
        yoko,tate=c_b(screen.get_rect(),bb_rct)
        if not yoko:  #横にはみ出ている
            vx*=-1.2
            bwnd+=1
            bb_img = pg.Surface((bbsize,bbsize))
            pg.draw.circle(bb_img,(rr,gg,bb),(bbsize/2,bbsize/2),bbsize/2)
            bb_img.set_colorkey((0,0,0))
            rr=0
            bb=255
            gg=0
        if not tate:  #縦にはみ出ている
            vy*=-1
            bb_img = pg.Surface((bbsize,bbsize))
            pg.draw.circle(bb_img,(rr,gg,bb),(bbsize/2,bbsize/2),bbsize/2)
            bb_img.set_colorkey((0,0,0))
            rr=0
            bb=0
            gg=255

        screen.blit(bb_img,bb_rct)

        if kk_rct.colliderect(bb_rct):
            kaiten=5
            kk_img = pg.transform.rotozoom(kk_img, kaiten, 0.95)
            
            time+=1
            if time>=50:
                return
        
        if time>=1:
            time+=1
            if time>50:
                return

        pg.display.update()
        clock.tick(1000)







def c_b(scrrct:pg.Rect,objrct:pg.Rect)-> tuple[bool,bool]:
    """
    オブジェクトが画面内かどうかの処理
    引数１　画面内SURFACEのRECT
    引数２　こうかとんとばくだんSURFACEのRECT
    """
    yoko,tate=True,True

    if objrct.left<scrrct.left or scrrct.right<objrct.right:
        yoko=False
    if objrct.top<scrrct.top or scrrct.bottom<objrct.bottom:
        tate=False
    return yoko,tate




if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()