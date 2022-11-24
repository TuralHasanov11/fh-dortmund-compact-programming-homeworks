from operator import itemgetter


def sortList(inputList: list) -> list:
    return sorted(inputList, key=itemgetter(1))


def main():
    sampleList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    result = sortList(inputList=sampleList)
    print(result)


if __name__ == '__main__':
    main()
