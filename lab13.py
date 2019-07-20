#LAB.13 โปรแกรมหาผลรวม Loop ต่อเนื่อง
#  ไม่จำกัดค่าจนกว่าเงื่อนไขจะเป็นเท็จ

sumObj = 0 #ตัวแปรเก็บค่าผลรวม

while(True):
  score=int(input("ป้อนตัวเลขที่ น้อยกว่า 0 คือเลิกทำ :"))
  if(score<0):
     break

  sumObj+=score
print("ผลรวมตัวเลข =%d:"%sumObj)    
