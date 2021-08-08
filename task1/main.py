import sys


def main():
    # print(f"{sys.argv[1]=}\n{sys.argv[2]=}") # работа с аргументами
    filling_the_array()


def filling_the_array():
    k = 1
    ln = []
    for i in range(2):
        ln.append([])
        for j in range(4):
            ln[i].append(k)
            k+=1
    print(ln)

    for i in range(len(ln)):
        print(ln[i][0])


if __name__ == "__main__":
    main()