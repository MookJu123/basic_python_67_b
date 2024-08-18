"""
#
# part: Python comment
#
"""

# this is a comment ทีละบรรทัด
# v = s/t
# v = ความเร็ว (m/s)
# s = ระยะทาง (m)
# t = เวลา (s)

""" คอมเมนต์หลายบรรทัด
this is a comment
v = s/t
v = ความเร็ว (m/s)
s = ระยะทาง (m)
t = เวลา (s)
"""

# สั่งปริ้น เเสดงผล

print("hello world!!!!")


"""
#
# part: Python Variable
#
"""

x = 5               # integer
y = "Hey Bruh"      # string
print(x, y)

x = str(5)
y = int(5)
z = float(5)
print(type(x), type(y), type(z))

"""
#
# part: VARIAABLE NAME
#
"""
myvar = "john" 
my_var = "john"        # นิยม ตั้งชื่อตััวแปลไม่ยาวมาก
_my_var = "john"       #
myVar = "john"
MYVAR = "john"
MY_VAR = "john"
my_var2 = "john"

# ตั้งตัวแปลแบบนี้ไม่ได้
# 2my_var = "john" 
# my - var = "john" 
# my var = "john"

# camal case
myVariableName = "john"
# Pascal case
MyVariableName = "john"
# Snake case
my_variable_name = "john"

"""
#
# part: python string
#
"""

x = "Hey Burh"
print(x)

y = """1 Hey Burh
2 Hey Burh
3 Hey Burh
"""
print(y)
x = "Hey Bruh"
print(x[2])
print(len(x))                 # เช็คขนาดตัวแปล
print("Hey" in x)
print("what'sup" not in x)     # เช็คคำหยาบ
print(x.upper())               # จัดตัวอักษรห้เป็นขนาดเล็ก เช่น email
print(x.lower())               # จัดตัวอักษรห้เป็นขนาดsหญ่

print(x.replace("Bruh", "Sis"))
print(x.split(" "))

# ต่อคำ
a = "apple"
b = "Company"
print( a+ " " + b)

#
price = 20
word = f"Price: {price:.2f}"
print(word)


