#การประกาศ Function ,
#EX.1 
def showMessage(istr):
    print(istr)    
showMessage("ทดสอบการส่งค่าเข้ามาใน Function")

print("รูปแบบ 1 ")#เว้นบรรทัดเวลาแสดงผล

#รูปแบบ 1 การสร้างฟังก์ชั่นที่ไม่มีค่าส่งกลับ
def showData ():
    print("chatchard")
showData()    



#รูปแบบ 2 การสร้างฟังก์ชั่นที่มีการรับค่ามาทำงาน
print("รูปแบบ 2")
def  showstr (str):
    print(str)
showstr("Python")  
showstr("MARCH") 

#รูปแบบ 3 การสร้างฟังก์ชั่นที่
print("รูปแบบ 3 ")
def minimum(num1,num2):
    minvalue =0 
    if (num1>num2):
        minvalue=num2
    elif(num1<num2):
        minvalue=num1
    else:
        minvalue=num1   
    return minvalue    
minArr =minimum(10,10)   
print("ค่าที่น้อยที่สุด :%d"%minArr)