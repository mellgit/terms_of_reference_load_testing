from sys import argv

def main():
    print(center_and_radius())
    print()
    print(coordinates())


def center_and_radius():
    # print(f'{argv[1]=}\n{argv[2]=}')
    # int(''.join(i for i in just if i.isdigit()))
    file_name = "file1.txt"
    ln = []
    with open(file_name, "r") as file1:
        for line in file1.read():
            # ln.append(int(line.strip('\n').replace(' ', '')))
            # return int(''.join(i for i in line if i.isdigit()))
            # print(line)
            ln.append(int(''.join(i for i in line if i.isdigit())))
    return ln


def coordinates():
    # print(f'{argv[1]=}\n{argv[2]=}')
    file_name = "file2.txt"
    ln = []
    with open(file_name, "r") as file2:
        for line in file2:
            ln.append(int(line.strip('\n').replace(' ', '')))
    return ln


if __name__ == "__main__":
    main()

