#EX.17-การสร้างฟังก์ชั่น function
#เป็นกลุ่มที่อยู่ของคำสั้งที่เรียกใช้งานซ้ำๆ,โปรแกรมย่อยๆ (Method)


#การประกาศฟังก์ชั่น
def showMessage ():
    print("chatchard"+"python")

def showNumber ( ):

    for i in range(1,13):
     print("%d * %d = %d "%(2,i,(2*i)))    

def showInput (str):
    print(str)
 #การเรียกใช้งาน **เรียกใช้หลายครั้งได้
showMessage() 
showNumber()
showInput("chatchard")
