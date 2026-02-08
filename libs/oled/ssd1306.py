# SSD1306 Micropython Driver
# Part of Micropython Studio Official Libraries

class SSD1306:
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        self.buffer = bytearray(self.pages * self.width)

    def show(self):
        print("OLED: Updating display...")

    def text(self, string, x, y, col=1):
        print(f"OLED: Printing '{string}' at {x},{y}")
