
students=["Nazli Güneş"]

students.append("Kemal Keskin")
#print(students)

students.pop(0)
#print(students)

students.extend(["Umut Aksu","Ayşe Yılmaz"])
#print(students)

for i in range(len(students)):
    print(students[i])

for i in range(len(students)):
    print("Öğrenci ad soyad :",students[i],"||","Öğrenci numarası :",i)


i=0
while(i<len(students)):
    students.pop()
    i+=1
    print(students)
    