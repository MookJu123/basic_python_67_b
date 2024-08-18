# สร้างลิสต์ของตัวเลขจาก 21 ถึง 40
numbers = list(range(21, 41))

# แยกจำนวนคี่และจำนวนคู่
odd_numbers = []
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)  # ถ้าเลขหาร 2 ลงตัว (เป็นจำนวนคู่) ให้เพิ่มลงใน even_numbers
    else:
        odd_numbers.append(num)     # ถ้าเลขหาร 2 ไม่ลงตัว (เป็นจำนวนคี่) ให้เพิ่มลงใน odd_numbers

print("เลขคี่:", odd_numbers)
print("เลขคู่:", even_numbers)
    
