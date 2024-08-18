"""
#
# Part : pythoncollection
# List, Tuple, set and dictiononary
# 
"""

"""
#
# Part : python List
# 
"""

this_list = ["apple", "banana", "coconut", "apple", "banana"]   #
print(this_list)
print(type(this_list))
print(len(this_list))
5
print(this_list[2])                                             #
this_list.append("cherry")
print(this_list, len(this_list))
this_list.insert(1,"orange")                                    #
print(this_list, len(this_list))

this_list2 = ["apple", "banana", "coconut", "apple", "banana"]  # เพิ่มข้อมูล
this_list3 = ["mango", "pineaapple", "grape"]
this_list2.extend(this_list3)
print(this_list2, len(this_list2))

this_list4 = ["apple", "banana", "coconut", "apple", "banana"]  #ลบแบบระบบคำ
this_list4.remove("banana")
print(this_list4, len(this_list4))

this_list5 = ["apple", "banana", "coconut", "apple", "banana"]  #ลบแบบระบุตำแหน่ง
this_list5.pop(2)
print(this_list5, len(this_list5))

this_list6 = ["apple", "banana", "coconut", "apple", "banana"]  #ลบข้อมูลที่ระบุหมด
del this_list6[1]
print(this_list6, len(this_list6))

this_list6.clear()                                              #ลบเหลือความว่างเปล่า
print(this_list6, len(this_list6))


this_list7 = ["apple", "banana", "kiwi", "pineapple", "banana"]  #เรียงตามตัวอักษร
this_list7.sort()
print(this_list7, len(this_list7))

this_list8 = ["apple", "banana", "kiwi", "pineapple", "banana"]  #เรียงข้อมูลจากหลังมาหน้า
this_list8.reverse()
print(this_list8, len(this_list8))

list1 = ["a", "b", "c"]
list2 = [1 ,2 , 3]
list3 = list1 + list2
print(list3)


"""
#
# Part : python tuple
# 
"""

this_tuple = ("apple", "banana", "coconut")
print(this_tuple)       # แสดงผลข้อมูล
print(type(this_tuple)) # เช็คชนิดข้อมูล
print(len(this_tuple))  # เช็คจำนวนข้อมูล

print(this_tuple[0])    # แสดงข้อมูลตำแหน่งที่ 0

# การเพิ่มข้อมูลของ tuple ต้องทำเป็น list เพราะ tuple เพิ่มข้อมูลไม่ได้
this_tuple2 = ("apple", "banana", "coconut")    
this_tuple3_list = list(this_tuple2)
print(this_tuple3_list, type(this_tuple3_list))
this_tuple4 = tuple(this_tuple3_list)
print(this_tuple4, type(this_tuple4))
      
this_tuple5 = ("apple", "banana", "coconut")   
this_tuple6_list = list(this_tuple5)
this_tuple6_list.append("durian")
this_tuple7 = tuple(this_tuple6_list)
print(this_tuple7, type(this_tuple7))

this_tuple8 = ("apple", "banana", "coconut")   
this_tuple9_list = list(this_tuple8)
this_tuple9_list.remove("banana")
this_tuple8 = tuple(this_tuple9_list)
print(this_tuple8, type(this_tuple8))

tuple1 = ("a","b","c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3, type(tuple3))


"""
#
# Part : python set
# 
"""

this_set = ("apple", "banana", "coconut")   
print(this_set)
print(type(this_set))
print(len(this_set))

for x in this_set:
    print(x)

this_set2 = {"apple", "banana", "coconut"} 
this_set2.add("durian")                         #เพิ่มข้อมูล
print(this_set2,type(this_set2))
this_set2.remove("coconut")                     #ลบข้อมูล
print(this_set,type(this_set2))

this_set3 = {"apple", "banana", "coconut"}      #เพิ่มข้อมูล
this_set4 = {"durian", "grape"}
this_set3.update(this_set4)
print(this_set3,type(this_set3))

this_set5 = {"apple", "banana", "coconut"}     #เพิ่มข้อมูล
this_set6 = {"durian", "grape"} 
this_set7 = {1, 2, 3}
this_set8 = this_set5 | this_set6 | this_set7
print(this_set8), type(this_set8) 

this_set8.clear()
print(this_set8), type(this_set8) 
del this_set8

"""
#
# Part : python dictionary
# 
"""
this_dict = {
    "brand" : "Ford",
    "model" : "Rapter",
    "year"  : "2024"
}
print(this_dict)
print(type(this_dict))
print(len(this_dict))

print(this_dict["brand"])
print(this_dict.get("year"))
print(this_dict.keys())

this_dict["year"] = "1987"
print(this_dict)
this_dict.update({
    "year" : "1987",
    "model": "Mustang"
})
print(this_dict)

this_dict["color"] = "red"          # เพิ่มข้อมูล
print(this_dict)

del this_dict["year"]               # ลบข้อมูลที่ระบุ
print(this_dict)

this_dict.clear                     # ลบทั้งหมด
print(this_dict, type(this_dict))
del this_dict
#print(this_dict, type(this_dict))

this_dict2 = {
    "brand" : "Toyota",
    "model" : "Yaris",
    "year"  : "2016"
}

this_dict3 = {
    "brand" : "Honda",
    "model" : "Civic",
    "year"  : "2024"
}   

this_dict4 = {
    "brand" : "Lamborgini",
    "model" : "huracan",
    "year"  : "2019"
}

my_car = {
    "car1" : this_dict2,
    "car2" : this_dict3,
    "car3" : this_dict4
}
print(my_car, len(my_car))
print(my_car["car2"]["model"])

