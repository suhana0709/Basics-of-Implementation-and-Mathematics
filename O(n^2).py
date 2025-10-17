#oder of n^2  (n square)

def test(n):
    iteration = 0
    for i in range (0, n):
        for j in range (0, n):
            print("*", end="")
            iteration += 1
        print("")
    print("When n is ",n," iteration = ",iteration,"\n")

test(5)
test(10)
#when n=5 in line 11, 25 stars will be printed
