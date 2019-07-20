#LAB.16 -แสดงแม่สูตรคูณ
while(True):
    number = int(input("ป้อนตัวแม่สูตรคูณ  :"))
    if (number<0):
        break

    for i in range (1,13):
        print("%d*%d=%d"%(number,i,(number*i)))
    print("---------------------------------")
