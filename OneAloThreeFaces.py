num = int(input("Enter the number: "))
#1st
print("\nFirst")
sum = 0
for i in range (1, num+1):
    sum += i
    print("Step ",i)
print("Result: ", sum)

#2nd
print("\nSecond")
print("Result: ",(num*(num+1))/2)

#3rd
print("\nThird")
sum = 0
for i in range(1, num+1):
    for j in range(i, i+1):
        sum += j
print("Result: ",sum)