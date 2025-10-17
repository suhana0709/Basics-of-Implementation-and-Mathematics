#Oder of n
#Linear Time Complexity

def OnTime(n):
    iteration = 0
    for i in range (1, n+1):
        iteration += 1
    print("Number of iterations: ",iteration,("\n"))

OnTime(10)
OnTime(30)