# Lab.7 แบบ sequence
# โดยปกติการใช้งานจะเก็บตัวแปรสำหรับค่าต่างๆจัดเก้บได้ทีละ 1 ค่าต่อตัวแปร
# เป็นตัวแปรหนึ่งที่เก็บค่าได้หลายๆตัวในเวลาเดียวกัน แบ่งออกเป้นประเภท
# Tuple : 
# List : มีลักษณะคล้าย Array แต่ระบุค่าที่เป็นลบได้ (-1)
# Dictionary :

#EX.1 แบบ List 
listNunber = [2.50,4.00,3.59,2.00] #เก็บข้อมูลชนิดเดียวกันรูปแบบเดียวกัน
listCustom = ["March","Chatchard",25,2.02]
#การเข้าถึงList
print("Name: ",listCustom[1])
print("Nickname :",listCustom[0])
print ("Age :",[2])
print (listNunber)
print (listNunber[1:3])

#EX.2 ปรับปรุงข้อมุล List และ ฟังก์ชั่นพื้นฐาน
listObj = ["python","c++","SQL"]
listObj [0] = "MySQL server" #แก้ในช่องที่ 0 
listObj [1] = "Arduino" #แก้ในช่องที่ 1
print (listObj)
print(len(listObj)) #หาความยาวใน listObj

del listObj [0] #ลบข้อความในช่องที่ 0 ของ listObj
print (listObj)

#EX.3  จัดการ List ด้วย Function

listsub1 = ["กล้วยทอด","มันทอด","เผือกทอด","สาเกทอด","AAA"]
listsub2 = ["ชาไข่มุข","ชากังราว","ชาเขียว"]
listsub3 = listsub1+listsub2
print (listsub3)

listsub3.append("กล้วยทอด") #append คือเพิ่มในตำแหน่งสุดท้ายของกลุ่ม List
print (listsub3.count("กล้วยทอด")) #count นับจำนวนสมาชิกใน List

listsub3.extend("กขค") #extend คือเพิ่มตำแหน่งสุดท้ายของกลุ่ม List แบบแยก
print (listsub3)

listsub3.pop(3) #pop การลบตำแหน่งที่จุดนั้นๆออกไป
print (listsub3)

listsub3.clear() #clear การลบออกไปทั้งหมด
print (listsub3)

#listsub3.remove("AAA") #extend คือเพิ่มตำแหน่งสุดท้ายของกลุ่ม List แบบแยก
#print (listsub3)