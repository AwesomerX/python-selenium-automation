# Homework Questions

# Question 1

number = int(input("Enter number:"))

sum_of_digits = 0
for digit in str(number):
    sum_of_digits += int(digit)

print(sum_of_digits)


# Question 2

lis = []

count = int(input('How many numbers in the list?'))

for n in range(count):
    number = int(input('Enter number:'))
    lis.append(number)

print("Largest number in the list is:", max(lis))

# Question 3

print("Enter the number:")

num = int(input())

odd = 0
even=0
while  (num!=0):
    rem = num % 10
    if rem % 2 == 1:
        odd += 1
    else:
        even += 1
    num//= 10

print("Number of even digits = ", even)
print("Number of odd digits = ", odd)


