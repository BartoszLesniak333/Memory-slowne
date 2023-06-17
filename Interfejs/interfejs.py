import pygame as pg

FPS = 60
WIDTH, HEIGHT = 800, 600

win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Topic17")


def draw(win):
    win.fill("white")
    pg.display.update()


def main():
    clock = pg.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break

        draw(win)

    pg.quit()
    quit()


if __name__ == "__main__":
    main()