print("Armstrong Number Checker\n")
num = int(input("Enter the number: "))
s = str(num)
n = len(s)
result = 0
temp = num
while temp != 0:
    digit = temp % 10
    result = result + digit**n
    temp = temp//10
if (num==result):
    print("Yes the number is an Armstrong number.")
else:
    print("No, the number is not an Armstrong number.")