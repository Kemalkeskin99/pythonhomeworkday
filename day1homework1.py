
#str => metinsel değerlerini tutmak için kullanılır üzerinde herhangi bir matematıksel işlemler yapılmaz

name =str("kemal")
print(name)

print("-----------------------------------")
#int => Tam sayı  değerini tutmak için kullanılır 
number1=int(10);
print(number1)


#float => ondalıklı sayı  değerini tutmak için kullanılır 
number2= float(10.2);
print(number2)

#complex => ileri düzey matamtiksel işlemlerde  kullanılır 
number3= complex(1j);
print(number3)

print("-----------------------------------")
#Boolean,bool => Doğru veya yanlış gibi cevabı olan seylerde kullanılır
number1=12;
if number1>10:
    print(True)
else:
    print(False)

print("-----------------------------------")

#dict / adresleme => veri  topluluğunu tutmak için kullanırız
kemal =dict(surname="keskin", age=23)
umut =dict(surname="aksu", age=22)
print(kemal)
print(umut)

print("-----------------------------------")
#diziler => aynı aynda birden fazla değeri tutmayı sağlarız
#list,tuple,range  
names=['kemal','umut','can',1]
print(names)

print("-----------------------------------")
#küme tipleri = birden çok öğeyi tek bir değişkende depolamak için kullanılır.
#set, frozenset
age=set((22,23,24,25))
print(age)

print("-----------------------------------")
#Binary tipler:
#bytes, bytearray, memoryview
number=bytes(20)
print(number)

#şart blogu ornegı 
userName="aliçamli@hotmail.com"
password=123456789

if userName=="aliçamli@hotmail.com" and password==1123456789:
    print("account open")
else:
    print("username or password false")


completionSratio=0
lessonfinish=True

if lessonfinish==True:
    completionSratio+10
    print( completionSratio+10)
else:
    print( completionSratio)