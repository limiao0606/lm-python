class Gun:
    def __init__(self, model):

        #1.枪的型号
        self.model = model

        #2.子弹的数量
        self.bulle_count = 0
    def add_bulle(self,count):
        self.bulle_count += count
    def shoot(self):
        #1.判断子弹数量
        if self.bulle_count <= 0:
            print("[%s] 没有子弹了..." %self.model)
            return #不需执行下方代码
        #2.发射子弹
        self.bulle_count -= 1
        #3.提示发射信息
        print("[%s] tututu...[%d]"%(self.model, self.bulle_count))

class Soldier:
    def __init__(self, name):
       #1.姓名
        self.name = name
       #2.枪 -新兵没有枪
        self.gun = None
    def fire(self):
        #1.判断士兵是否有枪
        if self.gun == None:
            print("[%s]还没有枪"%self.name)
            return
        #2.高喊口号
        print("冲啊...[%s]"%self.name)
        #3.让枪装填子弹
        self.gun.add_bulle(50)
        #4.让枪发射子弹
        self.gun.shoot()
#1.创建枪对象
ak47 = Gun("AK47")

#2.创建许三多
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()
print(xusanduo.gun)