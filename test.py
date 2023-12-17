import pyxel

class app:
    def __init__(self):
        pyxel.init(256,256)

        self.x = 0
        self.y = 0

    def update(self):
        self.x += 1
        self.y += 1
    def draw(self):
        pyxel.cls(1)
        pyxel.rect(self.x,self.y,100,100,2)
app()
