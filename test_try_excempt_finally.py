try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
finally:
    if 'file' in locals():
        file.close()  # Ensure the file is closed
