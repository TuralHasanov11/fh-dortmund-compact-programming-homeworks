def countWordOccurrences(s: str) -> dict:
    container: list = s.replace('.', ' ').replace(',', ' ').split(" ")
    container = [x for x in container if x.strip()]
    result: dict = {}

    for word in container:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


def main():
    s = input("Enter string: ")
    occurrencesDict = countWordOccurrences(s)
    occurrencesString = ', '.join(
        f'{key} = {value}' for key, value in occurrencesDict.items())
    print(occurrencesString)


if __name__ == '__main__':
    main()
