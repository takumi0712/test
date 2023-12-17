import pyxel

class app:
    def __init__(self):
        pyxel.init(256,192)

        self.x = 0
        self.y = 0

    def update(self):
        self.x += 1
        self.y += 1
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x,self.y,10,10,2)

if __name__ == "__main__":
    app()