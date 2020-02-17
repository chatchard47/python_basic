#EX.10-โปรแกรมคำนวณเกรด
score = int(input("คะแนน  :"))
if (score>=80 and score<100):
    print("A")
elif (score>=75 and score<=79):
    print ("B+")
elif (score>=70 and score<=74):
    print ("B")
elif (score>=65 and score<=69):
    print ("C+")
elif (score>=60 and score<=64):
    print ("c")
elif (score>=55 and score<=59):
    print ("D+")
elif (score>=50 and score<=54):
    print ("D")
elif (score>=0 and score<=49):
    print ("F")   
else:
    print ("คะแนนนไม่ถูกต้อง")   
#EX.10-โปรแกรมคำนวณเกรด
score = int(input("คะแนน  :"))
if (score>=80 and score<100):
    print("A")
elif (score>=75 and score<=79):
    print ("B+")
elif (score>=70 and score<=74):
    print ("B")
elif (score>=65 and score<=69):
    print ("C+")
elif (score>=60 and score<=64):
    print ("c")
elif (score>=55 and score<=59):
    print ("D+")
elif (score>=50 and score<=54):
    print ("D")
elif (score>=0 and score<=49):
    print ("F")   
else:
    print ("คะแนนนไม่ถูกต้อง")   

 #vr.2
 # ถ้าเขียนเป็นบรรทัดเดียว
def gradev2(score):    
    print((score < 0 or score >100) and "error" or "FFFFFDCBAAAA"[score//9])
gradev2(score)      
