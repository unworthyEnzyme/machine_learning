import re
import csv


if __name__ == "__main__":
    # load the dataset.txt
    with open("dataset.txt", "r") as file:
        lines = file.readlines()

    with open("dataset.csv", "w") as file:
        for line in lines:
            file.write(",".join(line.split()) + "\n")
