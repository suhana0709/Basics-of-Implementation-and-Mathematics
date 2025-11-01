from math import sqrt  


def cprime(n):
    if n < 2:                     
        return False              
    for i in range(2, int(sqrt(n)) + 1):  
        if n % i == 0:           
            return False
    return True                   


def Pprint(num):
    if num > 10:                  
        for i in range(10, num + 1):  
            if cprime(i):         
                print(i)          


num = int(input("Enter the number: "))
Pprint(num)
