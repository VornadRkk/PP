import csv


# -*- coding: utf-8 -*-
def create_x_and_y(csvfile: str) -> None:
    """
    Read data from a CSV file and split it into two separate CSV files.

    Parameters:
    - csvfile (str): The path to the input CSV file containing weather data.

    Returns:
    - None: This function does not return any value."""
    with open(csvfile, newline="") as f:
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
            file_writer = csv.writer(
                open("dataset-number.csv", "a", newline=""), lineterminator="\r"
            )
            file_writer.writerow([row["data"]])
            file_writer = csv.writer(
                open("dataset-data.csv", "a", newline=""), lineterminator="\r"
            )
            file_writer.writerow(
                [
                    row["temp_morning"],
                    row["presure_morning"],
                    row["wind_morning"],
                    row["temp_evening"],
                    row["presure_evening"],
                    row["wind_evening"],
                ]
            )


if __name__ == "__main__":
    create_x_and_y("dataset.csv")
