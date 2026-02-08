# GFX Library for SSD1306
# Part of Micropython Studio Official Libraries

class GFX:
    def __init__(self, display):
        self.display = display

    def line(self, x0, y0, x1, y1, col):
        print(f"GFX: Drawing line from {x0},{y0} to {x1},{y1}")

    def rect(self, x, y, w, h, col):
        print(f"GFX: Drawing rect at {x},{y} width {w} height {h}")
