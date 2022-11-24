def sortList(inputList: list) -> list:
    return sorted(inputList, key=lambda i: int(i['model']), reverse=True)


def main():
    sampleList = [
        {'make': 'Nokia', 'model': 216, 'color': 'Black'},
        {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
        {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
    ]
    result = sortList(inputList=sampleList)
    print(result)


if __name__ == '__main__':
    main()
