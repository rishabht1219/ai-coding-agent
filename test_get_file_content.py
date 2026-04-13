from funtions.get_file_content import get_file_content


def main():

    print('get_file_content("calculator", "lorem.txt")')
    content = get_file_content("calculator", "lorem.txt")

    print("Length:", len(content))
    print("Ends with truncation message?:", "truncated at" in content)

    print("\nget_file_content('calculator', 'main.py')")
    print(get_file_content("calculator", "main.py"))

    print("\nget_file_content('calculator', 'pkg/calculator.py')")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("\nget_file_content('calculator', '/bin/cat')")
    print(get_file_content("calculator", "/bin/cat"))

    print("\nget_file_content('calculator', 'pkg/does_not_exist.py')")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    main()