# -*- coding: utf-8 -*-
import csv
from typing import Optional


def get_data_for_date(csv_filename: str, target_date: str) -> Optional[dict]:
    """
    Parameters:
       - csv_filename (str): The path to the CSV file containing weather data.
       - target_date (str): The date for which weather data is requested.

       Returns:
       - dict or None: A dictionary containing weather data for the specified date
         with keys 'data', 'temp_morning', 'presure_morning', 'wind_morning',
         'temp_evening', 'presure_evening', 'wind_evening'. If the specified date
         is not found in the CSV file, returns None.
    """
    with open(csv_filename, newline="") as f:
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
            if date == target_date:
                return {
                    "данные": row["data"],
                    "температура_утром": row["temp_morning"],
                    "давление_утром": row["presure_morning"],
                    "ветер_утром": row["wind_morning"],
                    "температура_вечером": row["temp_evening"],
                    "давление_вечером": row["presure_evening"],
                    "ветер_вечером": row["wind_evening"],
                }
    return None


if __name__ == "__main__":
    print(get_data_for_date("dataset.csv", "2008-09-15"))
