from functions.write_file import write_file

def main() -> None:
    print("Testing overwriting an existing file ('lorem.txt') ...")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("-" * 40)
    
    print("Testing writing to a new file in a subdirectory ('pkg/morelorem.txt') ...")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("-" * 40)

    print("Testing out-of-bounds write attempt ('/tmp/temp.txt') ...")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print("-" * 40)


if __name__ == "__main__":
    main()
