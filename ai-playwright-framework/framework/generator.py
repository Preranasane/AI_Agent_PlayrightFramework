import os
from framework.llm_agent import generate_test_code

INPUT_FILE = "testcases.txt"
OUTPUT_DIR = "tests/generated/"

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(INPUT_FILE, "r") as f:
        testcases = f.readlines()

    for i, testcase in enumerate(testcases, start=1):
        code = generate_test_code(testcase.strip())
        filename = os.path.join(OUTPUT_DIR, f"test_case_{i}.py")
        with open(filename, "w") as out:
            out.write(code)
        print(f"Generated: {filename}")

if __name__ == "__main__":
    main()