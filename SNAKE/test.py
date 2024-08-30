def high_score():
    with open("snake_data.txt", "r") as file:
        return file.read()
print(high_score())