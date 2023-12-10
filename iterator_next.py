import csv

# -*- coding: utf-8 -*-


class DataIterator:
    def __init__(self, csv_filename: str):
        self.csv_filename = csv_filename
        self.data_iter = self.data_generator()

    def data_generator(self):
        with open(self.csv_filename, newline="") as f:
            fieldnames = [
                "data",
                "temp_morning",
                "presure_morning",
                "wind_morning",
                "temp_evening",
                "presure_evening",
                "wind_evening",
            ]
            reader = csv.DictReader(f, fieldnames=fieldnames)
            for row in reader:
                date = row["data"]
                data = {
                    "данные": date,
                    "температура_утром": row["temp_morning"],
                    "давление_утром": row["presure_morning"],
                    "ветер_утром": row["wind_morning"],
                    "температура_вечером": row["temp_evening"],
                    "давление_вечером": row["presure_evening"],
                    "ветер_вечером": row["wind_evening"],
                }
                yield data

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.data_iter)
        except StopIteration:
            raise StopIteration


if __name__ == "__main__":
    csv_filename = "dataset.csv"
    data_iter = DataIterator(csv_filename)
    try:
        next_data = next(data_iter)
        if next_data:
            print(next_data)
        else:
            print("don't database.")
    except StopIteration:
        print("don't database.")
    try:
        next_data = next(data_iter)
        if next_data:
            print(next_data)
        else:
            print("don't database.")
    except StopIteration:
        print("don't database.")
