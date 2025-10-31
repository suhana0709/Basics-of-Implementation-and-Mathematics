print("Palindrome Checker\n")
#input
num = int(input("Enter the number: "))

#storing the original number for later comparison
original_num = num
reversed_num = 0

#Reversing the number
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

#comparing and printing
if (original_num == reversed_num):
    print(f"{original_num} is a palindrome.")
else:
    print(original_num,"is not a palindrome.")