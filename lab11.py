#Lab.11 -การใช้งานคำสั่ง While *(วนซ้ำ-loop)
#EX.1 
#score=int(input("ป้อนตัวเลข"))
count = 0  #นับจำนวนรอบ
sumObj = 0 #ตัวแปนเก็บค่าผลรวม
#while(score>0): #
#    count+=1
#    print("HELLOW")
#    print("ค่าของ Count = %d"%(count))
while(count>=0):
    score=int(input("ป้อนตัวเลขmที่ %d :"%(count+1)))
    count+=1
    sumObj+=score
    if(count==4):
        break
print("ผลรวมตัวเลข =%d:"%sumObj)        



