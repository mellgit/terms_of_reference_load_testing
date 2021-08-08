import sys


def main():
    # print(f"{sys.argv[1]=}\n{sys.argv[2]=}") # работа с аргументами
    # n = sys.argv[1]
    # m = sys.argv[2]
    filling_the_array(5, 4)


def filling_the_array(n, m):
    # k = 1
    # ln = []
    # for i in range(2):
    #     if len(ln) == 0:
    #         ln.append([])
    #         for j in range(m):
    #             ln[i].append(k)
    #             k+=1
    #     else:
    #         ln.append([])
    #         k = ln[0][-1]
    #         for j in range(m):
    #             if k > n:
    #                 k = 1
    #             ln[i].append(k)
    #             k+=1
    
    # print(ln[-1][-1])

    k = 1
    i = 0
    q = 0
    ln = []
    while True:
        
        if len(ln) == 0:
            ln.append([])
            for j in range(m):
                ln[i].append(k)
                k+=1
            i+=1
            
        else:
            if ln[-1][-1] == ln[0][0]:
                break
            ln.append([])   
            k = ln[q][-1]
            q+=1
            for j in range(m):
                if k > n:
                    k = 1
                ln[i].append(k)
                k+=1
                
            i+=1
            
    
    print(ln)
    print(ln[-1][-1])
    print(ln[0][0])

    for i in range(len(ln)):
        print(ln[i][0], end='')
    print()
   


if __name__ == "__main__":
    main()