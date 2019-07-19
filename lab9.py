#LAB.9 -การใช้งานคำสั่ง And Or

##EX.1 #ทดสอบ
#str=input("ป้อน E-mail ของคุณ")
#if(str=="march"):
#    print("สวัสดีครับ march")
#else:
#    print("สวัสดี หน้าใหม่") 


#EX.2 
#str2=input("ป้อน E-mail ของคุณ")
#if('@'in str2 and ".com" in str2): #AND เงื่อนไขสองตัวเป็นจริงถึงจะผ่าน
#    print("Email ถูกต้อง")
#else:
#    print("ป้อน Email ใหม่") 


#EX.3 
str3=input("ป้อน E-mail ของคุณ")
if(str3=="Admin" or str3=="User"): #or เงื่อนไข2ตัวอันใดอันหนึ่งเป็นจริงถึงจะผ่าน
    print(" ถูกต้อง")
else:
    print(" ป้อนใหม่") 