def main():
    sampleList = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'omnus']
    result = list(map(lambda value: [value], sampleList))
    print(result)


if __name__ == '__main__':
    main()
