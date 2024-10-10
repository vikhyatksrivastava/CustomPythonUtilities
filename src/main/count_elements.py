def count_elements_of_list(lista):
    counts = {}
    for element in lista:
        counts[element] = counts.get(element, 0) + 1
    for element, count in counts.items():
        print(f"{element} appears {count} times.")
    return counts


def main():
    lista = ['a', 'b', 'c', 'a', 'b', 'c', 'd']
    print(count_elements_of_list(lista))


if __name__ == '__main__':
    main()
