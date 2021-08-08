import sys


def main():
    # вводимые аргументы
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    filling_the_array(n, m)


def filling_the_array(n, m):

    k = 1 # счетчик для вложенных списков ln[i][k]
    i = 0 # счетчик для основного списка ln[i]
    q = 0 # счетчик для длины обхода
    ln = [] # основной список

    while True:
        # заполнение первого вложенного пустого списка ln[[]]
        if len(ln) == 0:
            ln.append([])
            for j in range(m):
                ln[i].append(k)
                k+=1
            i+=1
            
        else:
            # заполнение последующих вложенных списков 
            if ln[-1][-1] == ln[0][0]: # концом будет являться первый элемент для выхода
                break
            ln.append([])   
            k = ln[q][-1]
            q+=1
            for j in range(m):
                if k > n: # проверка длины обхода
                    k = 1
                ln[i].append(k)
                k+=1
            i+=1

    for i in range(len(ln)):
        print(ln[i][0], end='')
    print()
   


if __name__ == "__main__":
    main()