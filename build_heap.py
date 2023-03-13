# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n, -1, -1):
         sort_heap(data, i, n)
    for i in range(n-1,0,-1):
         data[0], data[i] = data[i], data[0]
         sort_heap(data, i, 0)
    print(data)

    return swaps

def sort_heap(data, i , n , swaps):
     left = 2*i+1
     rigth = 2*i+2

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    izvele = input()
    
    if izvele[0] == 'I':
        n = int(input("Ievadiet skaitļu daudzumu: "))
    # input from keyboard
        parents = list(map(int, input("Enter the parent nodes separated by spaces: ").split()))

    # checks if lenght of data is the same as the said lenght
    elif izvele[0] == 'F':
        faila_nosaukums = input("Enter the file name: ")
        with open(F"./test/{faila_nosaukums}") as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))

    assert len(data) == n
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
