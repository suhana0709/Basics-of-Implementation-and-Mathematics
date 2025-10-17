def myfunction(n):
    iteration = 0
    for i in range (0, n+1):
        iteration += 1
        print("First Loop")

    j=1
    while(j<=n+1):
        iteration += 1
        print("Second Loop ",j)
        j=j*2
    
    for i in range(0, 100):
        iteration += 1
        print("Third Loop")
    num = iteration

    print("\nTotal number of iterations: ",num)
myfunction(5)