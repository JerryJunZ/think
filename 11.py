# created by xibai
import time
class auto():
    def __init__(self):
        intx, inty = 20, 30
        nx, ny = 100, 90
        self.x, self.y = nx - intx, ny - inty
        print(self.x, self.y)
    def key(intkey):
        print('start:',intkey)
        time.sleep(1)
        print('end:',intkey)
    def move():
        if self.x > 0 :
            key('d')
        elif x < 0 :
            key('a')
        else:
            pass
        if y < 0:
            key('w')
        elif y > 0:
            key('s')
        else:
            pass
    while True:
        move()

