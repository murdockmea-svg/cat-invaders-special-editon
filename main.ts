controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    chocolate = sprites.createProjectileFromSprite(img`
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
        `, cat, 0, -100)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(sprite)
    sprites.destroy(otherSprite, effects.fire, 100)
    info.changeScoreBy(1)
})
let enemySprite: Sprite = null
let chocolate: Sprite = null
let cat: Sprite = null
game.splash("LJ Presents Cat Invaders DO NOT IMITATE 13 OR PARENTAL QUIDANCE")
scene.setBackgroundColor(13)
cat = sprites.create(img`
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
    `, SpriteKind.Player)
cat.setPosition(73, 90)
controller.moveSprite(cat, 100, 0)
cat.setStayInScreen(true)
info.setScore(0)
game.onUpdateInterval(500, function () {
    enemySprite = sprites.create(img`
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
        `, SpriteKind.Enemy)
    enemySprite.setPosition(randint(10, 160), 0)
    enemySprite.setVelocity(0, 50)
})
