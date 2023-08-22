#แสดงข้อมูลหลายๆ ประเภทใน print เดียว
#1. ใช้ ,
print("SAU",555,123,456,True,10+50)

#2. ใช่ + มีข้อแม้ ข้อมูลที่ใฃ้ String ต้องแปลงเป็น String
print("SAU "+str(555)+" "+str(123,456)" "+str(True)" "+str(10+50))

#3. ใช้เมธอตฃื่อ format
print("SAU () () () ()" ,format(555, 323,456, True, 10+50))
print("SAU (0) (1) (2) (3)" ,format(555, 323,456, True, 10+50))

#4. ใฃ้ f+ string '''
print(f'SAU(555) (123,456) (True) (10+50)')

""""""""""""

print("555"), print(111); print(False)
