import csv
import os
def get_data_for_date(csv_filename, target_date):
    with open(csv_filename, newline='') as f:
        fieldnames = ['data', 'temp_morning', 'presure_morning', 'wind_morning', 'temp_evening', 'presure_evening', 'wind_evening']
        reader = csv.DictReader(f, fieldnames=fieldnames)

        for row in reader:
            date = row['data']
            if date == target_date:
                return {
                    "data": row['data'],
                    "temp_morning": row['temp_morning'],
                    "presure_morning": row['presure_morning'],
                    "wind_morning": row['wind_morning'],
                    "temp_evening": row['temp_evening'],
                    "presure_evening": row['presure_evening'],
                    "wind_evening": row['wind_evening']
                }
    return None
csv_filename = 'dataset.csv'
target_date = '2023-10-27'
data = get_data_for_date(csv_filename, target_date)

if data:
    print("database for data", target_date, "find:")
    print(data)
else:
    print("database for data", target_date, "don't find.")

