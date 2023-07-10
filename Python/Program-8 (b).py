f1 = "sample.txt"
f2 = "sample2.txt"
try:
    with open(f1, 'a') as start, open(f2, 'r') as end:
        content = end.read()
        start.write(content)
        start.seek(0)  # Move the file pointer back to the beginning of the file
        print(start.read())
except FileNotFoundError:
    print("File not found.")
