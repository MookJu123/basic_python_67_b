"""
#
# Part : python while loop
# 
"""

# while ทำเมื่อเป็นจริง (ถ้าเป็นจริงอนันต์ คอมจะทำงานหนักจนพังได้)
i = 1
while i < 5 :
    print
    i += 1  # i = i + 1

# ป้องกันค่า while เป็นอนันต์ 
i = 1
while i < 5 :
    print("i =" , i)
    if i == 3:
        break
    i += 1  # i = i + 1

# ทำให้ค่า while เป็นอนันต์
# i = 1
# while i < 5 :
#    print("i =" , i)
#   if i == 3:
#        continue
#    i += 1  # i = i + 1

# ออกจาก while เพื่อคำนวณค่าอื่นเพิ่ม
i = 1
while i < 5 :
    print("i =" , i)
    i += 1  # i = i + 1
else :
    print("Game Over")


"""
#
# Part : python for loop
# (เข้าใจง่ายกว่า while โอกาศอนันต์น้อย)
# 
"""

fruits = ["apple", "banana", "coconut"]
for fruit in fruits :                   #
    print("Fruits: ", fruit)

fruits = ["apple", "banana", "coconut"]
for fruit in fruits :
    print("Fruits: ", fruit)
    if fruit == "banana" :
        break

fruits = ["apple", "banana", "coconut"]
for fruit in fruits :
    if fruit == "banana" :
        break
    print("Fruits: ", fruit)

fruits = ["apple", "banana", "coconut"]
for fruit in fruits :
    print("Fruits: ", fruit)
    if fruit == "banana" :
        continue 

for x in range(len(fruits)):        # วน loop เท่าจำนวนตัวแปล
    print("Number: ", x)

for x in range(5):                  # วน loop 5 รอบแล้วสั่ง game over
    print("Number: ", x)
else:
    print("Game Over")

# loop for มักจะไม่เกิน 4 ชั้น 
adjs = ["red", "blue", "green"]
fruits = ["apple", "banana", "coconut"]
for adj in adjs :
    for fruit in fruits:
        print("Fruits: " + adj + " " + fruit)

















