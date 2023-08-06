# khai báo các thông tin cần xử dụng 
import random
import math

class Center:
    def __init__(self, pos_x=0, pos_y=0, nk=0, si=0, di=0, ti=20):
        """
        pos_x   : Toạ độ x
        pos_y   : Toạ đô y
        nk      : Số users trong cụm
        si      : Datasize
        di      : Deadline
        ti      : Time deadline
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.nk = nk
        self.id = []
        self.si = si
        self.di = di
        self.ti = ti
        self.gen_point()


    def gen_point(self):
        self.pos_x = random.randint(0, 800)
        self.pos_y = random.randint(0, 800)

        # note th < 0
        self.nk = int(max(1, min(4, random.gauss(3.2, 0.5))))

        self.si = []
        self.di = []
        id = 1
        for i in range(self.nk):
            self.si.append(max(1, min(100, random.gauss(50, 20))))
            self.di.append(max(1, min(100, random.gauss(50, 20))))