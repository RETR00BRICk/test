with open("data.txt", "w") as file:
    for i in range(3):
        line = input(f"Enter line {i+1}: ")
        file.write(line + "\n")

print("Data saved to data.txt")