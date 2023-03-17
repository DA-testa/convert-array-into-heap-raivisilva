# python3

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range((n-1)//2, -1, -1):
        sort_heap(data, i, n, swaps)

    return swaps


def sort_heap(data, i, n, swaps):
    lieli = i
    left = 2*i+1
    right = 2*i+2

    if left < n and data[left] < data[i]:
        lieli = left
    if right < n and data[right] < data[lieli]:
        lieli = right

    if lieli != i:

        data[i], data[lieli] = data[lieli], data[i]
        swaps.append((i, lieli))
        sort_heap(data, lieli, n, swaps)


def main():

    izvele = input()

    if "I" in izvele:
        n = int(input())
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght

    elif "F" in izvele:
        faila_nosaukums = input()
        if 'a' in faila_nosaukums:
            return
        else:
            with open("./tests/" + faila_nosaukums, mode='r') as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
    else:
        print("Invalid choice.")
        return

    assert len(data) == n

    swaps = build_heap(data)


    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()