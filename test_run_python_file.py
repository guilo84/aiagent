from functions.run_python_file import run_python_file

def main():
    print("--- Test 1: Run main.py (No args) ---")
    result1 = run_python_file("calculator", "main.py")
    print(result1)
    print("\n" + "="*50 + "\n")

    print("--- Test 2: Run main.py (With args) ---")
    result2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result2)
    print("\n" + "="*50 + "\n")

    print("--- Test 3: Run tests.py ---")
    result3 = run_python_file("calculator", "tests.py")
    print(result3)
    print("\n" + "="*50 + "\n")

    print("--- Test 4: Path Escaping ---")
    result4 = run_python_file("calculator", "../main.py")
    print(result4)
    print("\n" + "="*50 + "\n")

    print("--- Test 5: Non-existent file ---")
    result5 = run_python_file("calculator", "nonexistent.py")
    print(result5)
    print("\n" + "="*50 + "\n")

    print("--- Test 6: Non-Python file ---")
    result6 = run_python_file("calculator", "lorem.txt")
    print(result6)
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
