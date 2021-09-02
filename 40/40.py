#This program solves Project Euler #40.

numbers = ""
for n in range(1,1000000):
    numbers += str(n)
print(int(numbers[0]) * int(numbers[9]) * int(numbers[99]) * int(numbers[999])
* int(numbers[9999]) * int(numbers[99999]) * int(numbers[999999]))

