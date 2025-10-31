#input
numberLargest = int(input("Enter the Largest number: "))
numberSmallest = int(input("Enter the Smallest number: "))
#loop
while numberSmallest:
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("H.C.F is: ",numberLargest)