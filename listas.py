def double(arr):
    return [x * 2 for x in arr]


def maximum(arr):
    return max(arr)


def average(arr):
    return sum(arr) / len(arr)


def main():
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [10, 20, 30]
    lista3 = [7, 3, 9, 2]

    print("Lista:", lista1)
    print("Double:", double(lista1))
    print("Maximum:", maximum(lista1))
    print("Average:", average(lista1))
    print()

    print("Lista:", lista2)
    print("Double:", double(lista2))
    print("Maximum:", maximum(lista2))
    print("Average:", average(lista2))
    print()

    print("Lista:", lista3)
    print("Double:", double(lista3))
    print("Maximum:", maximum(lista3))
    print("Average:", average(lista3))


if __name__ == "__main__":
    main()