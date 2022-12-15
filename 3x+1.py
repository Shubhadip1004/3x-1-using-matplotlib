import sys
import matplotlib.pyplot as plt
x = int(input("Enter the number to be checked:"))
nt = 1
ylst = []
ylst.append(x)
xlst = []
while x:
    if x % 2 == 0:
        x = x/2
        ylst.append(x)
        nt += 1
        if x == 1:
            print("The number of times is", nt)
            for i in range(1, nt+1):
                j = int(i)
                xlst.append(j)
            print(ylst)
            plt.plot(xlst, ylst)
            plt.xlabel("X-Axis")
            plt.ylabel("Y-Axis")
            plt.title("3X+1")
            plt.show()
            sys.exit(0)
    else:
        x = 3*x
        x = x+1
        ylst.append(x)
        nt += 1
        if x == 1:
            print("The number of times is", nt)
            for i in range(1, nt+1):
                j = int(i)
                xlst.append(j)
            print(ylst)
            plt.plot(xlst, ylst)
            plt.xlabel("X-Axis")
            plt.ylabel("Y-Axis")
            plt.title("3X+1")
            plt.show()
            sys.exit(0)
