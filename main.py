def on_a_pressed():
    global chocolate
    chocolate = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . e . . . . . . . . .
            . . . . . . e . . . . . . . . .
            . . . . . . e . . . . . . . . .
            . . . . . . e . . . . . . . . .
            . . . . . . e . . . . . . . . .
            . . . . . . e . . . . . . . . .
            . . . . . . e . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        cat,
        0,
        -100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(sprite)
    sprites.destroy(otherSprite, effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

enemySprite: Sprite = None
chocolate: Sprite = None
cat: Sprite = None
game.splash("Liam Jackson Presents Cat Invaders 13 Year Olds ONLY! Otherwise Talk About It With A Parent Or(Parental Guidance) Advisory This Game is A Work Of Ficton Do NOT IMITATE THE GAME cheat code move a and d to move and space to shoot do it fast")
scene.set_background_color(13)
cat = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . f . . . . f . . . . . .
        . . . . . . . . . . . . . . . .
        . . . f 7 f f 7 f f . . . . . .
        . . . f f f f . f f f . . . . .
        . . . f d f f f f f f . . . . .
        . . . f d d f f f f . . . . . .
        . . . f f f f f f f . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.player)
cat.set_position(73, 90)
controller.move_sprite(cat, 100, 0)
cat.set_stay_in_screen(True)
info.set_score(0)

def on_update_interval():
    global enemySprite
    enemySprite = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . e e e e e e e . . . . .
            . . . e . . . . . . e . . . . .
            . . . e e . . . . e e . . . . .
            . . . e . . . e e . e . . . . .
            . . . e e e e e e e e . . . . .
            . . . . e e e e e . . . . . . .
            . . . . e e e e e . . . . . . .
            . . . . e e e e e . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.enemy)
    enemySprite.set_position(randint(10, 160), 0)
    enemySprite.set_velocity(0, 50)
game.on_update_interval(500, on_update_interval)
