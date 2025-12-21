#Exercise1 modulus
a =int(input("a="))
x=a%2 #sisa nila a dibagi 2
if (x>0):
    print("bilangan ganjil")
else:
    print("bilangan genap")


#Exercise2 age
age =int(input("age="))
if(age<=1):
    print ("Baby")
elif((age>=1) and (age<=3)):
    print("Toodler")
elif((age>=3) and (age<=5)):
    print("Prescholer")
elif((age>=5) and (age<=12)):
    print("Child")
elif((age>=12) and (age<=17)):
    print("Teenager")
elif((age>=17) and (age<=21)):
    print("Young Adult")
elif((age>=21) and (age<=30)):
    print("Pre-adult")
elif((age>=30) and (age<=50)):
    print("Adult")
elif((age>=50) and (age<=70)):
    print("Pre-elderly")
else:
    print("Ederly")
    

#Exercise3 konversi suhu
suhu =float(input("suhu="))
deg=input("satuan suhu=")
ctf=suhu*(9/5)+32
ctk=suhu+273.15
ftc=(32-suhu)*(5/9)
ftk=((32-suhu)*(5/9))+273.15
ktc=suhu-273.15
ktf=((suhu-273.15)*(9/5))+32
if(deg=="celcius"):
    print("suhu in F=",ctf,"F")
    print("suhu in K=",ctk,"K")
elif(deg=="fahrenheit"):
    print("suhu in C=",ftc,"C")
    print("suhu in K=",ftk,"K")
elif(deg=="kelvin"):
    print("suhu in C=",ktc,"C")
    print("suhu in F=",ktf,"F")


#Exercise4 segitiga
a=float(input("panjang sisi a= "))
b=float(input("panjang sisi b= "))
c=float(input("panjang sisi c= "))
import math
if(a==b==c):
    print("maka segitiga sama sisi")
elif((a==b) or (a==c) or (b==c)):
    print("maka segitiga sama kaki ")
elif((a+b<c) or (a+c<b) or (b+c<a)):
    print("maka bukan segitiga")
elif(a==math.sqrt(b**2+c**2) or (b==math.sqrt(c**2+a**2)) or (c==math.sqrt(a**2+b**2))):
    print("maka segitiga siku-siku")
else:
    print("maka segitiga sembarang")


#Exercise5 diskriminan
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if(a==0):
    print("maka bukan persamaan kuadrat")
else:
    D=((b*b)-(4*a*c))
    print("diskriminan=",D)
    if(D>0):
        print("maka dua akar yang berbeda")
    elif(D<0):
        print("maka akar imajiner")
    else:
        print("maka akar ganda")
