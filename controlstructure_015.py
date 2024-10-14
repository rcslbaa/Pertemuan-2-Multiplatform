#no 1
'''
student_performance = int(input("Enter the student's performance: "))

if student_performance >= 90:
    print("Excellent")
elif student_performance >= 80:
    print("Very Good")
elif student_performance >= 70:
    print("Good")
elif student_performance >=60:
    print("Average")
else:
    print("Bad performance")

#no 2
a = int(input("masukan nilai bilangan pertama: "))
b = int(input("masukan nilai bilangan pertama: "))
c = int(input("masukan nilai bilangan pertama: "))

terbesar=max(a, b, c)
print("bilangan terbesar adalah: ", terbesar)

'''
#no 3
nilai_fibonacci = int(input('Masukan nilai fibonacci : '))
def fibonacci(n):
    a, b = 0,1
    hasil = []
    while a <= n:
        hasil.append(a)
        a, b = b, a + b
    return hasil
'''

deret_fibonacci = fibonacci(nilai_fibonacci)
print("Deret Fibonacci hingga", nilai_fibonacci, "adalah:", deret_fibonacci)

#no 4
nilai_odd = int(input('Masukan nilai: '))
def odd_number(n):
    for i in range(1, n + 1, 2):
        print(i, end=" ")
odd_number(nilai_odd)

#no 5
nilai = int(input('Masukan nilai untuk tinggi pola: '))
for i in range(1, nilai + 1): 
    print(str(i) * i)

'''