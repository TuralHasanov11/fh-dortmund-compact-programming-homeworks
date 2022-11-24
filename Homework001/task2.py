if __name__ == '__main__':
    container = input("Enter your first name and last name: ")
    result = container.split(' ')
    result.reverse()
    result = ' '.join(result)
    print(f"Result: {result}")
