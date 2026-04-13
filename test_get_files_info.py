from funtions.get_files_info import get_files_info


def main():
    print('get_files_info("calculator", "."):')
    print("Result for current directory:")
    result = get_files_info("calculator", ".")
    for line in result.split("\n"):
        print(" ", line)

    print("\nget_files_info('calculator', 'pkg'):")
    print("Result for 'pkg' directory:")
    result = get_files_info("calculator", "pkg")
    for line in result.split("\n"):
        print(" ", line)

    print('\nget_files_info("calculator", "/bin"):')
    print("Result for '/bin' directory:")
    result = get_files_info("calculator", "/bin")
    print(" ", result)

    print('\nget_files_info("calculator", "../"):')
    print("Result for '../' directory:")
    result = get_files_info("calculator", "../")
    print(" ", result)


if __name__ == "__main__":
    main()