#LAB.14 การเพิ่มสมาชิก List ด้วย Loop
product = []
while (True):
    stock=input("ป้อนสินค้า")
    if(stock=="exit"):
        break
    product.append(stock)
print (product)  
