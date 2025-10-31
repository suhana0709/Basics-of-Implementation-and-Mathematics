#input
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

#checking for the greater number
if (num1>num2):
    greater = num1
else:
    greater = num2

#loop
while True:
    if (greater % num1 == 0) and (greater % num2 == 0):
        lcm = greater
        break
    greater += 1

print("LCM: ", greater)