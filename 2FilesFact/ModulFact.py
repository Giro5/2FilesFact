import sys

def main(x):
    i = x - 1 
    while(i > 1):
        x *= i
        i -= 1
    print(x)

main(int(sys.argv[1]))