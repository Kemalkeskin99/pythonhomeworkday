
students=["Nazli Güneş"]

#question1;
students.append("Kemal Keskin")
#print(students)

#question2;
students.pop(0)
#print(students)

#question3;
students.extend(["Umut Aksu","Ayşe Yılmaz"])
#print(students)

#question4;
for i in range(len(students)):
    print(students[i])

#question5;
#path1
print("öğrenci Numarası: ",students.index("Kemal Keskin")," || ","Öğrencinin adı:",students[0])
print("öğrenci Numarası: ",students.index("Umut Aksu")," || ","Öğrencinin adı:",students[1])
print("öğrenci Numarası: ",students.index("Ayşe Yılmaz")," || ","Öğrencinin adı:",students[2])

#path2
for i in range(len(students)):
    print("Öğrenci ad soyad :",students[i],"||","Öğrenci numarası :",i)


#question6;
i=0
while(i<len(students)):
    students.pop()
    i+=1
    print(students)
