try:
    file = "sample.txt"
    with open(file, 'r') as file_obj:
        n = int(input("Enter the number of lines to be read: "))
        for i in range(n):
            line = file_obj.readline().strip()
            if line:
                print(line)
            else:
                break
except FileNotFoundError:
    print("File not found.")
