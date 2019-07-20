#function รับค่าโดยที่ไม่จำกัด
def summation(v1,v2,v3):   
    return v1+v2+v3  
def summation2(v1,v2):   
    return v1+v2    
def summation3(*var): #ส่งค่า list หลายๆค่า 
    sumvalue=0 
    for a in range(len(var)) :
       sumvalue+=var[a]
    return sumvalue
result=summation3(10,30,12)
print("Result = ",result)   