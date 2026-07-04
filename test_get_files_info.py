from functions.get_files_info import get_files_info

def main() -> None:
    print("Testing '.' ...")
    print(get_files_info("calculator", "."))
    print("-" * 40)

    print("Testing '/bin' ...")
    print(get_files_info("calculator", "/bin"))
    print("-" * 40)

    print("Testing '../' ...")
    print(get_files_info("calculator", "../"))
    print("-" * 40)

    print("Testing 'main.py' ...")
    print(get_files_info("calculator", "main.py"))
    print("-" * 40)


if __name__ == "__main__":
    main()
