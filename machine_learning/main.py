import re
import csv


if __name__ == "__main__":
    # load the dataset.txt
    with open("dataset.txt", "r") as file:
        dataset = file.read()

    lines = dataset.split("\n")
    columns = []
    for line in lines:
        column = re.split(r"\s+", line)
        columns.append(column)
    columns = columns[:-1]

    with open("dataset.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(columns)
