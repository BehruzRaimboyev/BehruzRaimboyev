
#exercise 1
print("ex 1")
def abb(a,b):
    try:
        return a/b
    except ZeroDivisionError as rr:
        print('zere division error:')
        print(rr)
n=abb(2,0)
print('output',n)

#exercise 2
print("ex 2")
def addnb(prompt):
    try:
        value=int(prompt)
        return value
    except ValueError:
        print('Error:Input a valid integer.')

n=addnb('abs')
print('input value:',n) 


#exercise 3
print("ex 3")
def open_file(file):
    try:
        with open(file,'r') as file:
            content=file.read()
            print('File content:')
            print(content)
    except FileNotFoundError:
        print(f"Error: File  {file} does not exists")

if __name__ == "__main__":
    file_name="exet.txt"
    open_file(file_name)


# exercise 4
print("ex 4")
def get_numeric_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid input. Please Input a valid number.")

n1 = get_numeric_input('Give first number:')
n2 = get_numeric_input('Give second number:')
result = n1 * n2
print("Product of the said two numbers:", result)



# exercise 5
print("ex 5")
def bbn(filename):
    try:
        with open(filename,'r') as file:
            content=file.read()
            print('file content:')
            print(content)
    except PermissionError:
        print("Error: Permission denied to open the file.")


file_name=input("input a file name:")
bbn(file_name)

# exercise 6
print("ex 6")

def tete(data,index):
    try:
        result=data[index]
        print('Result:',result)
    except IndexError:
        print("Error:Index out of range.")

nums=[1,2,3,4,5,6,7,8,9]
index=int(input('give the index:'))
tete(nums,index)

# exercise 7
print("ex 7")
try:
    number=int(input('Give a number:'))
    print("entered number:",number)
except KeyboardInterrupt:
    print("input canceled by user.")

# exercise 8
print("ex 8")
def division(aa,bb):
    try:
        result=aa/bb
        print(f"result:{result}")
    except ArithmeticError:
        print("Error:Arithmetic Error occured")
aa=float(input("give dividend:"))
bb=float(input("input the divisor:"))
division(aa,bb)

# exercise 9
print("ex 9")
def open_file(filename):
    encoding=input("input the encoding(ASCII,UTF-16,UTF-8)for the file:")
    try:
        with open(filename,'r',encoding=encoding) as file:
            content=file.read()
            print('file content:')
            print(content)
    except UnicodeDecodeError:
        print("ERROR:encoding issue occured while reading the file")

file_name=input('input the file name:')
open_file(file_name)

# exercise 10
print("ex 10")

def test_list(num):
    try:
        r=len(num)
        print(f"length of the list:{r}")
    except AttributeError as bb:
        print("ERROR: the list does not have a length attribute.")
        print(bb)

num=[1,2,3,4,5,6]
test_list(num)
