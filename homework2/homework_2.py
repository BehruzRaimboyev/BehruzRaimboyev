#number date type 
# exercise1
print('first exercise')

num = float(input("Enter a float number: "))
rounded_num = round(num, 2)        
print(f"Rounded number: {rounded_num:.2f}")

#exercise2
print('second exercise')

number_1=float(input('first_number:'))
number_2=float(input('second number:'))
number_3=float(input('third number:'))
 
largest=max(number_1,number_2,number_3)
smallest=min(number_1,number_2,number_3)
print(f'largest number {largest}')
print(f'smallest number {smallest}')

#exercise 3
print('exercise 3')

km=float(input('km:'))
meters=km*1000
santimetr=km*100000
print(f'kilometrs in meters:{meters}')
print(f'kilometrs in santimetrs:{santimetr}')

#exercise 4
print('exercise 4')

num1=int(input('first number:'))
num2=int(input('second number:'))
int_divis=num1//num2
remainder=num1%num2
print(f'int division result:{int_divis}')
print(f'remainder:{remainder}')

#exercise 5
print('exercise 5')

celsius=float(input('enter temp in:'))
fahrenheit=(celsius*5/9)+32
print(f'{celsius} *C is equel to {fahrenheit}*F')

#exercise 6
print('exercise 6')

number=int(input('give number:'))
digit=abs(number)%10
print(f'last digit of {number} is {digit}')

#exercise 7
print('exercise 7')

number=int(input('give number:'))
if number % 2==0:
     print(f'{number} is even')
else: 
     print(f'{number} is odd') 

#exercise 8
print('exercise 8')

a=input('a=')
b=input('b=')
a,b=b,a
print(f'swapping:a={a},b={b}')

#String data type 
#exercise 1
print('string data type:')
print('exercise 1')
a=input('give word:')
c=a.title()
print(f'capitalized sentence:{c}')

#exercise 2
print('exercise 2')
a=input('give string: ')
vowels='aeiouAIEUO'
bb=''.join(char for char in a if char not in vowels)
print(f'string without vowels:{bb}')

#exercise 3
print('exercise 3')
a=input('give string:')
b=a[::-1]
print(f'reversed string:{b}')

#exercise 4
print('exercise 4')
a=input('give string:')
w=a.replace('','_')
print(f'with underscores:{w}')

#exercise 5
print('exercise 5')
word = input("Enter a word: ")
n_w=word.lower()
if n_w == n_w[::-1]:
    print(f"The word '{word}' is a palindrome.")
else:
    print(f"The word '{word}' is not a palindrome.")
#exercise 6
print('exercise 6')
a = input("Enter a string: ")
b = a.replace('a', 'o')
print("Modified string:",b)

#exercise 7
print('exercise 7')
email = input("Enter your email address: ")
username=email.split('@')[0]
print(f'the username is:{username}')

#exercise 8
print('exercise 8')
a=input('give string:')
m=a.title()
print(f'title case:{m}')

#exercise 9
print('exercise 9') 
a=input('give a string:') 
b=len(a)>1
mm=a[1:-1]
print(f'modified string:{mm}')

#exercise 10
print('exercise 10')
a=input('give string:')
word=input('enter a word to check:')
bb=word in a
print(f"the word '{bb}' is present in the sentence")


#exercise 11
print('exercise 11')
a=input('give a string:')
b=input('give string to find:')
position=a.find(b)
bb=position!=-1
print(f"the first occurence of '{b}' is at position {bb}")

#exercise 12
print('exercise 12')
txt=input('give a string:')
print(txt[-3:-1])

#exercise 13
print('exercise 13')
a=input('give a string:')
b=int(input('the number of times reapet the string'))
repeated=a*b
print(f'repeated string:{repeated}')

#exercise 14
print('exercise 14')
sentence=input('give a sentence:')
words=sentence.split()
print(f'new line {words}')

#exercise 15
print('exercise 15')
a = input("Enter a string: ")
b=a[::2]
print('letters at even:',b)

#exercise 16
print('exercise 16')
a = input("Enter a title: ")
formatted_string = f"Title: {a}"
print(formatted_string)

#exercise 17
print('exercise 17')
a = input("Enter a sentence: ")
b=a[::-1]
print(f'reversed sentence:{b}')

#exercise 18
print('exercise 18')
a=input('give first string:')
b=input('give second string:')

aa=len(a)
bb=len(b)
mm=abs(aa-bb)
print(f'diffence between two string:{mm}')

#boolean data type 
#exercise 1
print('boolean data type')
print('exercise 1')

username = input("Enter your username: ")
password = input("Enter your password: ")
if username and password:
      print("Succesfully:")
else:
    print("Error: it must be non-empty.")     

#exercise 2
print('exercise 2')
a=float(input('give first number:'))
b=float(input('give second number:'))
bb= a==b
print(bb)

#exercise 3
print('exercise 3')
number=float(input('give a number:'))
bb=number>0 and number%2==0
print(bb)

#exercise 4
print('exercise 4')
number1=float(input('give 1-number:'))
number2=float(input('give 2-number:'))
number3=float(input('give 3-number:'))
bb=number1!=number2 and number1!=number3 and number2!=number3
print(bb)

#exercise 5
print('exercise 5')
a1=input('give 1-string:')
a2=input('give 2-string:')
bb=len(a1)==len(a2)
print(bb)

#exercise 6
print('exercise 6')
number=int(input('give me number:'))
if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")

#exercise 7
print('exercise 7')
number1=float(input('give 1-number:'))
number2=float(input('give 2-number:'))
if (number1 + number2) > 50:
    print("The sum of the two numbers is greater than 50.")
else:
    print("The sum of the two numbers is not greater than 50.")

#exercise 8
print('exercise 8')
a=float(input('give me number:'))
if 10 <= number <= 20:
    print("The number is between 10 and 20 (inclusive).")
else:
    print("The number is'nt between 10 and 20.")



