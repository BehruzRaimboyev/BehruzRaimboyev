#begin1
a=float(input('a='))
P=4*a
print('perimetr=',P)

#begin2 
a=float(input('a='))
S=a**2
print('Yuzi=',S)

#begin3
a=float(input('a='))
b=float(input('b='))
P=2*(a+b)
S=a*b
print('perimetr=',P)
print('Yuzi=',S)

#begin4
pi=3.14
d=float(input('d='))
L=pi*d
print('aylana_yuzi=',L)

#begin5 
a=float(input('a='))
V=a**3
S=6*a**2
print('Hajm=',V)
print('tola_sirti=',S)

#begin6
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
V=a*b*c
S=2*(a*b+b*c+a*c)
print('hajm=',V)
print('tola_sirti=',S)

#begin7
pi=3.14
R=float(input('R='))
L=2*pi*R
S=pi*R**2
print('uzunligi=',L)
print('yuzasi=',S)

#begin8

a=float(input('a='))
b=float(input('b='))
O=(a+b)/2
print('orta_arifmetik=',O)

#begin9
a=float(input('a='))
b=float(input('b='))
import math
print('orta_arif=',math.sqrt(a*b))

#begin10
a=int(input('a='))
b=int(input('b='))
Y=a+b
K=a*b
A=a**2
B=b**2
print('yigindi=',Y)
print('kopaytma=',K)
print('Akv=',A)
print('Bkv=',B)

#begin11
a=float(input('a='))
b=float(input('b='))
Y=a+b
K=a*b
import math
print('yigindi=',Y)
print('kopaytma=',K)
print(abs(a))
print(abs(b))

#begin12
a=float(input('a='))
b=float(input('b='))
import math
M=math.sqrt(a**2+b**2)
P=2*(a+b)
print('Perimetr=',Y)
print('c=',math.sqrt((M)))

#begin13
pi=3.14
R1=float(input('R1='))
R2=float(input('R2='))
R1>R2
S1=pi*R1
S2=pi*R2
S3=pi*(R1-R2)
print('S1=',S1)
print('S2=',S2)
print('S3=',S3)

#begin14
L=float(input('L='))
pi=3.14
R=L/2
S=pi*R**2
print('radiusi=',R)
print('yuzi',S)

#begin15
S=float(input('S='))
pi=3.14
import math
R=abs(S/pi)
D=R*2
print('radius=',R)
print('diametr=',D)

#begin16
x1=float(input('x1='))
x2=float(input('x2='))
m=x2-x1
print('oraliq_masofa=',m)

#begin17
A=float(input('A='))
B=float(input('B='))
C=float(input('C='))
AC=A+B+C
BC=B+C
print('AC=',AC)
print('BC=',BC)

#begin18
A=float(input('A='))
B=float(input('B='))
C=float(input('C='))
AC=A+C
BC=B+C
print('AC=',AC)
print('BC=',BC)

#begin19
x1,y1=map(float(input('A=')))
x2,y2=map(float(input('B=')))
uzunlik=abs(x2-x1)
eni=abs(y2-y1)

P=2*(uzunlik+eni)
S=uzunlik*eni
print('perimetr=',P)
print('Yuzi=',S)

#begin 20
import math
x1, y1 = map(float, input('x1=y1=masofa=').split())
x2, y2 = map(float, input('x2=y2=masofa=').split())
masofa = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f'oraliq_masofa=',masofa)

#begin21
import math
x1, y1 = map(float, input("(x1, y1)=").split())
x2, y2 = map(float, input("(x2, y2)=").split())
x3, y3 = map(float, input("(x3, y3)=").split())
a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)  
c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)  

P = a + b + c
s = P / 2
S = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f'Perimetr=',P)
print(f'Yuza=',S)

#begin22
A=float(input('A='))
B=float(input('B='))
print('B=',A)
print('A=',B)

#begin23
A=float(input('A='))
B=float(input('B='))
C=float(input('C='))
print('B=',A)
print('A=',C)
print('C=',B)

#begin24
A=float(input('A='))
B=float(input('B='))
C=float(input('C='))
print('A=',C)
print('C=',B)
print('B=',A)

#begin25
X=float(input('X='))
Y=3*(X**6)-6*(X**2)-7
print('Y=',Y)

#begin 26
x=float(input('x='))
y=4*((x-3)**6)-7((x-3)**3)+2
print('y=',y)

#begin27
A=float(input('A='))
A2=A**2
A3=A**3
A8=A**8
print('A2=',A2)
print('A3=',A3)
print('A8=',A8)

#begin 28
A=float(input('A='))
A2=A**2
A3=A**3
A5=A**5
A10=A**10
A15=A**15
print('A2=',A2)
print('A3=',A3)
print('A5=',A5)
print('A10=',A10)
print('A15=',A15)

#begin29
L=float(input('L='))
pi=3.14
M=L/180*pi
print('M=',M)

#begin30
pi=3.14
x=float(input(burchak_radianini_kiriting=))
gradus=x*(180/pi)
print('burchak_gradusi=',gradus)

#begin31
TF=float(input('Ftemp='))
TC=(TF-32)*5/9
print('temp_selsiyda=',TC)

#begin32
TC=float(input('Ctemp='))
TF=TC*(9/5)+32
print('temp_farengeytda=',TF)

#begin33
x=float(input('kg_narxi='))
y=float(input('kanfet_kgsi='))
kg_narxi=x
ykg_narxi=y*X
print('1 kg narxi=',kg_narxi)
print('kg_narxi=',ykg_narxi)

#begin 34
A=float(input('choc_kg_narx='))
B=float(input('konf_kg_narx='))
if A>B:
    farq = A - B
    print(f"1 kg shokolad 1 kg konfetdan {farq} so'm qimmatroq")
elif A < B:
    farq = B - A
    print(f"1 kg konfet 1 kg shokoladga nisbatan {farq} so'm qimmatroq")
else:
    print("1 kg shokolad va 1 kg konfet narxlari teng")

#begin35
V=float(input('V_tezligi='))
U=float(input('U_tezligi'))
V>U
T1=float(input('oqim boyincha tezligi='))
T2=float(input('oqimga qarchi tezlik='))

S_oqim=(V+U)*T1
S_qarshi=(V-U)*T2
S=S_oqim+S_qarshi 
print('umumiy yul',S)

#begin36
V1=float(input('1avto_tezligi='))
V2=float(input('2avto_tezligi='))
V>U
S=float(input('avtolar orasidagi masofa='))
T=float(input('vaqt='))
M=S+(V1+V2)*T
print('T vaqtdan keyin oraliq masofa(km)=',M)

#begin37
V1=float(input('1avto_tezligi='))
V2=float(input('2avto_tezligi='))
S=float(input('avtolar orasidagi masofa='))
T=float(input('vaqt='))
M=S-(V1+V2)*T
if M<0 :
     print('mashinalar toqnashsa')
else :
     print('T vaqtdan kyn oraliq masofa=',M)

#begin38
A=float(input('A(A!=0)='))
B=float(input('B='))
X=-B/A
print('answer:x={X}')

#begin39
import math
A = float(input("A(A != 0)= "))
B = float(input("B= "))
C = float(input("C= "))
D = B**2 - 4 * A * C
if D > 0:
    x1 = (-B + math.sqrt(D)) / (2 * A)
    x2 = (-B - math.sqrt(D)) / (2 * A)
    print(f"Answers: x1 = {x1}, x2 = {x2}")
else:
    print("Bo'sh to'plam")

#begin40
A1 = float(input("A1= "))
B1 = float(input("B1= "))
C1 = float(input("C1= "))
A2 = float(input("A2= "))
B2 = float(input("B2= "))
C2 = float(input("C2= "))
D = A1 * B2 - A2 * B1
if D != 0:
    x = (C1 * B2 - C2 * B1) / D
    y = (A1 * C2 - A2 * C1) / D
    print(f"Answers: x = {x}, y = {y}")
else:
    print("Bo'sh to'plam")


