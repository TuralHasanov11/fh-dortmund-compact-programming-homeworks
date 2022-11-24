def countVowels(s: str) -> int:
    vowels = ('a', 'o', 'u', 'e', 'i')
    result = 0
    for v in vowels:
        result += s.count(v)
    return result


if __name__ == '__main__':
    s = input("Enter word: ")
    print(f"The number of vowels in string is: {countVowels(s)}")
