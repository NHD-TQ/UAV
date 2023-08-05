# khai báo các thông tin cần xử dụng 
import random
import math

class Center:
    def Center(self, pos_x, pos_y, nk, si, di, ti=20):
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
        self.si = si
        self.di = di
        self.ti = ti
        self.name_user = []

    def Center(self):
        pass  

    def gen_point(self):
        self.pos_x = random.randint(0, 800)
        self.pos_y = random.randint(0, 800)

        # note th < 0
        self.nk = int(max(1, min(4, random.gauss(2, 1))))

        self.si = []
        self.di = []
        self.name_user = []
        for i in range(self.nk):
            self.name_user.append(i)
            self.si.append(max(1, min(100, random.gauss(50, 20))))
            self.di.append(max(1, min(100, random.gauss(50, 20))))
            
        return self.pos_x, self.pos_y, self.nk, self.si, self.di