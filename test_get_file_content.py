from functions.get_file_content import get_file_content

def main() -> None:
    print("Testing 'lorem.txt' (truncation test) ...")
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    print("-" * 40)
    
    print("Testing 'main.py' ...")
    print(get_file_content("calculator", "main.py"))
    print("-" * 40)

    print("Testing 'pkg/calculator.py' ...")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print("-" * 40)

    print("Testing '/bin/cat' (out of bounds test) ...")
    print(get_file_content("calculator", "/bin/cat"))
    print("-" * 40)

    print("Testing 'pkg/does_not_exist.py' (not found test) ...")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print("-" * 40)


if __name__ == "__main__":
    main()
