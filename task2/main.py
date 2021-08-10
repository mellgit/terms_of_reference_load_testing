from sys import argv

def main():
    search()


def search():
    # print(f'{argv[1]=}\n{argv[2]=}')
    with open(r"/home/mellgit/github/terms_of_reference_load_testing/task2/f1.txt", "r") as file1:
        # t = file1.readlines()
        for line in file1.readlines:
            print(line)


if __name__ == "__main__":
    main()