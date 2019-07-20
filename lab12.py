#LAB.12 -โปรแกรมหาผลรวม/ค่าเฉลี่ย *ประยุกค์การใช้คำสั่ง while
usernum = int(input("ป้อนจำนวนรอบ  :"))  #inputนับจำนวนรอบ
count = 0  #ตัวแปรนับจำนวนรอบ
sumObj = 0 #ตัวแปรเก็บค่าผลรวม
while(count>=0):
    score=int(input("ป้อนตัวเลขmที่ %d :"%(count+1)))
    sumObj+=score
    count+=1
    if(count==usernum):
        break
print("ผลรวมตัวเลข =%d:"%sumObj)    
print("หาค่าเฉลี่ย : %d"%(sumObj/count))
