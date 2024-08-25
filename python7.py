"""
#
# Part : python class and object
# 
"""
# Build class
class MyClass:
    x = 5

# call class
object1 = MyClass()
print("Object1 =" ,object1.x)
object2 = MyClass()
print("Object2 =" ,object2.x)

class SpyXFamily:
    def __init__(self, name_f , age_f):
        self.name = name_f
        self.age =  age_f

    def __str__(self):
        # return self.name + "  -  " + self.age   
        # {}แทรกตัวแปลแบบ ไม่ต้อง ++
        return f"{self.name} - {self.age}"     
    
    def seyHi(self, last_name = "forger") :
        print(f"Hey what'sup {self.name} {last_name}")

P1 = SpyXFamily("Anya", 8)
print(P1.name, P1.age)
print(P1)
P1.seyHi()

P2 = SpyXFamily("Damian", 8)
print(P2.name, P2.age)
print(P2)
P2.seyHi("Desmond")

class Car :
    def __init__(self, body_color, engine_size):
        self.wheels = 4
        self.window = 4
        self.window_front = 1
        self.window_back = 1
        self.body_color = body_color
        self.engine_size = engine_size

    def push_window_button(self):
        # do sometio=ng
        pass

    def pop_window_button(self):
        # do something
        pass                                    # การสร้างคลาส ช่วยลดโค้ดซ้ำซ้อน มีขนาดหญ่ 

    def turnOnfrontligth(self, status = "off") :
        if status == "on" :
            pass
            # do something
        else:
            # do something
            pass

