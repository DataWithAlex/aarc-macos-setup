# create_test_file.py

def create_text_file():
    filename = "test.txt"
    content = "This is a test file created by the Python script."

    # Create and write to the file
    with open(filename, "w") as file:
        file.write(content)

    print(f"'{filename}' has been created with the content.")

if __name__ == "__main__":
    create_text_file()