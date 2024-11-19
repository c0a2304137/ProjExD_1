import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")   #oadで読み込まれるとSurfaceとなる
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            rit = (-1, -1)
        #    kk_rct.move_ip(0, -1)
        elif key_lst[pg.K_DOWN]:
            rit = (-1, +1)
         #   kk_rct.move_ip(0, +1)
        #if key_lst[pg.K_LEFT]:  
        #kk_rct.move_ip(-1, 0)
        elif key_lst[pg.K_RIGHT]:
            rit = (1, 0)  
        #    kk_rct.move_ip(+2, 0)
        else:
            rit = (-1, 0)
            
        kk_rct.move_ip(rit)


        x = -(tmr % 3200)
        screen.blit(bg_img, [x, 0])  #screan Surfaceに背景画像Surfaceに張り付ける
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img,  [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        # screen.blit(kk_img, [300, 200])  #練習4
        screen.blit(kk_img, kk_rct) 
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()